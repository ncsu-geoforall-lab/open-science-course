Combining text, code and results into one document
==================================================

One innovation related to open science are computational notebooks
also known as notebook interfaces or data science notebooks.
These notebooks are electronic, interactive notebooks used for
data analysis, visualization, computations and programming.
It pairs the functionality of word processing software with both the shell and kernel of that notebook's programming language.
Examples of the notebook interface include the Mathematica notebook, Maple worksheet, MATLAB notebook, IPython/Jupyter, R Markdown, Apache Zeppelin, Apache Spark Notebook, and the Databricks cloud.[2]

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
    c = a * b

Each piece of code is called cell. To execute a cell, use Shift+Enter

To show the result, as in interactive console, use just the name of the
variable::

    c

Alternatively, use print (statement in Python 2 and function in
Python 3)::

    print "Answer is", c

What is unique to Jupyter is that Python code can be mixed with command
line code (like Bash). To do that, it is enough just to prefix the
command line with an exclamation mark::

    !echo "Answer is $c"

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

Mac OS
``````

If you are already using Homebrew, use it to install Jupyter::

    brew install jupyter

Alternatives to Jupyter
-----------------------

There are both open source and proprietary notebooks. The open source
include, besides Jupyter, R Notebooks and Apache Zeppelin.


Resources
---------

Texts
`````

* `Jupyter Notebook Tutorial: The Definitive Guide <https://www.datacamp.com/community/tutorials/tutorial-jupyter-notebook>`_
* `Basics of Jupyter Notebook and Python <https://datahub.packtpub.com/tutorials/basics-jupyter-notebook-python/>`_

Videos
``````

* `Jupyter Notebook Tutorial: Introduction, Setup, and Walkthrough <https://www.youtube.com/watch?v=HW29067qVWk>`_ (30 mins)
* `Jupyter Notebook Tutorial <https://www.youtube.com/watch?v=q_BzsPxwLOE&list=PLeo1K3hjS3uuZPwzACannnFSn9qHn8to8>`_ (YouTube playlist by codebasics)
* `Scripting GRASS GIS 7 with Python <https://www.youtube.com/watch?v=PX2UpMhp2hc>`_ (2 hours)

Assignment
----------

Practice and get familiar with using Jupyter Notebooks using the
Try Jupyter! service.

* https://try.jupyter.org/

Install Jupyter on your computer and try to run it with GRASS GIS. If
that fails for some reason, use the NCSU VCL Ubuntu machine for the
rest of the assignment.

Then transfer the following code (all or just a part) to a Jupyter
notebook on your computer, execute the code, do modifications if needed,
and create a PDF document with the results.

* https://github.com/wenzeslaus/geospatial-modeling-course-jupyter/blob/master/notebooks/buffers_cost_python.ipynb
