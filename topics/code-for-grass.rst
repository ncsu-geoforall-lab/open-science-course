Publishing code as part of GRASS GIS
====================================

This guide counts on using Ubuntu, so please use NCSU VCL if you want
to or need to follow the guide closely. The guide requires GRASS GIS
version 7.2, so on Ubuntu 16.04, you need to install GRASS GIS from
UbuntuGIS PPA::

    sudo add-apt-repository ppa:ubuntugis/ubuntugis-unstable
    sudo apt-get update
    sudo apt-get upgrade
    sudo apt-get install grass grass-gui

Basic structure
---------------

A minimal GRASS GIS module written in Python needs to contain these
three following files:

* Python script
* HTML documentation
* Makefile

These files are placed into a directory which has the same name as the
module. In GRASS GIS Addons, this would be a subdirectory in the Addons
repository. In our case, this will be a name of the Git repository we
will use. In this example, we will create a module to add two maps
together using raster algebra operator plus. It is a module which
processes rasters and all these modules in GRASS GIS start with ``r.``.
So, we will name our module ``r.plus``. For your assignment, pick a name
which is appropriate for the processing you are doing.
Create a repository on GitHub or similar service and clone it.

Python script
-------------

The script is in Python, so we use ``.py`` as file extension and the
name of the module is *r.plus*, so the file name is ``r.plus.py``.

Python script starts with shebang, the first line we have already seen
in Bash scripts or Python scripts for unix-like system::

    #!/usr/bin/env python

