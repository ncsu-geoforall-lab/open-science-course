Publishing data on web
======================

To publish scientific data online, we have several choices based on
the discipline and type of data. The resources section lists several
repositories which are either general or with some geospatial focus.
For the practical part, we will try an absolutely general method which
does not use a centralized scientific repository, but which is
applicable also for non-scientific geospatial data.

Custom web page with geospatial data
------------------------------------

Preparation
```````````

Install GDAL (command for Ubuntu)::

    sudo apt install gdal-bin

Get data and upack them::

    wget http://grass.osgeo.org/sampledata/north_carolina/nc_rast_geotiff.tar.gz
    wget http://grass.osgeo.org/sampledata/north_carolina/nc_shape.tar.gz
    tar xvf nc_rast_geotiff.tar.gz
    tar xvf nc_shape.tar.gz

Covert Shapefile to GeoJSON::

    ogr2ogr -f GeoJSON -t_srs crs:84 nc_state.geojson ncshape/nc_state.shp

Web page
````````

Now create a file in a text editor with the following HTML code,
name the file ``index.html`` and open this file in a web browser::

    <!DOCTYPE html>
    <html>
      <head>
        <title>OpenLayers simple raster and vector</title>
        <link rel="stylesheet" href="https://openlayers.org/en/v4.3.4/css/ol.css" type="text/css">
        <!-- The line below is only needed for old environments like Internet Explorer and Android 4.x -->
        <script src="https://cdn.polyfill.io/v2/polyfill.min.js?features=requestAnimationFrame,Element.prototype.classList,URL"></script>
        <script src="https://openlayers.org/en/v4.3.4/build/ol.js"></script>
        <script src="https://cdnjs.cloudflare.com/ajax/libs/proj4js/2.4.4/proj4.js"></script>
      </head>
      <body>
        <div id="map" class="map"></div>
        <script>
            /* JavaScript goes here */
        </script>
      </body>
    </html>

The first half of the file links to OpenLayers JavaScript mapping library
(CSS files and JavaScript files). The second half is mostly empty and
we will fill it now.

Here is the basic JavaScript code to get OpenStreetMap as a base map::

      var map = new ol.Map({
        layers: [
          new ol.layer.Tile({
            source: new ol.source.OSM()
          })
        ],
        target: 'map',
        controls: ol.control.defaults({
            attributionOptions: ({
            collapsible: false
          })
        }),
        view: new ol.View({
          projection: 'EPSG:4326',
          center: [0, 0],
          zoom: 2
        })
      });

Now would be the time to reload the page in the web browser. After that
we can add code to load our GeoJSON file before the code for
OpenStreetMap::

      var vectorSource = new ol.source.Vector({
        format: new ol.format.GeoJSON(),
        url: 'nc_state.geojson',
        attributions: "NC Boundary: Neteler &amp; Mitasova 2008"
      });
      var vectorLayer = new ol.layer.Vector({
        source: vectorSource
      });

We need to edit the list of layers in the code add the GeoJSON::

    var map = new ol.Map({
        layers: [
          new ol.layer.Tile({
            source: new ol.source.OSM()
          }),
          vectorLayer
        ],
        ...

Now you can look again in the web browser and you should see the borders
of North Carolina as a separate layer.

If you don't see it the reason might error in your JavaScript code or
the reason might be same-origin policy in you web browser.
You can tell the difference by starting developer tools in your web
browser and looking at messages in the console or log (e.g. in Firefox,
Tools -> Web Developer -> Toggle Tools -> Console).
Firefox `policy <https://developer.mozilla.org/en-US/docs/Same-origin_policy_for_file:_URIs>`_
allows for a local file in the same directory to be loaded,
so you should be good to go when using Firefox.
However, Chrome and Chromium require a special command line option
(replace ``chromium-browser`` by ``chrome`` or path to it if needed)::

    chromium-browser --disable-web-security --user-data-dir

