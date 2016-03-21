import os
import sys
from chunky.util.base import BaseCommand


class Command(BaseCommand):
    def usage(self):
        return 'Usage: chunky list [pipelines|configs]'

    def help_text(self):
        help_msg = 'Lists installed pipelines'
        return '\n'.join([self.usage(), help_msg])

    def run(self):
        sys.stdout.write('Installed pipelines (in {}):\n\n'.format(self.home_configs))
        if not os.path.isdir(os.path.join(self.user_home, '.chunky')):
            sys.stdout.write('No pipelines installed\n')
        else:
            sys.stdout.write('There are pipelines installed!\n')
