Open Science for Grand Challenges
=================================

This is material for a guest lecture in
*GIS 710: Geospatial Analytics for Grand Challenges*.

Reading
-------

Please, read the following papers as a preparation for the lecture and the discussion:

* Watson, Mick (2015). “When will ‘open science’ become simply ‘science’?“. In: Genome biology, 16(1), 101. https://doi.org/10.1186/s13059-015-0669-2

Optional: Here are two additional papers. Both are pro-open science,
but they can help you to defend your stances in the classroom debate.
They are also useful for writing your next paper which applies open science principles.

* Ince, Darrel C., Leslie Hatton, and John Graham-Cumming (2012). “The case for open computer programs”. In: Nature 482.7386, pp. 485–488. http://doi.org/10.1038/nature10836

* Rocchini, Duccio and Markus Neteler (2012). “Let the four freedoms paradigm apply to ecology”. In: Trends in Ecology and Evolution. http://doi.org/10.1016/j.tree.2012.03.009

Lecture
-------

(60 min)

* `Open Science <../lectures/open-science-for-grand-challenges.html>`_

Discussion exercise
-------------------

(30+30 min)

* Split into three groups.
* Each group will spend ~30 minutes preparing an argument for their prepared position. Each group will select one member to give a 1-2 minute opening statement outlining their position in addition to discussing their position in depth to select the best arguments in their favor. 
* After re-grouping, each position will offer their opening statement before the discussion floor is opened to all participants. Participants should focus on discussing the relative strengths of their position while highlighting the relative weaknesses of the others. 
* Discuss open science using one of the three following positions.

Group 1
```````

For (open science proponents, in favor of open science)

Possible questions to start with:

* Why is open science necessary for science?
* Why is open science good?
* What are our goals in science and how much do they overlap with open science?

Group 2
```````

Against (status quo proponents, opposed to open science)

Possible questions to start with:

* What are the reasons not to do open science?
* Is it even realistic?
* Does it now or would it ever deliver on its promises?
* Can open science be sometimes even bad?
* Isn’t open science more trouble than it’s worth?
* How is open science supposed to work for industry?

Group 3
```````

Middle way (pragmatics, neither for or against)

Possible questions to start with:

* Is there something in between?
* How to implement something to satisfy both groups above?
* Is something like partial open science more sustainable?
* Should we implement something transitional (for now)?
* Does reviewer needs to see more than a reader?

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

1. GRASS GIS in Jupyter Notebook using Binder

   * https://github.com/wenzeslaus/try-grass-in-jupyter
   * Highlights: Dataset download, general image display

1. Zonal statistics of solar time series in GRASS GIS with Python

   * https://github.com/wenzeslaus/grass-zonal-of-solar
   * Highlights: Two different types of image display (general and Matplotlib)

1. Sudden Oak Death example for PoPS model in Binder

   * https://github.com/ncsu-landscape-dynamics/pops-intro-grass-notebook
   * Highlights: model by CGA, compiled GRASS GIS, Binder files in a subdirectory, JupyterLab

1. FUTURES model in JupyterLab using Binder

   * https://github.com/wenzeslaus/futures-model-intro-notebook
   * Highlights: model by CGA published as a GRASS GIS module, R, compiled GRASS GIS, Binder files in a subdirectory

1. Species distribution modeling with R and GRASS GIS in RStudio

   * https://github.com/LukasGab/R_grassgis
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
creativity (originality of ideas). Please submit your blog post as a
PDF to Moodle by October 12.
