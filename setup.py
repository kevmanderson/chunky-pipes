import sys
import os
from setuptools import setup, find_packages

setup(
    name='Chunky',
    version='0.1.0',
    description='Pipeline design and distribution framework',
    author='Dominic Fitzgerald',
    author_email='dominicfitzgerald11@gmail.com',
    url='https://github.com/djf604/chunky',
    packages=find_packages(),
    entry_points={
        'console_scripts': ['chunky = chunky.util:execute_from_command_line']
    },
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Topic :: Scientific/Engineering',
        'Topic :: Scientific/Engineering :: Bio-Informatics',
        'Topic :: Software Development :: Libraries'
    ]
)

user_home = os.path.expanduser('~')
try:
    if not os.path.exists(os.path.join(user_home, '.chunky')):
        os.mkdir(os.path.join(user_home, '.chunky'))
    if not os.path.exists(os.path.join(user_home, '.chunky', 'pipelines')):
        os.mkdir(os.path.join(user_home, '.chunky', 'pipelines'))
    if not os.path.isfile(os.path.join(user_home, '.chunky', 'pipelines', '__init__.py')):
        os.mknod(os.path.join(user_home, '.chunky', 'pipelines', '__init__.py'), 0o644)
    if not os.path.exists(os.path.join(user_home, '.chunky', 'configs')):
        os.mkdir(os.path.join(user_home, '.chunky', 'configs'))
except OSError as e:
    sys.stderr.write('An error occured creating the Chunky hidden filesystem.\n{}\n'.format(e.message))
