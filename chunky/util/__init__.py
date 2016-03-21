import sys
from importlib import import_module


def fetch_command_class(subcommand):
    module = import_module('chunky.util.commands.{}'.format(subcommand))
    return module.Command()


def print_help_text():
    fetch_command_class('help').run_from_argv()


def print_unrecognized_command(subcommand):
    sys.stdout.write('Unrecognized command: {}\n\n'.format(subcommand))
    sys.stdout.write('Use one of the following:\n')
    print_help_text()


def execute_from_command_line(argv=None):
    argv = argv or sys.argv[:]
    try:
        subcommand = argv[1]
    except IndexError:
        print_help_text()
        sys.exit(0)

    send_argv = []
    if len(argv) > 2:
        send_argv = argv[2:]

    try:
        fetch_command_class(subcommand).run_from_argv(send_argv)
    except ImportError:
        print_unrecognized_command(subcommand)
