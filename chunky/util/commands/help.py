import os
import sys
import pkgutil
from importlib import import_module
from chunky.util.base import BaseCommand
import chunky.util.commands

FILENAME_WITHOUT_EXTENSION = 0
ARGV_COMMAND_NAME = 0


class Command(BaseCommand):
    command_name = os.path.splitext(os.path.basename(__file__))[FILENAME_WITHOUT_EXTENSION]

    def run(self):
        chunky_commands = [name for _, name, _
                           in pkgutil.iter_modules(chunky.util.commands.__path__)
                           if name != self.command_name]
        if self.argv and self.argv[ARGV_COMMAND_NAME] in chunky_commands:
            chunky_commands = [self.argv[ARGV_COMMAND_NAME]]

        base_module = 'chunky.util.commands.{}'
        for command in chunky_commands:
            sys.stdout.write(command + ':\n')
            module = import_module(base_module.format(command)).Command()
            sys.stdout.write(module.help_text() + '\n\n')
