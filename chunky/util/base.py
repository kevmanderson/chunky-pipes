import os


class BaseCommand(object):
    argv = None
    options = {}
    user_home = os.path.expanduser('~')
    home_pipelines = os.path.join(user_home, '.chunky', 'pipelines')
    home_configs = os.path.join(user_home, '.chunky', 'configs')

    def run(self):
        pass

    def usage(self):
        return 'default usage'

    def help_text(self):
        return 'default print help'

    def parse_options(self):
        pass

    def run_from_argv(self, argv=None):
        if argv:
            self.argv = argv
        self.run()
