Command line and Python tools for geospatial work
=================================================

This topic is focused on processing geospatial data in command line.
Specifically, we will use GDAL and unix-like command line.
For Python, we will use IPython as the interpreter.
All the tools we will use are open source under various licenses.
With many tools, you can use parameters ``--version``, ``--help``,
or ``--license`` or run *man* to find out what is the specific license.
However, all tools we will use are under licenses which fit
the Open Source Definition by the Open Source Initiative.

GDAL
----

GDAL is a free and open source project under MIT license.
GDAL has CLI and also C and Python APIs and is used broadly by other
software as a backend especially for format transformations.
GDAL is an OSGeo project.

https://gdal.org/

GDAL has a raster part and vector part. The vector part is sometimes
referred to as OGR and in that case GDAL is referred to as GDAL/OGR.
There is multiple interfaces and wrappers of GDAL, but here we will
focus mainly on command line where the raster commands start typically
with ``gdal`` and the vector ones with ``ogr``.

We will assume an Ubuntu machine in the following examples,
but please see installation instructions for your operating system.

Preparation
```````````

Install GDAL (command for Ubuntu)::

    sudo apt install gdal-bin

Install additional programs (all at once)::

    sudo apt install python-gdal ipython imagemagick

Download data::

    wget https://www.grassbook.org/wp-content/uploads/data_extra/o35078g6_NC.tif.gz

Uncompress (GZIP format)::

    gunzip o35078g6_NC.tif.gz

Basics
``````

Get info::

    gdalinfo o35078g6_NC.tif

The output is too long, let's get just first part::

    gdalinfo o35078g6_NC.tif | head

Let's get first 50 lines::

    gdalinfo o35078g6_NC.tif | head -n 50

Browse through all using *less* (use *Q* to exit)::

    gdalinfo o35078g6_NC.tif | less

See if there is some option for getting just the basic info
(use arrow keys or *Page Up* and *Page Down* to navigate, *Q* to exit)::

    man gdalinfo

There is couple of options which start with `-no` which will allow
us to print less information without additional command line tricks.
Let's disable printing color table and raster attribute table::

    gdalinfo -noct -norat o35078g6_NC.tif

Get more data::

    wget http://grass.osgeo.org/sampledata/north_carolina/nc_rast_geotiff.tar.gz
    wget http://grass.osgeo.org/sampledata/north_carolina/nc_shape.tar.gz

Unpack the data (TAR.GZ format)::

    tar xvf nc_rast_geotiff.tar.gz
    tar xvf nc_shape.tar.gz

Get info using *ogrinfo* with ``-so`` which is for printing only the
summary::

    ogrinfo -so ncshape/lakes.shp lakes

Note that we are specifying the file, a data source to be exact,
and a layer within that data source. Here it is file ``lakes.shp`` in
directory ``shape`` and layer ``lakes`` which is the base part of the
file name in this case since Shapefiles have only one layer in them.

Rasterization
`````````````

Rasterize the vector using *gdal_rasterize*. The ``-burn`` parameter
specifies what raster value we want to use for the vector features
(objects) and the ``-tr`` parameter specifies the resolution of
the resulting raster.

::

    gdal_rasterize -burn 100 -tr 100 100 -l lakes ncshape/lakes.shp lakes.tif

Convert TIFF to PNG for visualization using ImageMagick
command *convert*::

    convert lakes.tif lakes.png

Show PNG using Eye of GNOME (*eog*)::

    eog lakes.png

To preserve georeferencing, we can use *gdal_translate* to convert TIFF
to PNG::

    gdal_translate -of PNG -scale -co worldfile=yes lakes.tif lakes.png

To get basic information about a file program called *file* can be used.
We use it to confirm that the format translation preserved number of
pixels in the raster::

    file lakes.tif
    file lakes.png