This is followed by a block of Python comments (lines starting with
``#``) which provide basic information about the module.
The way it is formated is common for GRASS GIS, but other projects have
similar standards.

::

    ########################################################################
    #
    # MODULE:       r.plus
    # AUTHOR:       Ann Doe
    # PURPOSE:      Adds two rasters using raster algebra
    # COPYRIGHT:    (C) 2017 Ann Doe
    #               This program is free software under the GNU General
    #               Public License (>=v2). Read the file COPYING that
    #               comes with GRASS for details.
    #
    ########################################################################

The next part is again just a Python comment, but this time it is
formated in a very specific way and GRASS GIS reads this information
and uses that to build CLI, GUI, documentation and more.
The description of the syntax can be found on the manual page of the
`g.parse <https://grass.osgeo.org/grass72/manuals/g.parser.html>`_
module.

::

    #%module
    #% description: Adds the values of two rasters (A + B)
    #% keyword: raster
    #% keyword: algebra
    #% keyword: sum
    #%end
    #%option G_OPT_R_INPUT
    #% key: araster
    #% description: Name of input raster A in an expression A + B
    #%end
    #%option G_OPT_R_INPUT
    #% key: braster
    #% description: Name of input raster B in an expression A + B
    #%end
    #%option G_OPT_R_OUTPUT
    #%end

This description contains four blocks: one ``module``, and three
``option`` blocks. The ``module`` block contains a short ``description``
of the module and ``keyword``s (tags) which should help users to find
the module. Each ``option`` block defines type, name, and description
for each of the options (parameters). Here, all three are using
predefined options (called standard options) which provide default
values each of the entries. ``G_OPT_R_INPUT`` stands for
"raster input GRASS option", i.e. an parameter specifying a name of
a raster map which will be used as input. Here we have two inputs, so
we need to define our own name and description and that's done using
``key`` and ``description``.

Now the actual code follows, starting with imports::

    import sys

    import grass.script as gscript

The main part of the code is not on the top level (with no indentation),
but as part of a function which we named ``main``. In other words,
the code is after ``def main():`` and is indented. This is a best
practice used by many, if not all, projects in Python.

Here, the first part of the ``main()`` function code is reading what
was provided in the command line and storing it into Python variables.
The next part is the processing, here is it just one line calling
``mapcalc()`` function which in turn calls GRASS GIS module *r.mapcalc*,
the GRASS GIS module for raster algebra.
Finally, we use ``return 0`` which is in this context a way of saying
that everything went well.

::

    def main():
        options, flags = gscript.parser()
        araster = options['araster']
        braster = options['braster']
        output = options['output']

        gscript.mapcalc('{r} = {a} + {b}'.format(r=output, a=araster, b=braster))

        return 0

We end the script with ``if __name__ == "__main__":`` block which is a
top level code, i.e. not indented code. The ``if`` condition tells
Python to execute the code if the file is a used as a main file in
program execution which is the case for our script. Together with
``def main():`` this is a commonly used best practice. 

::

    if __name__ == "__main__":
        sys.exit(main())

This is file by itself will run when we execute it in GRASS GIS.
We can use GRASS GIS Simple Python Editor to do that, or we can use
command line::

    python r.plus.py

However, for scripts on unix-like systems, we set executable
permissions::

    chmod u+x r.plus.py

Then we can execute the script like this::

    ./r.plus.py

To increase chances our code is accepted by community, we should check
it against the GRASS GIS submitting guidelines for Python code:

https://trac.osgeo.org/grass/wiki/Submitting/Python

HTML documentation
------------------

A documentation of a module in GRASS GIS uses HTML as the markup
language, but the HTML code for the full web page is generated
automatically. We need to provide just basic sections::
description, see also, and author or authors. These sections are marked
as heading level 2, i.e. ``<h2>``.
The name of the file is the name of the module with the extension
``.html``, so ``r.plus.html`` in our case.

The description section should explain what the module does, how it does
it, and how to use it. Here we provide just an short oversimplified
description as a place holder::

    <h2>DESCRIPTION</h2>

    <em>r.plus</em> adds two rasters together using addition operator
    in raster algebra. The options are members of equation
    ``c = a + b``. All parameters are mandatory for obvious reasons.

Another required section is a see also section which contains links to
modules which are related to the new module. It can be modules which are
alternative, explain the same concept, are part of the same workflow,
or, as in our case, are used in the implementation.

::

    <h2>SEE ALSO</h2>

    <em><a href="r.mapcalc.html">r.mapcalc</a></em>

Finally we also include authors, this can be a simple list of names but
it can also include institutions, funding sources, or how individual
authors contributed to the code.

::

    <h2>AUTHOR</h2>

    Ann Doe

For more information, see the GRASS GIS submitting guidelines for
documentation:

https://trac.osgeo.org/grass/wiki/Submitting/Docs

Makefile
--------

A Makefile is a file which typically gives instructions how to compile
code (e.g. C or C++ code) into a executable (binary). Although Python
code does not have to compiled into binary, we are still using Makefile
because in this case, it does several important steps such as creating
the documentation and putting files into a right place in order to
run the module as part of GRASS GIS. Most of instructions how to do that
are part of GRASS GIS and our Makefile will just use those. Thus, our
Makefile is exactly the same as any other script except the name of the
module which we need to provide as a value of ``PGM`` variable.

::

    MODULE_TOPDIR = ../..

    PGM = r.plus

    include $(MODULE_TOPDIR)/include/Make/Script.make

    default: script

The Makefile is used by a tool called *make*. This tool needs to know
where to find the Makefiles which come with GRASS GIS. For that we need
use the ``MODULE_TOPDIR`` variable.

However, before that it is important to note that we need to have *make*
installed and we need GRASS GIS with these Makefiles. To achieve that on
Ubuntu, we need to install GRASS GIS development package which is called
``grass-dev``.

::

    sudo apt install grass-dev

Now we could run *make*, but since GRASS GIS 7.2 provides the same
functionality in a more convenient way, we will use that. We can run
*g.extension* module and point it to the directory with the module::

    g.extension extension=r.plus url=/your/directory/with/the/module

After this, when we are in GRASS GIS command line, we can run our
*r.plus* module in the same was as any other GRASS GIS module, i.e.
without ``./`` or ``python`` and with GUI if requested.

Obtain short help in command line::

    r.plus --help

Run the module without parameters (GUI should appear)::

    r.plus

Publishing and downloading
--------------------------

If we were putting to the module to GRASS GIS Addons, we would now check
the submitting guidelines, conditions for submitting code and gaining
access to the repository at an official page:

https://grass.osgeo.org/development/code-submission/

In our case, we are just publishing the code using GitHub, so we need
to add files to Git, commit, and push.

Now on another computer which currently also needs to be Linux (or
potentially Mac OS), we can test installing the module from GitHub::

    g.extension extension=r.plus url=github.com/anndoe/r.plus

Resources
---------

Texts
`````

* `How to write a Python GRASS GIS 7 addon  <https://github.com/wenzeslaus/python-grass-addon>`_
* `GRASS GIS Python scripting with script package <https://grass.osgeo.org/grass72/manuals/libpython/script_intro.html>`_ (official documentation)
* `Official instructions for code submission <https://grass.osgeo.org/development/code-submission/>`_
* `Example of a GRASS GIS module implemented in Python <https://grass.osgeo.org/grass72/manuals/addons/r.bioclim.html>`_ (see the source code link at the bottom of the page)
* `Introduction to GRASS GIS: Python scripting <http://ncsu-geoforall-lab.github.io/grass-intro-workshop/python.html>`_
* `Using Python and GRASS GIS <https://ncsu-geoforall-lab.github.io/uav-lidar-analytics-course/assignments/python.html>`_ (class material from GIS595/MEA792: UAV/lidar Data Analytics)

Videos
``````

* `Publishing code as a GRASS GIS module <http://fatra.cnr.ncsu.edu/open-science-course/code-as-grass-module.mp4>`_ (recording from the class, 1 hour)
* `Scripting GRASS GIS 7 with Python <https://www.youtube.com/watch?v=PX2UpMhp2hc>`_
