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
providing basic functionality and a place (channel) for publishing.

Examples
--------

Implementation included in the project
``````````````````````````````````````

Authors of the following paper wrote the code as a GRASS GIS module
and included (or asked for inclusion of) the module into GRASS GIS.

Brovelli, Maria A., Massimiliano Cannata, and Ulisse M. Longoni.
"LIDAR data filtering and DTM interpolation within GRASS."
Transactions in GIS 8.2 (2004): 155-174.
https://doi.org/10.1111/j.1467-9671.2004.00173.x

https://grass.osgeo.org/grass72/manuals/v.surf.bspline.html

Extension in an official repository
```````````````````````````````````

Authors of the following paper wrote the code as a GRASS GIS module
and put the module to the official GRASS GIS Addons repository.

Beaumont, B., Grippa, T., Lennert, M., Vanhuysse, S., Stephenne, N., and Wolff, E.
"Toward an operational framework for
fine-scale urban land-cover mapping in Wallonia using submeter remote
sensing and ancillary vector data." Journal of Applied Remote
Sensing 11.3 (2017): 036011.
https://doi.org/10.3390/rs9040358

https://grass.osgeo.org/grass72/manuals/addons/r.object.geometry.html

Independent extension of the project
````````````````````````````````````

Authors of the following paper wrote the code as a GRASS GIS module
and published the code on GitHub.

Petrasova, A., Mitasova, H., Petras, V., and Jeziorska, J.
"Fusion of high-resolution DEMs for water
flow modeling." Open Geospatial Data, Software and Standards 2.1
(2017): 6.
https://doi.org/10.1186/s40965-017-0019-2

https://github.com/petrasovaa/r.patch.smooth

Independent project using on an existing project
````````````````````````````````````````````````

Authors of the following paper present their code as a standalone
project called RHESSys. From point of view of this project,
GRASS GIS is a dependency. At the same time, significant part of the
code is implemented as GRASS GIS modules.

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

https://grass.osgeo.org/grass72/manuals/addons/r.bioclim.html

Third party tutorial for about creating addons for GRASS GIS:

https://github.com/wenzeslaus/python-grass-addon

Resources
---------

Texts
-----

* `How to write a Python GRASS GIS 7 addon  <https://github.com/wenzeslaus/python-grass-addon>`_

Videos
``````

* `Scripting GRASS GIS 7 with Python <https://www.youtube.com/watch?v=PX2UpMhp2hc>`_

Assignment
----------

Take some geospatial procedure you performed and write it as a GRASS GIS
Python module, i.e. Python script including interface description,
documentation and a (trivial) Makefile. Publish this using GitHub or
other service (we would use an official GRASS GIS Addons repository
in a real case). Then try to install it from that source locally
(currently, you need to use Linux or Mac OS to do that, use NCSU VCL if
needed).

If you don't have a good procedure you want to script, you can implement
some trivial process.
