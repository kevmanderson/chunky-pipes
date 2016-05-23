import os


class BaseCommand(object):
    chunky_home = (os.path.expanduser('~')
                   if 'CHUNKY_HOME' not in os.environ
                   else os.environ['CHUNKY_HOME'])
    home_pipelines = os.path.join(chunky_home, '.chunky', 'pipelines')
    home_configs = os.path.join(chunky_home, '.chunky', 'configs')

    def help_text(self):
        return ''

    def run(self, command_args):
        return NotImplementedError