Converting raster and its extracting metadata
`````````````````````````````````````````````

To make sharing of the geospatial data easier, we will again convert to
CRS:84. For that we will use *gdalwarp*. However, PNG cannot be written
directly using *gdalwarp* with the current version of GDAL, so we first
write a GDAL virtual dataset (VRT) and then we use *gdal_translate* to
convert the reprojected VRT to PNG.

::

    gdalwarp -of VRT -r average -t_srs crs:84 ncrast/elev_state_500m.tif elev_state_500m.vrt
    gdal_translate -of PNG elev_state_500m.vrt elev_state_500m.png

We are using PNG because unlike TIFF, web browsers can display it.
However, the PNG file itself does not carry the geospatial metadata
(unlike GeoTIFF). Therefore, we need to get the information from
the metadata and put it to JavaScript code manually. We already know
the coordinate reference system (but we can check it). What we need
to get is the extent and we can do that using *gdalinfo*::

    gdalinfo elev_state_500m.png

All we need is ``Lower Left`` and ``Upper Right`` and we could just
copy the numbers to the JavaScript code in the next section. However,
for this exercise, we will extract the extent in an automated way.
If you can't get GDAL version 2 or *jq* (see below), you can skip
executing commands in this part and just read through it
(but you should be good to go if you are using, e.g. an Ubuntu machine
from NCSU VCL).

What we want to get is the following line::

    [-84.4223856,  33.4882788, -75.0518788,  36.6207207]

The previous *gdalinfo* command gives output which can be processed by
*grep* and other command line tools, but the output format may not be
guaranteed to stay the same, so a new version may not work with command
based on it. For this reason we will use a more stable JSON output
offered by *gdalinfo*. For this, we need GDAL version 2 or higher,
so you need to make sure you have it. For example, on Ubuntu 16.04,
the version of GDAL is 1, so we need to add a PPA (Personal Package
Archive) repository which provides a more recent version of GDAL
with the cost of potential less stability within thesoftware or in
relation to other installed software. The commands to do it follow::

    sudo add-apt-repository ppa:ubuntugis/ubuntugis-unstable
    sudo apt update
    sudo apt upgrade

Now, with GDAL version 2 or higher, we can use the ``-json`` option
to obtain JSON output::

    gdalinfo -json elev_state_500m.png

JSON is not easily parseable with tools such as *grep*, however there
is a tool called *jq* which works in a similar way as *grep* and other
tools but for JSON. Here is an installation command for Ubuntu::

    sudo apt install jq

Now we can use *jq* and pipes in the same way we would use *grep*.
JSON format consists of keys and values in dictionaries where values
can be strings, numbers, lists, or dictionaries.
Using the ``.key`` syntax we get only the value associated with the
given key::

    gdalinfo -json elev_state_500m.png | jq .cornerCoordinates

We can pipe the output again to *jq* and get values for two keys
using ``.oneKey, .anotherKey`` syntax::

    gdalinfo -json elev_state_500m.png | jq .cornerCoordinates | \
        jq ".lowerLeft, .upperRight"

This gives us all information we need but not formated exactly
as we want it, i.e. a single list in one line, so we use *tr* to replace
newlines by spaces (``tr "\n" " "``), *sed* to replace ``] [`` by comma
(using expression ``/\] \[/,/``), and finally we use tr again to squeeze
all repeated spaces into one::

    gdalinfo -json elev_state_500m.png | jq .cornerCoordinates | \
        jq ".lowerLeft, .upperRight" | \
        tr "\n" " " | sed -e "s/\] \[/,/g" | tr -s " "

Alternatively, we can leverage more the *jq* command. The *jq* command
itself has a pipe syntax which has similar logic to the command line
pipes, so we can actually write expression
``.cornerCoordinates | lowerLeft, .upperRight``. To merge the two
separate list (which are the values ``.lowerLeft`` and ``.upperRight``),
we can use the plus operator in the *jq* expression
(``lowerLeft + .upperRight``). To avoid *jq* default formatting with one
list item per line, we use ``-c`` to create compact output. Then we
use *sed* just to replace comma by comma followed by a space
(expression ``/,/, /``) to have a better coding style in the JavaScript
code::

    gdalinfo -json elev_state_500m.png | \
        jq -c ".cornerCoordinates | [.lowerLeft[], .upperRight[]]" | \
        sed "s/,/, /g"

You can learn more about *jq* online or using::

    man jq

Same applies to *tr* and *sed* but using the *info* command instead of
the *man* command will give you full documentation::

    info tr

Adding raster
`````````````

Now, we can add the JavaScript code to the web page::

      var imageExtent = [-84.4223856, 33.4882788, -75.0518788, 36.6207207];
      var rasterLayer = new ol.layer.Image({
            source: new ol.source.ImageStatic({
              url: 'elev_state_500m.png',
              crossOrigin: '',
              projection: 'CRS:84',
              imageExtent: imageExtent,
              attributions: "NC Elevation: Neteler &amp; Mitasova 2008"
            })});

