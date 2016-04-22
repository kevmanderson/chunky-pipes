Getting Started
===============

To install with pip:
::

    $ pip install chunkypipes

Before ChunkyPipes can function, it needs to be initialized with a call to ``chunky init``::

    $ chunky init
    > ChunkyPipes successfully initialized at /home/user

To install a pipeline, point ChunkyPipes to the python source file::

    $ chunky install /path/to/pipeline.py
    > Pipeline pipeline.py successfully installed

To configure a pipeline to run on the current platform, execute the configuration subcommand::

    $ chunky configure pipeline

To run the pipeline, execute the run subcommand::

    $ chunky run pipeline [options]

