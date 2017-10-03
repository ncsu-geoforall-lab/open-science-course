Command line and Python tools for geospatial work
=================================================

This topic is focused on processing geospatial data in command line.
Specifically, we will use GDAL and unix-like command line.
For Python, we will use IPython as the interpreter.
All the tools we will use are open source under various licenses.
With many tools, you can use parameters ``--version``, ``--help``,
or ``--license`` or run *man* to find out what is the specific license.

GDAL
----

GDAL is a free and open source project under MIT license.
GDAL has CLI and and also C and Python APIs and is used broadly by other
software as a backend especially for format transformations.
GDAL is an OSGeo project.

Preparation
```````````

Install GDAL (command for Ubuntu)::

    sudo apt install gdal-bin

Install additional programs (all at once)::

    sudo apt install python-gdal ipython imagemagick

Download data::

    wget https://www.grassbook.org/wp-content/uploads/data_extra/o35078g6_NC.tif.gz

Unpack (GZIP format)::

    gunzip o35078g6_NC.tif.gz

Basics
``````

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

Rasterization
`````````````

Rasterize the vector::

    gdal_rasterize -burn 100 -te 610760 196084 677119 258303 -tr 100 100 -l lakes ncshape/lakes.shp lakes.tif

Convert TIFF to PNG for visualization using ImageMagick)::

    convert lakes.tif lakes.png

Show PNG using Eye of GNOME::

    eog lakes.png

Processing textual outputs
``````````````````````````

In the previous example, we needed the extent of the vector and we
manually transfered the values. That would not be feasible if we
would need to do it repetitively or in a reproducible way.
Any textual output of a command (standard output), can be easily
processed in the command line. Sometimes we have to be careful on how
likely is the format to change in the future, but for now, we can
consider the *ogrinfo* output to be stable enough.

We start with extracting just the line we are interested in using
the *grep* command::

    ogrinfo -so ncshape/lakes.shp lakes | grep Extent:

Now, we need only the numbers from this line. There is couple of
different ways how to do it, like using *sed*, *awk*. Here, we will use
Python, and although regular expressions are a powerful tool we could
use, it will enough to just use *replace* function. We will use
packaged called *fileinput* which takes care of reading from the
standard input (and files if needed). Create a file
called ``filter_numbers.py`` and use the following content:

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

Now use the Python script file in the command::

    ogrinfo -so ncshape/lakes.shp lakes | grep Extent: | python filter_numbers.py

In unix-like systems, we can make any file executable when it makes
sense, so we will do it also with our script. It is done using the
*chmod* command with parameter ``u+x`` which adds (``+``) executable
permissions (``x``) to the user who is the file owner (``u``)::

    chmod u+x filter_numbers.py

Now we can use the script without specifying Python as the interpreter
because that will be taken from the first line of the script which
starts with ``#!``. This line is called *shebang*.
However, we need to be explicit about the script being a file by
adding ``./`` when it is in the current directory to distinguish it
from other commands (for safety and organization purposes)::

    ogrinfo -so ncshape/lakes.shp lakes | grep Extent: | ./filter_numbers.py

At this point we have the numbers separated by spaces and we can get
back to the *gdal_rasterize* command. We need to include these numbers
are part of the *gdal_rasterize* command. This can be done using
``$()`` which is for command substitution which places standard output
of one command into the given context, in our case command line
parameters of *gdal_rasterize*. See the final command and notice also
the slashes at the end of the first two lines which are telling the
interpreter that the command continues on the following line::

    gdal_rasterize -burn 100 \
        -te $(ogrinfo -so ncshape/lakes.shp lakes | grep Extent: | python filter_numbers.py) \
        -tr 100 100 -l lakes ncshape/lakes.shp lakes.tif

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

It is worth noting that the subcommand syntax above (``$()``) can be
used also in this context::

    for NUM in $(seq -w 50 50 300)
    do
        echo $NUM
    done
