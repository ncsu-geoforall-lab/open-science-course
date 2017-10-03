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


Resources
---------

* `How to deposit data on the OSF <https://osf.io/a5imq/wiki/How%20to%20Upload%20Data%20to%20the%20OSF>`_ (part of Reproducibility Project: Cancer Biology)
* `Hosting Data on Authorea <https://intercom.help/authorea/host-data>`_ (Authorea help pages)
* `Getting started with figshare: How to's <https://support.figshare.com/support/solutions/folders/6000200032>`_ (figshare Support pages)
