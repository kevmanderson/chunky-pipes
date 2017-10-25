from setuptools import setup, find_packages

import chunkypipes

setup(
    name='ChunkyPipes',
    version=chunkypipes.__version__,
    description='Pipeline design and distribution framework',
    license='MIT',
    author='Dominic Fitzgerald',
    author_email='dominicfitzgerald11@gmail.com',
    url='https://github.com/djf604/chunky-pipes',
    download_url='https://github.com/djf604/chunky-pipes/tarball/{}'.format(chunkypipes.__version__),
    packages=find_packages(),
    install_requires=['pathos>=0.2.1', 'six'],
    entry_points={
        'console_scripts': ['chunky = chunkypipes.util:execute_from_command_line']
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
        'Topic :: Software Development :: Libraries',
        'License :: OSI Approved :: MIT License'
    ]
)
