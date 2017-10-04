Publishing data on web
======================

Install GDAL and *jq* (command for Ubuntu)::

    sudo apt install gdal-bin jq

::

    ogr2ogr -f GeoJSON -t_srs crs:84 nc_state.geojson ncshape/nc_state.shp

::

    gdalinfo elev_state_500m.png

::

    gdalinfo -json elev_state_500m.png | jq .cornerCoordinates | \
        jq ".lowerLeft, .upperRight" | \
        tr "\n" " " | sed -e "s/\] \[/,/g" | tr -s " "

::

    gdalinfo -json elev_state_500m.png | \
        jq -c ".cornerCoordinates | [.lowerLeft[], .upperRight[]] " | \
        sed "s/,/, /g"

::

    gdalwarp -of VRT -r average -t_srs crs:84 ncrast/elev_state_500m.tif elev_state_500m.vrt
    gdal_translate -of PNG elev_state_500m.vrt elev_state_500m.png

::

    gdalinfo elev_state_500m.png


Firefox `policy <https://developer.mozilla.org/en-US/docs/Same-origin_policy_for_file:_URIs>`_
allows for a local file in the same directory to be loaded.
Chrome and Chromium require a special command line option
(replace ``chromium-browser`` by ``chrome`` or path to it if needed)::

    chromium-browser --disable-web-security --user-data-dir

::

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

::

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

::

      var vectorSource = new ol.source.Vector({
        format: new ol.format.GeoJSON(),
        url: 'nc_state.geojson',
        attributions: "NC Boundary: Neteler &amp; Mitasova 2008"
      });
      var vectorLayer = new ol.layer.Vector({
        source: vectorSource
      });

::

      var imageExtent = [-84.4223856,  33.4882788, -75.0518788,  36.6207207];
      rasterLayer = new ol.layer.Image({
            source: new ol.source.ImageStatic({
              url: 'elev_state_500m.png',
              crossOrigin: '',
              projection: 'CRS:84',
              imageExtent: imageExtent,
              attributions: "NC Elevation: Neteler &amp; Mitasova 2008"
            })});

::

    var map = new ol.Map({
        layers: [
          new ol.layer.Tile({
            source: new ol.source.OSM()
          }),
          rasterLayer,
          vectorLayer
        ],

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

::

    git add nc_state.geojson elev_state_500m.png

::

    git commit ...
    git push

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

Other
`````

* `Rendering and diffing images on GitHub <https://help.github.com/articles/rendering-and-diffing-images/>`_
* `Mapping GeoJSON files on GitHub <https://help.github.com/articles/mapping-geojson-files-on-github/>`_
* `EPSG.io <http://epsg.io/>`_ (Coordinate Systems Worldwide)
