import os
import sys
import errno
import argparse
from chunkypipes.util.commands import BaseCommand

ARGV_CHUNKY_HOME_ROOT = 0


# Based off https://stackoverflow.com/a/600612/1539628
def mkdir_p(path):
    try:
        os.makedirs(path)
    except OSError as os_error:
        if os_error.errno != errno.EEXIST or not os.path.isdir(path):
            raise


def make_chunky_home(chunky_home_root):
    chunky_root_pipelines = os.path.join(chunky_home_root, '.chunky', 'pipelines')
    chunky_root_configs = os.path.join(chunky_home_root, '.chunky', 'configs')
    try:
        # Make directory tree
        mkdir_p(chunky_root_pipelines)
        mkdir_p(chunky_root_configs)

        # Add __init__.py to make modules
        os.mknod(os.path.join(chunky_root_pipelines, '__init__.py'), 0o644)
        os.mknod(os.path.join(chunky_root_configs, '__init__.py'), 0o644)

        # Write out user messages
        sys.stdout.write('ChunkyPipes successfully initialized at {}\n'.format(chunky_home_root))
        if chunky_home_root != os.path.expanduser('~') and not os.environ.get('CHUNKY_HOME'):
            sys.stdout.write('Please set a CHUNKY_HOME environment variable to {}\n'.format(chunky_home_root))
    except OSError as e:
        sys.stderr.write('An error occurred initializing ChunkyPipes at {}.\n{}\n'.format(
            chunky_home_root,
            e.message
        ))


def usage():
    return 'chunky init [chunky_home_root]'


class Command(BaseCommand):
    def help_text(self):
        return ('Initializes ChunkyPipes at the given location.'
                'If no path is given, the user home directory is used. For any location other than '
                'the user home directory, the user '
                'needs to set a CHUNKY_HOME environment variable manually for ChunkyPipes '
                'to use the newly created directory.')

    def run(self, command_args):
        parser = argparse.ArgumentParser(prog='chunky init', usage=usage(), description=self.help_text())
        parser.add_argument('chunky-home-root', default='', nargs='?',
                            help=('ChunkyPipes will initialize in this directory. '
                                  'Defaults to the user home directory.'))
        args = vars(parser.parse_args(command_args))

        # If input is help, display help message
        if args['chunky-home-root'].strip().lower() == 'help':
            parser.print_help()
            sys.exit(0)

        # Default to environment var CHUNKY_HOME if set, otherwise user defined location
        make_chunky_home(args['chunky-home-root'] or os.environ.get('CHUNKY_HOME') or os.path.expanduser('~'))