We need to edit the list of layers again to add the raster::

    var map = new ol.Map({
        layers: [
          new ol.layer.Tile({
            source: new ol.source.OSM()
          }),
          rasterLayer,
          vectorLayer
        ],
        ...

See the complete web page `here <../resources/openlayers_raster_and_vector.html>`_
and compare it with yours (you can see the code of the page in your web
browsers; usually using Ctrl+U).

Publishing with GitHub
``````````````````````

Now we will publish the web page using GitHub, specifically GitHub
Pages service which can be activated for any Git repository on GitHub.

Install Git on your local machine (command for Ubuntu)::

    sudo apt install git

Create a repository on GitHub. You will need write access to
the repository, so you need to use HTTPS and know your GitHub password
or set up SSH keys. If you are on a machine which is not yours (like
NCSU VCL machine), HTTPS will be easiest. Alternatively, just login to
GitHub (in a web browser) and use direct upload (e.g. with drag and
drop).

Now clone the repository. We will call it ``openlayers-test``
(``...`` stands for URL of the repository).

::

    git clone ... openlayers-test

Move the web page files into the repository, i.e. the HTML file,
the PNG file, and the GeoJSON file. Then change the directory to the
repository. You can use *mv* and *cd* to do that::

    mv index.html openlayers-test
    mv nc_state.geojson openlayers-test
    mv elev_state_500m.png openlayers-test
    cd openlayers-test

Add the files to the repository::

    git add index.html nc_state.geojson elev_state_500m.png

Now you can commit and push::

    git commit ...
    git push

Now go to the repository page on GitHub in your web browser, go to
*Settings* and in *Options* (loaded by default) find *GitHub Pages*.
In *Source* select *master branch*, then click *Save*. Wait for the page
to reload and show you the URL of the newly created web site which is
at yourusername.github.io/repository-name.

Colorize the raster and examine the change on GitHub
````````````````````````````````````````````````````

Now let's change the color table of the raster. For that we will use
*gdaldem* which accepts color tables in format one value-color pair per
line (similar format to what e.g. GRASS GIS uses).

The color table needs to be in a file. We can create a file from command
line without using a text editor, just by copy pasting the following
command line code block (all lines together)::

    cat > colors.txt <<EOF
    100% 255 255 255
    60%  235 220 175
    40%  190 185 135
    5%   240 250 150
    0     50 180  50
    nv   0 0 0 0
    EOF

The above code uses what is called *here-document*. The ``<<EOF``
part starts a content of a file and all is part of this file until
the line which says ``EOF``. This file (here-document) is used as input
to *cat* command which writes it to an actual file on the disk
(``cat > colors.txt``).

We use *gdaldem* in the ``color-relief`` mode, use the VRT dataset
as input, and output PNG (change the path to files as needed)::

    gdaldem color-relief -of PNG elev_state_500m.vrt colors.txt elev_state_500m.png -alpha

The ``-alpha`` option ensures that an alpha channel (transparency and
opacity) is written to the PNG file and together with ``nv 0 0 0 0``
line in  color table file, it ensures that NULL values are transparent.

Then commit the change in the PNG file and push::

    git commit elev_state_500m.png ...
    git push

Finally, go to GitHub and find the commit (change) you just made.
While Git in command line can't show differences in binary files such
as PNGs, GitHub has several different ways of exploring changes in
selected binary formats including PNGs.

Resources
---------

Repositories
````````````

* `How to deposit data on the OSF <https://osf.io/a5imq/wiki/How%20to%20Upload%20Data%20to%20the%20OSF>`_ (part of Reproducibility Project: Cancer Biology)
* `Hosting Data on Authorea <https://intercom.help/authorea/host-data>`_ (Authorea help pages)
* `Getting started with figshare: How to's <https://support.figshare.com/support/solutions/folders/6000200032>`_ (figshare Support pages)
* `Dryad Digital Repository: Frequently Asked Questions <http://datadryad.org/pages/faq>`_
* `Zenodo <http://zenodo.org/>`_
* `data.world <https://data.world/>`_
* `Hydroshare <http://hydroshare.org/>`_
* `OpenTopography <http://opentopography.org/>`_
* `Recommended Data Repositories by Nature <https://www.nature.com/sdata/policies/repositories>`_

Other
`````

* `Rendering and diffing images on GitHub <https://help.github.com/articles/rendering-and-diffing-images/>`_
* `Mapping GeoJSON files on GitHub <https://help.github.com/articles/mapping-geojson-files-on-github/>`_
* `EPSG.io <http://epsg.io/>`_ (Coordinate Systems Worldwide)
* `OpenLayers <http://openlayers.org/>`_

Assignment
----------

Explore the general repositories for scientific data linked above
and search for a repository which is used in your field. If you find
something what is not on the list, you can share it on the message
board.

Then go through the instructions to create your own simple, but
interactive web map showing a raster and vector and publish it through
GitHub. Send the link to the repository and to the web page online to
the message board.
