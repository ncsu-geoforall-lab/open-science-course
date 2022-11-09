Open Science for Grand Challenges
=================================

This is material for a guest lecture in
*GIS 710: Geospatial Analytics for Grand Challenges*.

Reading
-------

Please, read the following papers as a preparation for the lecture and the discussion:

* Watson, Mick (2015). “When will ‘open science’ become simply ‘science’?“. In: Genome biology, 16(1), 101. https://doi.org/10.1186/s13059-015-0669-2

Here are two optional papers:

* Ince, Darrel C., Leslie Hatton, and John Graham-Cumming (2012). “The case for open computer programs”. In: Nature 482.7386, pp. 485–488. http://doi.org/10.1038/nature10836

* Rocchini, Duccio and Markus Neteler (2012). “Let the four freedoms paradigm apply to ecology”. In: Trends in Ecology and Evolution. http://doi.org/10.1016/j.tree.2012.03.009

Lecture
-------

(60 min)

* `Open Science <../lectures/open-science-for-grand-challenges.html>`_

(Break: 15 min)

Class Debate
------------

(5+25+5+5+5+15 min)

* Debate for and against a resolution about scientific publications.
* Two teams. Affirmative agrees with the resolution and Negative disagrees with the resolution.

Resolution
``````````

A scientific publication needs to consist of text, data, source code, software environment, and reviews
which are all openly licensed, in open formats, checked during the submission process, and publicly available without any delay after publication.

Context
```````

* Text: The main part of the publication, the “classic” article, with narrative, figures, tables, etc.
* Data: Recorded factual material, raw input data, resulting data.
* Source code: Unique code including code to generate numbers, figures, and tables for the text.
* Software environment: Software setup where to apply the source code to the input data.
* Reviews: Parts of the review process, esp. comments from reviewers and publication versions.
* The Open Definition: Content can be freely used, modified, and shared by anyone for any purpose.
* Open format: File format based on an open standard and readable by open source software.
* Data embargo: Period during which a scheduled-to-be-public data remains private.
* FAIR:  Findability, Accessibility, Interoperability, and Reuse of digital assets, esp. data.
* Findability (in FAIR):  (Meta)data are registered and assigned a persistent identifier.
* Accessibility (in FAIR): Sharing protocol is open, free, and universally implementable.
* Interoperability (in FAIR): (Meta)data use formal language and references to other datasets.
* Reuse (in FAIR): (Meta)data are richly described with a plurality of accurate and relevant attributes.

Consider
````````

* Scientists are concerned with additional work and being scooped.
* Research funding agencies with limited financial resources focused on innovation.
* Citizens who want to have access to science which influences their lives.
* Industry and entrepreneurs who want to reap benefits of tax-funded research.
* Number of special cases including sensitive personal data and data related to national security.

Hands-on exercise
-----------------

Goal: Public repository with research code and a way for everybody to run it.

Introduction to the tools and technologies (20 min):

* `Python in Binder <../lectures/python-in-binder.html>`_

Examples (15 min):

* `Simple example <https://github.com/wenzeslaus/trivial-example-for-binder>`_
* `Geospatial example <https://github.com/wenzeslaus/trivial-geospatial-example-for-binder>`_

Task:

* Create a Git repository which opens in Binder and contains a script and a notebook.

Steps (20-40 min):

* If you don't have it already, create an account on GitHub (https://github.com).
* Create a new (Git) repository on GitHub.
* Write a trivial Python script
  * ``c = a + b`` followed by ``print(c)`` or something similar is sufficient.
  * You can create and edit files on GitHub using the web interface
* Open the repository using Binder at `mybinder.org <https://mybinder.org>`_.
* Create a new notebook.
  * New button in top right corner. Pick (notebook:) Python 3.
  * Name the notebook at the top of the page (Example or Test 1 are good names here).
* Run the script from the notebook (``!python script_name.py``).
* Optionally, add some Python code to the notebook itself.
* Download the notebook.
  * You should end up with file with ``.ipynb`` extension.
* Upload the file to your repository on GitHub.
* Repeat as needed.
  * Typically, you would develop your code elsewhere avoiding the cumbersome update loop
    like in this workflow.
  * JupyterLab and Jupyter Notebook in Binder allow you to save the document to
    your web browser storage allowing you to pick up where you left last time.
  * It is not advised (by Binder) to upload to GitHub from Binder for security reasons (or enter
    any credentials) for security reasons (this may change in the future).
* Include link to Binder (the Launch Binder button) to your readme file.
  * Specify you want to use JupyterLab (instead of Jupyter Notebook) using ``?urlpath=lab``.
  * Make it show your notebook right away by extending the above to
    ``?urlpath=lab/tree/Example.ipynb`` where ``Example.ipynb`` is name of your notebook.

(Break: 10 min)

Extra tasks:

* Write code which uses *rasterio* to display data or to get its CRS in the notebook.
* Put that code into a separate file and use it in notebook.
  * Do not run the file.
  * Make it so that it works for the data display and that you can store the CRS in a variable.

Geospatial and more advanced examples
-------------------------------------

(60 min)

Examples using Binder:

1. Hydrology and zonal statistics in GRASS GIS in JupyterLab

   * https://mybinder.org/v2/gh/OSGeo/grass/0e43bf349d8b6b0291e094681b9c1c79909bdda5?urlpath=lab%2Ftree%2Fdoc%2Fnotebooks%2Fhydrology.ipynb
   * Highlights: Included dataset, two different types of plotting (GRASS-specific general and Matplotlib)

1. Sudden Oak Death example for PoPS model in JupyterLab

   * https://github.com/ncsu-landscape-dynamics/pops-intro-grass-notebook
   * Highlights: model by CGA, compiled GRASS GIS, Binder files in a subdirectory, JupyterLab

1. FUTURES model in JupyterLab

   * https://github.com/ncsu-landscape-dynamics/futures-model-intro-notebook
   * Highlights: model by CGA published as a GRASS GIS module, R, compiled GRASS GIS, Binder files in a subdirectory

1. Species distribution modeling with R and GRASS GIS in RStudio

   * https://github.com/LukasGab/R_grassgis/tree/link-external-data
   * Highlights: RStudio in Binder

Examples not using Binder:

1. Code Ocean

   * https://doi.org/10.24433/CO.3986355.v2

1. Script and container-based solution without notebooks for running locally

   * https://doi.org/10.1186/s40965-017-0021-8
   * https://github.com/wenzeslaus/forestfrag3d
   * Highlights: Dockerfile, no notebooks, Travis CI, reusable code

1. Repository with reusable code

   * https://gitlab.com/vpetras/v.net.tripplanner
   * Highlights: GitLab, static generated web page

Outro
-----

(15 min)

* `Open Science: Outro <../lectures/open-science-for-grand-challenges-outro.html>`_

Assignment
----------

Blog Assignment. Reflect on the theory and practice of open geospatial
science. In 250 words or less, please share your viewpoint on where you
stand in today's role playing debate. Also consider sharing challenges
that are preventing you from practicing open science if you are in
favor of it. Your blog will be evaluated based on the following rubric:
1) clarity (good grammar, succinct logical flow and organization), 2)
compellingness (persuasiveness, well-grounded in evidence), critical
thinking (evaluation of facts to form a judgment or opinion), and 3)
creativity (originality of ideas). Please see class instructions in
Google Drive for the latest instructions and due date.
