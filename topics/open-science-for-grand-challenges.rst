Open Science for Grand Challenges
=================================

This is material for a guest lecture in
*GIS 710: Geospatial Analytics for Grand Challenges*.

Lecture
-------

* `Open Science <../lectures/open-science-for-grand-challenges.html>`_

Hands-on exercise
-----------------

Goal: Public repository with research code and a way for everybody to run it.

Introduction to the tools and technologies:

* `Python in Binder <../lectures/python-in-binder.html>`_

Examples:

* `Simple example <https://github.com/wenzeslaus/trivial-example-for-binder>`_
* `Geospatial example <https://github.com/wenzeslaus/trivial-geospatial-example-for-binder>`_

Steps:

* Create an account on GitHub (https://github.com)
* Create repository on GitHub
* Create and edit files on GitHub using the web interface
* Write a trivial Python script (a + b or similar)
* Open the repository using Binder with JupyterLab
* Run the code
* Modify the code
* Update the repository content

Reading
-------

Please, consider reading the following papers as a preparation for the
discussion. They are all pro-open science, but they all will help you to
defend your stances in the debate. They are also useful for writing your
next paper which applies open science principles.

* Watson, M. (2015). When will ‘open science’ become simply ‘science’?. Genome biology, 16(1), 101. https://doi.org/10.1186/s13059-015-0669-2

* Ince, Darrel C., Leslie Hatton, and John Graham-Cumming. “The case for open computer programs”. In: Nature 482.7386 (2012), pp. 485–488. http://doi.org/10.1038/nature10836

* Rocchini, Duccio and Markus Neteler. “Let the four freedoms paradigm apply to ecology”. In: Trends in Ecology and Evolution (2012). http://doi.org/10.1016/j.tree.2012.03.009

Geospatial and more advanced examples
-------------------------------------

1. GRASS GIS in Jupyter Notebook using Binder

   * https://github.com/wenzeslaus/try-grass-in-jupyter
   * Highlights: Dataset download, general image display

1. Zonal statistics of solar time series in GRASS GIS with Python

   * https://github.com/wenzeslaus/grass-zonal-of-solar
   * Highlights: Two different types of image display (general and Matplotlib)

1. Google Colaboratory

   * From Google Earth Engine to GRASS GIS and back in a notebook

1. Code Ocean

   * https://doi.org/10.24433/CO.3986355.v2

1. Script and container-based solution without notebooks for running locally

   * https://doi.org/10.1186/s40965-017-0021-8
   * https://github.com/wenzeslaus/forestfrag3d
   * Highlights: Dockerfile, no notebooks, Travis CI, reusable code

1. Repository with reusable code

   * https://gitlab.com/vpetras/v.net.tripplanner
   * Highlights: GitLab, static generated web page

1. Notebooks for NCSU Geospatial Modeling and Analysis course

   * https://github.com/wenzeslaus/geospatial-modeling-course-jupyter
   * Highlights: Dockerfile, massive collection, converted from website, plain Python and IPython versions

1. GRASS GIS in Jupyter Notebook with Bash

   * https://github.com/wenzeslaus/try-grass-in-jupyter-with-bash
   * Highlights: plain Bash, start file

1. FUTURES model in JupyterLab using Binder

   * https://github.com/wenzeslaus/futures-model-intro-notebook
   * Highlights: model by CGA, R, compiled GRASS GIS, Binder files in a subdirectory

Discussion exercise
-------------------

* Split into three groups.
* Discuss open science using one of the three following positions.

Group 1
```````

For (open science proponents, in favor of open science)

Possible questions to start with:

* Why is open science necessary for science?
* Why is open science good?

Group 2
```````

Against (status quo proponents, opposed to open science)

Possible questions to start with:

* What are the reasons not to do open science?
* Is it even realistic?
* Can open science be sometimes even bad?
* Isn’t open science more trouble than it’s worth?

Group 3
```````

Middle way (pragmatics, neither for or against)

Possible questions to start with:

* Is there something in between?
* How to implement something to satisfy both groups above?
* Is something like partial open science more sustainable?
* Should we implement something transitional (for now)?

Assignment
----------

Write a blog post.
