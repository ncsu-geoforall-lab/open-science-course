GRASS GIS
=========

GRASS GIS is a free and open source desktop geographic system
and geospatial analytics library which serves as a platform for
open science. It is licensed under GNU GPL.

Official website and download: https://grass.osgeo.org

GRASS GIS and repeating what you did
------------------------------------

Reviewing history
`````````````````

See the file where the history is saved::

    echo $HISTFILE

Review the history::

    less $HISTFILE

Make a backup of the currently used history file::

    cp $HISTFILE workflow.txt

Store the unsaved history to the file::

    history -a

Data provenance
```````````````

Basic raster map matedata with command used to create the map::

    r.info elevation

The provenance information by itself::

    r.info -h elevation

The provenance of a vector map (series of commands and
additional information)::

    v.info -h lakes


Examples of how GRASS GIS is used to publish research
-----------------------------------------------------

Here is couple of examples of how GRASS GIS was used to publish
and disseminate research.

FUTURES
```````

FUTURES urban model currently being developed at NCSU as GRASS GIS module.

* https://grasswiki.osgeo.org/wiki/FUTURES_tutorial
* https://grass.osgeo.org/grass7/manuals/addons/r.futures.html

Temporal framework
``````````````````

Temporal framework for managing and analyzing time series developed
by Soeren Gebbert an a part of GRASS GIS.

* https://grasswiki.osgeo.org/wiki/Temporal_data_processing

Resources
---------

* `From GRASS GIS novice to power user <https://grasswiki.osgeo.org/wiki/From_GRASS_GIS_novice_to_power_user_(workshop_at_FOSS4G_Boston_2017)>`_ (workshop material for FOSS4G Boston 2017)
* `Unleash the power of GRASS GIS at US-IALE 2017 <https://grasswiki.osgeo.org/wiki/Unleash_the_power_of_GRASS_GIS_at_US-IALE_2017>`_ (contains interfacing with R)
* `Introduction to GRASS GIS: Network analysis using four interfaces <http://ncsu-geoforall-lab.github.io/grass-intro-workshop/network.html>`_ [primary resource]
* `GRASS GIS assignments for NCSU GIS/MEA582 <http://ncsu-geoforall-lab.github.io/geospatial-modeling-course/grass/>`_
* `General explanation of GRASS GIS module dialogs <https://grass.osgeo.org/grass72/manuals/wxGUI.modules.html>`_ [primary resource]

Videos
``````

* `Getting started with GRASS GIS GUI <https://www.youtube.com/watch?v=9fcBvYetIsM>`_
* `Introduction to GRASS GIS with network analysis <https://www.youtube.com/watch?v=VKaASntBq8U>`_ (Geospatial Studio at NCSU, September 2016) [primary resource]
* `Scripting GRASS GIS 7 with Python <https://www.youtube.com/watch?v=PX2UpMhp2hc>`_
* `GRASS GIS A Point Cloud (LiDAR) Evaluation Resource <https://www.youtube.com/watch?v=Fj0TO4ZKEc0>`_
* `33 Years Of GRASS GIS As An Innovation Platform <https://www.youtube.com/watch?v=Vv5NnPg6MOY>`_ at NCGIS 2017 [primary resource]
* `GRASS 7.2 and QGIS 2.15 Tutorials <https://www.youtube.com/watch?v=t44_h4cA7GQ&list=PLSCH2IXZ2pHqkSs9H19xhbW2MyxWC2F2h&index=1>`_ (YouTube playlist of videos by Isaac Ullah)

Papers
``````

* Rocchini, D., Petras, V., Petrasova, A., Horning, N., Furtkevicova, L., Neteler, M., Leutner, B., Wegmann, M. 2017, Open data and open source for remote sensing training in ecology. Ecological Informatics, `DOI: 10.1016/j.ecoinf.2017.05.004 <http://dx.doi.org/10.1016/j.ecoinf.2017.05.004>`_
* Mitasova, H and Neteler, M, 2004, GRASS as Open Source - Free Software GIS: accomplishments and perspectives. Transactions in GIS 8(2), 145-154
* Neteler, Markus, M. H. Bowman, Martin Landa, and Markus Metz. “GRASS GIS: A Multi-Purpose Open Source GIS.” Environmental Modelling & Software 31, 2012: 124–130.

Books
`````

* Neteler, M. and Mitasova, H., 2008, Open source GIS: A GRASS GIS Approach, Third edition, Springer, New York, 406p
* Hardin, E., Mitasova, H., Tateosian, L., Overton, M., 2014, GIS-based Analysis of Coastal Lidar Time-Series, Springer Briefs in Computer Science, Springer, New York, 84 p.
* Petrasova, A., Harmon, B., Petras, V., Mitasova, H., 2015, Tangible Modeling with Open Source GIS, Springer International Publishing, 135 p. eBook ISBN: 978-3-319-25775-4, Hardcover ISBN: 978-3-319-25773-0, DOI: 10.1007/978-3-319-25775-4


Assignment
----------

Try to reproduce the following paper and let us know how far did you get:

* https://opengeospatialdata.springeropen.com/articles/10.1186/s40965-017-0019-2
