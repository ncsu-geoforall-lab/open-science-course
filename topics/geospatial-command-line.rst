Command line and Python tools for geospatial work
=================================================

Install::

    sudo apt install gdal-bin
    sudo apt install python-gdal ipython imagemagick

Download data::

    wget https://www.grassbook.org/wp-content/uploads/data_extra/o35078g6_NC.tif.gz

Unpack (GZIP format)::

    gunzip o35078g6_NC.tif.gz

Get info::

    gdalinfo o35078g6_NC.tif

Get just first part::

    gdalinfo o35078g6_NC.tif | head

Get little more::

    gdalinfo o35078g6_NC.tif | head -n 50

Browser through all::

    gdalinfo o35078g6_NC.tif | less

See if there is some option for getting just the basic info::

    man gdalinfo

Disable printing color table and raster attribute table::

    gdalinfo -noct -norat o35078g6_NC.tif

Get more data::

    wget http://grass.osgeo.org/sampledata/north_carolina/nc_rast_geotiff.tar.gz
    wget http://grass.osgeo.org/sampledata/north_carolina/nc_shape.tar.gz

Unpack the data (TAR.GZ format)::

    tar xvf nc_rast_geotiff.tar.gz
    tar xvf nc_shape.tar.gz

Get info::

    ogrinfo -so ncshape/lakes.shp lakes

Rasterize the vector::

    gdal_rasterize -burn 100 -te 610760 196084 677119 258303 -tr 100 100 -l lakes ncshape/lakes.shp lakes.tif

Convert TIFF to PNG for visualization using ImageMagick)::

    convert lakes.tif lakes.png

Show PNG using Eye of GNOME::

    eog lakes.png

::

    ogrinfo -so ncshape/lakes.shp lakes | grep Extent:

filter_numbers.py

::

    #!/usr/bin/env python

    import fileinput

    for line in fileinput.input():
        print(line
              .replace("Extent: ", "")
              .replace("(", "")
              .replace(")", "")
              .replace(",", "")
              .replace("- ", "")
              )

::

    ogrinfo -so ncshape/lakes.shp lakes | grep Extent: | python filter_numbers.py

::

    chmod u+x filter_numbers.py

::

    ogrinfo -so ncshape/lakes.shp lakes | grep Extent: | ./filter_numbers.py

::

    gdal_rasterize -burn 100 \
        -te $(ogrinfo -so ncshape/lakes.shp lakes | grep Extent: | python filter_numbers.py) \
        -tr 100 100 -l lakes ncshape/lakes.shp lakes.tif

::

    gdal_translate -of PNG -scale -co worldfile=yes ncrast/elev_ned_30m.tif ned.png

::

    file ncrast/elev_ned_30m.tif
    file ned.png

tif2png.sh::

    #!/bin/bash

    gdal_translate -of PNG -scale -co worldfile=yes $1 $2

::

    gdalwarp -tr 300 300 -r cubic -co "TFW=YES" -overwrite ncrast/elev_ned_30m.tif srtm_300.tif

::

    convert srtm_*.png -resize 500x -delay 100 srtm.gif

Resources
---------

Texts
`````

* `GDAL at Spatial Ecology <http://spatial-ecology.net/dokuwiki/doku.php?id=wiki:gdal>`_ (collection of tutorials)
* `pktools at Spatial Ecology <http://spatial-ecology.net/dokuwiki/doku.php?id=wiki:pk_tools>`_ (collection of tutorials)
* `Python GDAL/OGR Cookbook <https://pcjericks.github.io/py-gdalogr-cookbook/>`_

Videos
``````

Assignment
----------
