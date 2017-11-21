Combining text, code and results into one document
==================================================

One innovation related to open science are computational notebooks
also known as notebook interfaces or data science notebooks.
These notebooks are electronic, interactive notebooks used for
data analysis, visualization, computations and programming.
Computational notebooks serve as word processing software, software
development tool, and as a record of the result.
We will focus on one specific notebook software called Jupyter.

Jupyter Notebooks (formerly IPython Notebooks) are a tool aspiring to be
a standard way of modern and future data analysis. The notebook format
allows any code and its output to be viewed together and also run again.
Given all the dependencies and data are right, the computation and
results can be reproduced on any computer.

Jupyter supports different languages including Python, R, Julia, Haskell and Ruby.

Official Jupyter website: https://jupyter.org/

Python code, can be executed as expected::

    a = 6
    b = 7
    c = a + b

Each piece of code is called cell. To execute a cell, use Shift+Enter

To show the result, as in interactive console, use just the name of the
variable::

    c

This should show number 13 right under the letter ``c``.

Alternatively, use print (statement in Python 2 and function in
Python 3)::

    print "Result is", c

What is unique to Jupyter is that Python code can be mixed with command
line code (like Bash). To do that, it is enough just to prefix the
command line with an exclamation mark::

    !echo "Result is $c"

The variables from Python code are referenced in the same way as
variables in Bash.


Install Jupyter on your computer
--------------------------------

If you are already using Anaconda, use it to install Jupyter, otherwise
follow the instructions for each operating system.

Linux
`````

Use system packages or pip packages, e.g. on Ubuntu::

    sudo apt install python-pip
    sudo pip install jupyter

Windows
```````

Install OSGeo4W, then run OSGeo4W Shell as administrator. There, update
pip first::

    pip install -U pip

Then update setuptools::

    pip install -U setuptools

Then install Jupyter::

    pip install Jupyter

Mac OS
``````

Since we will be using Jupyter with GRASS GIS, run GRASS GIS first
to be sure you will use Python which GRASS GIS uses.

Then in the GRASS GIS terminal run::

    pip install -U pip
    sudo pip install jupyter

Alternatively, if the above does not work, you can try Homebrew.
Use it to install Jupyter::

    brew install jupyter

Alternatives to Jupyter
-----------------------

There are both open source and proprietary notebooks. Besides Jupyter,
the open source include R Notebooks (R Markdown) and Apache Zeppelin.
Same concepts as we can find in notebooks are also in tools which are
usually not considered computational notebooks but can be used in the
same way; examples include Emacs Org mode and LaTeX.

Resources
---------

Texts
`````

* `Jupyter Notebook Tutorial: The Definitive Guide <https://www.datacamp.com/community/tutorials/tutorial-jupyter-notebook>`_
* `Basics of Jupyter Notebook and Python <https://datahub.packtpub.com/tutorials/basics-jupyter-notebook-python/>`_
* `Notebook interface <https://en.wikipedia.org/wiki/Notebook_interface>`_
* `Literate programming <https://en.wikipedia.org/wiki/Literate_programming>`_

Videos
``````

* `Computational Notebooks: Introduction to Jupyter <http://fatra.cnr.ncsu.edu/open-science-course/notebooks-jupyter-intro.mp4>`_ (recording from the class, 14 mins)
* `Computational Notebooks: Files in Jupyter <http://fatra.cnr.ncsu.edu/open-science-course/notebooks-jupyter-publish.mp4>`_ (recording from the class, 6 mins)
* `Computational Notebooks: Files in Jupyter <http://fatra.cnr.ncsu.edu/open-science-course/notebooks-jupyter-files.mp4>`_ (recording from the class, 8 mins)
* `Computational Notebooks: Installing Jupyter and GRASS GIS on Ubuntu <http://fatra.cnr.ncsu.edu/open-science-course/notebooks-jupyter-install-linux.mp4>`_ (recording from the class, 18 mins)
* `Computational Notebooks: Installing Jupyter on MS Windows with OSGeo4W <http://fatra.cnr.ncsu.edu/open-science-course/notebooks-jupyter-install-mswindows.mp4>`_ (recording from the class, 14 mins)
* `Jupyter Notebook Tutorial: Introduction, Setup, and Walkthrough <https://www.youtube.com/watch?v=HW29067qVWk>`_ (30 mins)
* `Jupyter Notebook Tutorial <https://www.youtube.com/watch?v=q_BzsPxwLOE&list=PLeo1K3hjS3uuZPwzACannnFSn9qHn8to8>`_ (YouTube playlist by codebasics)
* `Scripting GRASS GIS 7 with Python <https://www.youtube.com/watch?v=PX2UpMhp2hc>`_ (2 hours)

Assignment
----------

Practice and get familiar with using Jupyter Notebooks using the
Try Jupyter! service. If needed, use one of the linked resources above
to learn about Jupyter.

* https://try.jupyter.org/

Try using the Jupyter for geospatial tasks with GRASS GIS using the
URL given in Moodle. Go through the execution of one of the notebooks.

Then, install Jupyter on your computer (see above) and try to run it
with GRASS GIS. If that fails for some reason, use the NCSU VCL Ubuntu
machine for the rest of the assignment.

Then transfer the following code (all or just a part) to a Jupyter
notebook on your computer, execute the code, do modifications if needed,
and create a PDF document with the results.

* https://github.com/wenzeslaus/geospatial-modeling-course-jupyter/blob/master/notebooks/buffers_cost_python.ipynb

Submit the created PDF to Moodle.
If you did something different for the installation or you were not able
to install it at all, submit comments on that as part of the document.
