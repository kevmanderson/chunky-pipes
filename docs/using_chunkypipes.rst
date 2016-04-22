Using ChunkyPipes
=================

ChunkyPipes is designed to make running pipelines as painless as possible.

Initializing ChunkyPipes
^^^^^^^^^^^^^^^^^^^^^^^^
Although ChunkyPipes can run without initializing a hidden directory, doing so makes using ChunkyPipes and running
pipelines much easier and more organized.
::

    $ chunky init

If no argument is provided, ChunkyPipes intializes a hidden directory in the home directory. This is also where
ChunkyPipes looks by default to install, configure, and run pipelines. If the user wishes to initialize a hidden
directory at a location other than the home directory, a path argument may be specified. To change where
ChunkyPipes looks when operating, introduce a ``CHUNKY_HOME`` environment variable and point it to the hidden
directory.
::

    $ chunky init /path/to/other/place
    > Please set a CHUNKY_HOME environment variable to /path/to/other/place
    $ export CHUNKY_HOME=/path/to/other/place

.. note::
   The above ``export`` statement will only persist for the life of the terminal session. To introduce a ``CHUNKY_HOME``
   environment variable permanently, add the export statement to ``~/.bashrc`` or the platform equivalent.

Installing Pipelines
^^^^^^^^^^^^^^^^^^^^
To install pipelines into ChunkyPipes::

   $ chunky install /path/to/fun-pipeline.py

This will install the pipeline into the ChunkyPipes hidden directory, whether that be the default home directory or
the directory pointed to by ``CHUNKY_HOME``.

To show a list of installed pipelines::

   $ chunky list

This list also shows which pipelines have corresponding configuration files.

Configuring Pipelines
^^^^^^^^^^^^^^^^^^^^^
To configure a pipeline::

   $ chunky configure fun-pipeline

ChunkyPipes will present an interactive configuration, asking the user for anything required by the pipeline.
::

   $ chunky configure fun-pipeline
   > Full path to software1: (User enters) /path/to/soft1
   > Provide a value for arg1: (User enters) 45
   > Full path to software2: (User enters) /path/to/soft2

If no ``--location`` parameter is given, the configuration file is
stored in the ChunkyPipes hidden directory as a JSON formatted file with the same base
filename as the pipeline. If the user doesn't provide a ``--config`` parameter to the pipeline, ChunkyPipes uses the
config file in the hidden directory.

As of version 0.2.0, ChunkyPipes interactive configuration supports TAB-completion, but not left-and-right character
seeking.


Running Pipelines
^^^^^^^^^^^^^^^^^
To run a pipeline::

   $ chunky run <pipeline_name or path> [-h] [--config CONFIG] [pipeline_args]

The pipeline can be either the name of an installed pipeline or a path to a Python file containing a properly
formatted Pipeline class. If a name is given without a ``--config`` parameter, both components will come from the
ChunkyPipes hidden directory. If a path is given, ``--config`` must also be given a value.
