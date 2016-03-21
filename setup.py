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
