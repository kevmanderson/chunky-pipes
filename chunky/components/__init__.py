import subprocess
import time
import json
import sys

EXIT_ERROR = 1


class Software:
    def __init__(self, software_name, software_path):
        self.software_name = software_name
        self.software_path = software_path

    def run(self, *args):
        run_cmd = self.__generate_cmd(*args)
        print(' '.join(['>', time.strftime('%d %b %Y %H:%M:%S'), 'Running', self.software_name]))
        print(run_cmd)
        subprocess.Popen(run_cmd, shell=True, executable='/bin/bash').wait()

    def cmd(self, *args):
        return self.__generate_cmd(*args)

    def __generate_cmd(self, *args):
        return '{software_path} {parameters}'.format(
            software_path=self.software_path,
            parameters=' '.join([str(p) for p in args])
        )


class Parameter(object):
    def __init__(self, *args):
        self.parameter = ' '.join(args)

    def __str__(self):
        return self.parameter


class Redirect(object):
    def __init__(self, type='>', dest='out.txt'):
        self.type = type
        self.dest = dest

    def __str__(self):
        return ''.join([self.type, self.dest])


class Pipe(object):
    def __init__(self, piped_cmd):
        self.piped_cmd = '| ' + piped_cmd

    def __str__(self):
        return self.piped_cmd


class BasePipeline(object):
    pipeline_args = None
    pipeline_config = None

    def description(self):
        return ''

    def add_pipeline_args(self, parser):
        return parser

    def parse_config(self):
        try:
            with open(self.pipeline_args['config']) as config:
                self.pipeline_config = json.loads(config.read())
        except IOError:
            sys.stdout.write('Fatal Error: Config file at {} does not exist.\n'.format(
                self.pipeline_args['config']
            ))
            sys.stdout.write('A config file location can be specified with the --config option.\n')
            sys.exit(EXIT_ERROR)
        except ValueError:
            sys.stdout.write('Fatal Error: Config file at {} is not in JSON format.\n'.format(
                self.pipeline_args['config']
            ))
            sys.exit(EXIT_ERROR)

    def configure(self):
        return {}

    def run_pipeline(self, pipeline_args, pipeline_config):
        pass
