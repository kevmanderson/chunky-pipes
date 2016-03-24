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


def add_common_pipeline_args(parser):
    parser.add_argument('--reads', required=True, action='append',
                        help=('Raw reads to process with this pipeline. Paired-end reads ' +
                              'can be joined together with a colon (:). Specify this option ' +
                              'multiple times to process multiple raw reads files.\nEx ' +
                              'paired-end: --reads read1.fastq:read2.fastq\nEx single-end: ' +
                              '--reads sample1.fastq sample1.extra.fastq'))
    parser.add_argument('--output', required=True,
                        help='Directory to store all results of this pipeline in.')
    parser.add_argument('--log')


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
