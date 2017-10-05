Publishing data on web
======================

Custom web page with geospatial data
------------------------------------

Preparation
```````````

Install GDAL and *jq* (command for Ubuntu)::

    sudo apt install gdal-bin jq

Get data and upack them::

    wget http://grass.osgeo.org/sampledata/north_carolina/nc_rast_geotiff.tar.gz
    wget http://grass.osgeo.org/sampledata/north_carolina/nc_shape.tar.gz
    tar xvf nc_rast_geotiff.tar.gz
    tar xvf nc_shape.tar.gz

Covert Shapefile to GeoJSON::

    ogr2ogr -f GeoJSON -t_srs crs:84 nc_state.geojson ncshape/nc_state.shp

Web page
````````

Now create a file in a text editor with the following HTML code
and open this file in a web browser::

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

::

    gdalwarp -of VRT -r average -t_srs crs:84 ncrast/elev_state_500m.tif elev_state_500m.vrt
    gdal_translate -of PNG elev_state_500m.vrt elev_state_500m.png

GDAL >=2

::

    gdalinfo elev_state_500m.png

Lower Left, Upper Right

[-84.4223856,  33.4882788, -75.0518788,  36.6207207]

optional
::

    gdalinfo -json elev_state_500m.png | jq .cornerCoordinates | \
        jq ".lowerLeft, .upperRight" | \
        tr "\n" " " | sed -e "s/\] \[/,/g" | tr -s " "

::

    gdalinfo -json elev_state_500m.png | \
        jq -c ".cornerCoordinates | [.lowerLeft[], .upperRight[]] " | \
        sed "s/,/, /g"

Adding raster
`````````````

Now, we can add the JavaScript code to the web page::

      var imageExtent = [-84.4223856,  33.4882788, -75.0518788,  36.6207207];
      rasterLayer = new ol.layer.Image({
            source: new ol.source.ImageStatic({
              url: 'elev_state_500m.png',
              crossOrigin: '',
              projection: 'CRS:84',
              imageExtent: imageExtent,
              attributions: "NC Elevation: Neteler &amp; Mitasova 2008"
            })});

See the complete web page `here <../resources/openlayers_raster_and_vector.html>`_.

Install Git (command for Ubuntu)::

    sudo apt install git

Create a repository on GitHub. Clone it. You will need write access to
the repository, so you need to use HTTPS and know your GitHub password
or set up SSH keys. If you are on a machine which is not yours, HTTPS
will be easiest. Alternatively, just login to GitHub and use direct
upload (e.g. with drag and drop).

::

    git clone ...

Move the web page files into the repository, i.e. the HTML file,
the PNG file, and the GeoJSON file. You can use *mv* to do that::

    mv index.html openlayers-test
    mv nc_state.geojson openlayers-test
    mv elev_state_500m.png openlayers-test

::

    git add nc_state.geojson elev_state_500m.png

::

    git commit ...
    git push

Colorize the raster and examine the change on GitHub
````````````````````````````````````````````````````

gdaldem

::

    cat > colors.txt <<EOF
    100% 255 255 255
    60%  235 220 175
    40%  190 185 135
    5%   240 250 150
    0     50 180  50
    nv   0 0 0 0
    EOF

::

    gdaldem color-relief -of PNG elev_state_500m.vrt colors.txt elev_state_500m.png -alpha

::

    git commit elev_state_500m.png ...
    git push



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

Assignment
----------
