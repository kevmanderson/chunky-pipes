import subprocess
import time


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
    def add_pipeline_args(self, parser):
        return parser

    def configure(self):
        pass

    def run_pipeline(self, pipeline_args):
        pass