Bash script with parameters
```````````````````````````

The above conversion, although basic, requires much longer command than
the one which used ImageMagic. Therefore, we will create a script to
wrap it and allow for simpler syntax when used in the command line.
Python would be unnecessarily complicated for this simple task, so we
will use Bash which is using the same syntax as the command line we are
using. We will name the file ``tif2png.sh``. Although there is a
potential for confusion, we don't have to worry if there is a command
of the same name because we will need to specify the path or ``./``
when calling the command and we also named the file with file extension
and that way, it will be clear what command is used. In the following
file content, notice the first line (shebang) and also the numbers one
and two preceded with a dollar sign. The dollar sign is used to access
value of variables and the special variables ``$1`` and ``$2``
are set to the first and second parameter in the command line.

::

    #!/bin/bash

    gdal_translate -of PNG -scale -co worldfile=yes $1 $2

To make the script executable, run the following *chmod* command
which adds the executable permissions::

    chmod u+x tif2png.sh

This script can be used in the following way::

    ./tif2png.sh lakes.tif lakes.png

The ``./`` part or whatever directory path the script is on is still
necessary because the script is not in the directory specified by the
``PATH`` variable, i.e. it is not on path. This is perfectly fine and
usually desired for scripts.


Resampling and animation
````````````````````````

The *gdalwarp* is a powerful tool for reprojection and other
transformations. We will use it for resampling into lower resolution
using ``average`` method::

    gdalwarp -tr 300 300 -r average -co "TFW=YES" -overwrite ncrast/elev_ned_30m.tif srtm_300.tif

Let's do it for couple more resolutions::

    gdalwarp -tr 200 200 -r average -co "TFW=YES" -overwrite ncrast/elev_ned_30m.tif srtm_200.tif
    gdalwarp -tr 100 100 -r average -co "TFW=YES" -overwrite ncrast/elev_ned_30m.tif srtm_100.tif
    gdalwarp -tr 50 50 -r average -co "TFW=YES" -overwrite ncrast/elev_ned_30m.tif srtm_050.tif

Using previously created script, convert the TIFFs to PNGs::

    ./tif2png.sh srtm_300.tif srtm_300.png
    ./tif2png.sh srtm_200.tif srtm_200.png
    ./tif2png.sh srtm_100.tif srtm_100.png
    ./tif2png.sh srtm_050.tif srtm_050.png

Using ImageMagic, we can add all to one animated GIF::

    convert -coalesce -delay 1/1 -resize 500x srtm_*.png srtm.gif

Point buffer in Python
``````````````````````

For Python, we will use interactive shell called IPython::

    ipython

GDAL (and OGR) functionality is part of the *osgeo* package::

    from osgeo import ogr

Creating a point::

    point = ogr.Geometry(ogr.wkbPoint25D)
    point.AddPoint(610920, 196552, 320)

Simple printing of a point object::

    print point

Point as GeoJSON string::

    point.ExportToJson()

Creating a buffer around a point::

    buffer = point.Buffer(200)

To write the GeoJSON to a file, open a file for writing (``'w'``)::

    buffer_file = open('buffer.json', 'w')

Write the GeoJSON string to the file::

    buffer_file.write(buffer.ExportToJson())

Close the file (so that all changes are written to the disk and the
system knows that we finished working with the file)::

    buffer_file.close()

Now it would be good to review content of that file. This can be easily
done in command line using tools such as *cat*, *less*, or *head*.
One of the advantages of IPython is that the command line tools are
actually available using an exclamation mark at the beginning of the
line like in the following example which shows the first 100 characters
from the file::

    !head -c 100 buffer.json

Resources
---------

Texts
`````

* `GDAL at Spatial Ecology <http://spatial-ecology.net/dokuwiki/doku.php?id=wiki:gdal>`_ (collection of tutorials)
* `pktools at Spatial Ecology <http://spatial-ecology.net/dokuwiki/doku.php?id=wiki:pk_tools>`_ (collection of tutorials)
* `Python GDAL/OGR Cookbook <https://pcjericks.github.io/py-gdalogr-cookbook/>`_

Videos
``````

* `An Introduction to GDAL <https://www.youtube.com/watch?v=N_dmiQI1s24>`_ by Robert Simmon (30 mins)
* `Simple raster manipulation using GDAL <https://www.youtube.com/watch?v=ap5Y-UcLDNA>`_ by Simon Marius Mudd (12 mins)
* `Pragmatic GDAL <https://www.youtube.com/watch?v=uM8RQIJmfOk>`_ by Rob Labs (8 mins)

Assignment
----------

Go through the above instructions and examples. For smooth experience,
it is recommended to use NCSU VCL Ubuntu machine, but testing GDAL
on your own computer is highly encouraged.

Then take the part which is resampling the rasters and creating and
animated GIF and create a Bash script which does this procedure without
repeating commands. If possible, include also download of the file and
its unpacking of needed so that your result can be reproduced on any
computer. Submit this file to Moodle.

You may find these two following things useful. For loop in Bash is::

    for FRUIT in apple orange banana
    do
        echo $FRUIT
    done

A sequence of numbers can be generated using *seq*::

    seq -w 50 50 300

Finally, you can include into you script a textual result of another
command using the subcommand syntax. The syntax is ``$(command here)``.
The textual output will be simply put into the place of ``$(...)``.
This can be used in the context of a for loop like this::

    for NUM in $(seq -w 50 50 300)
    do
        echo $NUM
    done
