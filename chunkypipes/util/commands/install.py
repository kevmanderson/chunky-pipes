import sys
import os
import shutil
import argparse
from chunkypipes.util.commands import BaseCommand

ARGV_PIPELINE_NAME = 0
EXIT_CMD_SUCCESS = 0
EXIT_CMD_SYNTAX_ERROR = 2


class Command(BaseCommand):
    @staticmethod
    def usage():
        return 'chunky install <pipeline>'

    def help_text(self):
        return 'Install a ChunkyPipes formatted pipeline.'

    def run(self, command_args):
        parser = argparse.ArgumentParser(prog='chunky install', usage=self.usage(), description=self.help_text())
        parser.add_argument('pipeline-name', help='Full path to a ChunkyPipes formatted pipeline to install.')
        pipeline_name = vars(parser.parse_args(command_args))['pipeline-name']
        if pipeline_name.lower() == 'help':
            parser.print_help()
            sys.exit(0)

        # Check if provided filepath actually exists
        if not os.path.isfile(pipeline_name):
            sys.stderr.write('Pipeline not {} found.\n'.format(pipeline_name))
            sys.exit(EXIT_CMD_SYNTAX_ERROR)

        # Check if pipeline already exists
        if os.path.isfile(os.path.join(self.home_pipelines, pipeline_name)):
            overwrite = raw_input('Pipeline {} is already installed, overwrite? [y/n] '.format(
                    pipeline_name
            ))
            if overwrite.lower() in {'no', 'n'}:
                sys.exit(EXIT_CMD_SUCCESS)

        # Copy pipeline file
        try:
            shutil.copy2(pipeline_name, self.home_pipelines)
            sys.stdout.write('Pipeline {} successfully installed.\n'.format(pipeline_name))
        except (IOError, OSError, shutil.Error):
            sys.stdout.write('Pipeline {} could not be installed.\n'.format(pipeline_name))
            sys.exit(EXIT_CMD_SYNTAX_ERROR)
