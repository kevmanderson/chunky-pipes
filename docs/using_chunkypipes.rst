Using ChunkyPipes
=================

ChunkyPipes is designed to make running pipelines as painless as possible.

Initializing ChunkyPipes
^^^^^^^^^^^^^^^^^^^^^^^^
Although ChunkyPipes can run without initializing a hidden directory, doing so makes using ChunkyPipes and running
pipelines much easier and more organized. By keeping pipeline files and various configurations in an internal
hidden directory structure, ChunkyPipes abstracts out filepath details involved in running pipelines.
::

    $ chunky init

If no argument is provided, ChunkyPipes intializes a hidden directory in the home directory. This is also where
ChunkyPipes looks by default to install, configure, and run pipelines. If the user wishes to initialize a hidden
directory at a location other than the home directory, a path argument may be specified. To change where
ChunkyPipes looks when operating, introduce a ``CHUNKY_HOME`` environment variable and point it to the
directory containing the ChunkyPipes hidden directory.
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

   $ chunky install /path/to/ngs-pipeline.py

This will install the pipeline into the ChunkyPipes hidden directory, whether that be the default home directory or
the directory pointed to by ``CHUNKY_HOME``.

If the pipeline requires any Python package dependencies, ``chunky install`` will prompt the user to install these
dependencies via pip. Though this step is optional, it's likely that the installed pipeline won't run without the
declared dependencies.

.. warning::
   ``chunky install`` will feed the developer-provided package name and version directly to pip using the ``--upgrade``
   option. The exact version specified will be installed, even if it's an older version than a package that's currently
   installed. If this behavior isn't desired, the user can pick and choose dependencies to install by running
   ``chunky show`` on the pipeline to get all dependencies and installing those desired.

.. note::
   If the user is not in a virtual environment at the time ``chunky install`` is run, ``sudo`` or the platform
   equivalent may need to be prepended to the command in order to install Python packages into system files.

To show a list of installed pipelines::

   $ chunky list

This list also shows which pipelines have corresponding configuration files.

Configuring Pipelines
^^^^^^^^^^^^^^^^^^^^^
To configure a pipeline::

   $ chunky configure <pipeline-name>

ChunkyPipes will present an interactive configuration, asking the user for any platform-specific information \
required by the pipeline.
::

   $ chunky configure ngs-pipeline
   > Full path to software1: (User enters) /path/to/soft1
   > Provide a value for arg1: (User enters) 45
   > Full path to software2: (User enters) /path/to/soft2

If no ``--location`` parameter is given, the configuration file is
stored in the ChunkyPipes hidden directory as a JSON formatted file with the same base
filename as the pipeline. If the user doesn't provide a ``--config`` parameter when running a pipeline, ChunkyPipes
uses the config file in the hidden directory.

As of version 0.2.0, ChunkyPipes interactive configuration supports TAB-completion for filesystem paths, but not
left-and-right character seeking.

Showing Pipelines
^^^^^^^^^^^^^^^^^
To show information about a pipeline::

   $ chunky show <pipeline-name>

This command will show the pipeline description, arguments, dependencies, configuration dictionary, and the current
default configuration, if it exists.

Running Pipelines
^^^^^^^^^^^^^^^^^
To run a pipeline::

   $ chunky run <pipeline-name or path> [-h] [--config CONFIG] [pipeline_args]

The pipeline can be either the name of an installed pipeline or a path to a Python file containing a properly
formatted Pipeline class. If an installed pipeline name is given without a ``--config`` parameter,
both components will come from the
ChunkyPipes hidden directory. If a path is given, ``--config`` must also be given a value.
