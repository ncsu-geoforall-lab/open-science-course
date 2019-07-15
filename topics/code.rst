Publishing code as part of an open source project
=================================================

There is several ways how to publish code:

* Modifying a project by changing its source code
  * A change integrating or modifying a piece of code
  * Using an internal extension mechanism
  * Creating a new project which is a modification of the original one (fork)

* Extending a project by publishing an extension (addon, plugin, package)
  * In an official place (repository)
  * In an unofficial place (repository)

* Creating an a new project
  * Using minimal dependencies (e.g. C or Python)
  * Leveraging existing projects (e.g. QGIS, GRASS GIS)

We will focus on ways which are using existing projects as a dependency
providing basic functionality and as a place (channel) for publishing.

First, view the `How Open Source Geospatial Development Works`_ lecture.

Examples
--------

Implementation included in the project
``````````````````````````````````````

Authors of the following paper wrote the code as a GRASS GIS module
and included (or asked for inclusion of) the module into GRASS GIS
(no the module is part of GRASS GIS).

Brovelli, Maria A., Massimiliano Cannata, and Ulisse M. Longoni.
"LIDAR data filtering and DTM interpolation within GRASS."
Transactions in GIS 8.2 (2004): 155-174.
https://doi.org/10.1111/j.1467-9671.2004.00173.x

https://grass.osgeo.org/grass76/manuals/v.surf.bspline.html

Extension in an official repository
```````````````````````````````````

Authors of the following paper wrote the code as a GRASS GIS module
and put the module into the official GRASS GIS Addons repository.

Beaumont, B., Grippa, T., Lennert, M., Vanhuysse, S., Stephenne, N., and Wolff, E.
"Toward an operational framework for
fine-scale urban land-cover mapping in Wallonia using submeter remote
sensing and ancillary vector data." Journal of Applied Remote
Sensing 11.3 (2017): 036011.
https://doi.org/10.3390/rs9040358

https://grass.osgeo.org/grass7/manuals/addons/r.object.geometry.html

Independent extension of the project
````````````````````````````````````

Authors of the following paper wrote the code as a GRASS GIS module
and published the code on GitHub. (Later, they put it also to the
official GRASS GIS Addons repository.)

Petrasova, A., Mitasova, H., Petras, V., and Jeziorska, J.
"Fusion of high-resolution DEMs for water
flow modeling." Open Geospatial Data, Software and Standards 2.1
(2017): 6.
https://doi.org/10.1186/s40965-017-0019-2

https://github.com/petrasovaa/r.patch.smooth

Independent project using an existing project
````````````````````````````````````````````````

Authors of the following paper present their code as a standalone
project called RHESSys. From point of view of this project,
GRASS GIS is a dependency. At the same time, significant part of the
code is implemented as a GRASS GIS modules.

Tague, C. L., and L. E. Band. "RHESSys: Regional Hydro-Ecologic
Simulation System—An object-oriented approach to spatially distributed
modeling of carbon, water, and nutrient cycling."
Earth Interactions 8.19 (2004): 1-42.
https://doi.org/10.1175/1087-3562(2004)8%3C1:RRHSSO%3E2.0.CO;2

https://github.com/RHESSys/RHESSys


GRASS GIS
---------

GRASS GIS is a free and open source desktop geographic system
and geospatial analytics library which serves as a platform for
open science. It is licensed under GNU GPL.

Official website and download: https://grass.osgeo.org

Official instructions for contributing and publishing code through
the project:

https://grass.osgeo.org/development/code-submission/

Example of a GRASS GIS module implemented in Python (see the source
code link at the bottom of the page):

https://grass.osgeo.org/grass7/manuals/addons/r.bioclim.html

To get an idea about how one can write a custom module for GRASS GIS,
see this tutorial_ about creating addons for GRASS GIS.

.. _tutorial: code-for-grass.html

Resources
---------

Videos
``````

* `How Open Source Geospatial Development Works <https://youtu.be/ENn9vTdtpko>`_
  (`alternative video page <https://cnr.online.ncsu.edu/online/Catalog/catalogs/geospatial-forum>`_) [main resource]
* `World Without Linux Final Episode #6 Free Burger <https://www.youtube.com/watch?v=fvPSNK8iB0Y>`_ (2.5 min, content applies to most open source software)
* `Scripting GRASS GIS 7 with Python <https://www.youtube.com/watch?v=PX2UpMhp2hc>`_

Slides
``````

* `How Open Source Geospatial Development Works (slides) <http://wenzeslaus.github.io/presentations/geoforum2014-foss.pdf>`_
* `Additional lecture slides <../lectures/open-source.html>`_
* `Introduction to Open Source for Geospatial Analysis and Modeling <http://ncsu-geoforall-lab.github.io/foss-for-geospatial-analysis/intro-to-foss.html>`_


Texts
`````

* `What is open source? <https://opensource.com/resources/what-open-source>`_ (opensource.com)
* `If you were on a desert island, which license would you take with you? <https://opensource.com/article/17/7/what-open-license-would-i-choose-desert-island>`_ (opensource.com)
* `How to write a Python GRASS GIS 7 addon <https://github.com/wenzeslaus/python-grass-addon>`_

Websites
````````

* `opensource.com <https://opensource.com>`_ (articles, use cases, and FAQs)


Assignment
----------

Mandatory part
``````````````

Pick an open source project you are using or considering to use.
Search on the Internet or in the installation of the software
(GUI, CLI, documentation) for information related to use of the project,
its community, and development. Find what is the project license,
whether the license is approved by OSI or FSF, which type of license
it is (short, long, permissive, copyleft, ...), how to report bugs and
request new features in the project,
how to ask questions about using the project, how to contact developers,
who provides commercial support, how to get latest source code,
where to view the code online,
where to get information about contributing to the project
what would you have to do in oder to contribute some of your work to the
project or as a project extension,
whether the project is active,
and anything else what you think is important.

Please, don't do this for GRASS GIS since it is in the lecture
presentation. Don't worry about somebody else picking
the same project as long as you work on your answer without consulting
their work.

To practice Git, create a repository on GitHub or other service and
put the answers there in a text file formated using Markdown or other
lightweight markup. You can use Git and text editor on your computer,
GitHub web interface, or any other tool to work on the text file
and work with Git. Sent the link to it to message board.

Optional part
`````````````

Take some geospatial procedure you performed and write it as a GRASS GIS
Python module, i.e. Python script including interface description,
documentation and a (trivial) Makefile. Publish this using GitHub or
other service (we would use an official GRASS GIS Addons repository
in a real case). Then try to install it from that source locally
(currently, you need to use Linux or Mac OS to do that, use NCSU VCL if
needed).

If you don't have a good procedure you want to script, you can implement
some trivial process.
