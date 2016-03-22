import subprocess
import sys
import os
from chunky.util.base import BaseCommand

ARGV_PIPELINE_NAME = 0
EXIT_CMD_SYNTAX_ERROR = 2


class Command(BaseCommand):
    def usage(self):
        return 'Easily install pipelines'

    def help_text(self):
        return ''

    def run(self):
        # Checks to see if they entered a pipeline name
        if not self.argv:
            sys.stdout.write('No pipeline provided to install.\n')
            sys.stdout.write(self.usage() + '\n')
            sys.exit(EXIT_CMD_SYNTAX_ERROR)

        # Get pipeline name from argv
        pipeline_name = self.argv[ARGV_PIPELINE_NAME]

        # Helper to check if pipeline exists
        pipeline_filepath = os.path.join(self.home_pipelines,
                                         '{}'.format(pipeline_name))

        # Check if pipeline already exists
        if os.path.exists(pipeline_filepath):
            overwrite = raw_input('Pipeline {} is already installed, overwrite? [y/n] '.format(
                    pipeline_name
            ))
            no_set = {'no', 'n'}
            # Terminate if user says no
            if overwrite.lower() in no_set:
                sys.exit(0)

        # Not quite sure how to get rid of the:
        # 'cp: cannot stat 'non_existant_file': No such file or directory' error

        # Make sure they don't input the wrong name
        try:
            subprocess.check_call(['cp', pipeline_name, self.home_pipelines])
            sys.stdout.write('Pipeline successfully installed\n')
        except (IOError, OSError, subprocess.CalledProcessError):
            sys.stdout.write('Pipeline not found\n')
            sys.exit(0)



