import os
import sys
from chunkypipes.util.base import BaseCommand

BASENAME = 0
EXTENTION = 1


class Command(BaseCommand):

    def usage(self):
        return 'Usage: chunky list'

    def help_text(self):
        help_msg = 'Lists installed pipelines'
        return '\n'.join([self.usage(), help_msg])

    def run(self):
        sys.stdout.write('Installed pipelines (in {}):\n\n'.format(self.home_pipelines))

        # Grab the installed files from both directories
        installed_pipelines = {os.path.splitext(pipeline)[BASENAME] for pipeline
                               in os.listdir(self.home_pipelines)
                               if pipeline != '__init__.py'}

        installed_configs = [config for config in os.listdir(self.home_configs)]

        for pipeline_name in installed_pipelines:
            if '{}.json'.format(pipeline_name) in installed_configs:
                print '{} is configured'.format(pipeline_name)
            else:
                print '{} is not configured'.format(pipeline_name)

        # return
        #
        #
        # all_pipelines = [os.path.basename(pipeline) for pipeline
        #                  in os.listdir(self.home_pipelines)
        #                  if os.path.splitext(pipeline)[EXTENTION] != '.pyc']
        # if '__init__.py' in all_pipelines:
        #     all_pipelines.remove('__init__.py')
        # print all_pipelines
        # return
        # pipeline_configuration = {}  # Dictionary for the pipelines
        # j = ''  # variable to keep out duplicates
        #
        # # sort to avoid putting duplicates into dictionary
        # all_pipelines.sort()
        #
        # # Put all pipelines in the library
        # for i in all_pipelines:
        #     if j.split('.')[0] != i.split('.')[0]:  # if the previous pipeline has the same name, do not add
        #         pipeline_configuration[i.split('.')[0]] = 'NOT configured'
        #     j = i
        #
        # # Set the pipelines in the configured folder to configured
        # for pipeline in configured_pipelines:
        #     pipeline_configuration[pipeline.split('.')[0]] = 'configured'
        # # print the pipelines
        # for pipeline, configuration in pipeline_configuration.iteritems():
        #     sys.stdout.write('{} is {}\n'.format(pipeline, configuration))