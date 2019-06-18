Combining text, code, results, and software
===========================================

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

Jupyter supports different languages including Python, R, Julia,
Haskell, and Ruby.

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

Adding the computational environment
------------------------------------

Docker
``````

Official Docker website: https://www.docker.com/

Docker is open source under Apache 2.0 license but some additional
components and tools are under different licenses including proprietary
ones.

Installing Docker
`````````````````

For this week we will need to install Docker. Here are instructions for
different operating systems. The version you need to install for
MS Windows and Mac OS is called Docker Toolbox. On Ubuntu, the package
is currently called docker.io.

MS Windows:

https://docs.docker.com/toolbox/toolbox_install_windows/

Mac OS:

https://docs.docker.com/toolbox/toolbox_install_mac/

Ubuntu:

::

    sudo apt-get install docker.io
    sudo groupadd docker
    sudo usermod -aG docker $USER

In the Ubuntu (Linux) installation, for the change of group to take
place (``usermod``), you need to login again.
Logging out and logging in is one way. A more convenient way
is the following command:

::

    su - $USER

You may need to agree with EULA or some terms and conditions in order
to get the MS Windows or Mac OS version. If you don't feel comfortable
installing it on your computer at this point or it doesn't work for you,
you can use NCSU VCL Ubuntu machine.

Building and running
````````````````````

Build an image using content of a GitHub repository::

    docker build -t pointcloud-nb github.com/wenzeslaus/Notebook-for-processing-point-clouds-in-GRASS-GIS

Now run a container based on the newly created image::

    docker run -p 8888:8888 pointcloud-nb

Resources
---------

Videos [main resources]
```````````````````````

* `Introduction to Jupyter <http://fatra.cnr.ncsu.edu/open-science-course/notebooks-jupyter-intro.mp4>`_ (recording from the class, 14 mins)
* `Files in Jupyter <http://fatra.cnr.ncsu.edu/open-science-course/notebooks-jupyter-publish.mp4>`_ (recording from the class, 6 mins)
* `Files in Jupyter <http://fatra.cnr.ncsu.edu/open-science-course/notebooks-jupyter-files.mp4>`_ (recording from the class, 8 mins)
* `Installing Jupyter and GRASS GIS on Ubuntu <http://fatra.cnr.ncsu.edu/open-science-course/notebooks-jupyter-install-linux.mp4>`_ (recording from the class, 18 mins)
* `Installing Jupyter on MS Windows with OSGeo4W <http://fatra.cnr.ncsu.edu/open-science-course/notebooks-jupyter-install-mswindows.mp4>`_ (recording from the class, 14 mins)
* `Reproducible computational environments: Overview of tools <http://fatra.cnr.ncsu.edu/open-science-course/environments-intro.mp4>`_ (recording from the class, 24 mins)
* `Reproducible computational environments: Docker <http://fatra.cnr.ncsu.edu/open-science-course/environments-docker.mp4>`_ (recording from the class, 20 mins)
* `Reproducible computational environments: How to use Docker <http://fatra.cnr.ncsu.edu/open-science-course/environments-docker-how.mp4>`_ (recording from the class, 40 mins)
* `Reproducible computational environments: About Docker isolation <http://fatra.cnr.ncsu.edu/open-science-course/environments-docker-isolation.mp4>`_ (recording from the class, 2 mins)

Slides
``````

* `Lecture slides <../lectures/environments.html>`_ [main resource]

Additional videos
`````````````````

* `Jupyter Notebook Tutorial: Introduction, Setup, and Walkthrough <https://www.youtube.com/watch?v=HW29067qVWk>`_ (30 mins)
* `Jupyter Notebook Tutorial <https://www.youtube.com/watch?v=q_BzsPxwLOE&list=PLeo1K3hjS3uuZPwzACannnFSn9qHn8to8>`_ (YouTube playlist by codebasics)
* `Scripting GRASS GIS 7 with Python <https://www.youtube.com/watch?v=PX2UpMhp2hc>`_ (2 hours)
* `Docker Tutorial - What is Docker & Docker Containers, Images, etc? <https://www.youtube.com/watch?v=pGYAg7TMmp0>`_ (by LearnCode.academy, 8 mins)
* `Introduction to Docker <https://www.youtube.com/watch?v=Q5POuMHxW-0>`_ (by Solomon Hykes at Twitter University, 47 mins)

Texts
`````

* `Jupyter Notebook Tutorial: The Definitive Guide <https://www.datacamp.com/community/tutorials/tutorial-jupyter-notebook>`_
* `Basics of Jupyter Notebook and Python <https://datahub.packtpub.com/tutorials/basics-jupyter-notebook-python/>`_
* `Notebook interface <https://en.wikipedia.org/wiki/Notebook_interface>`_
* `Literate programming <https://en.wikipedia.org/wiki/Literate_programming>`_

References
``````````

* Boettiger, C. (2015). An introduction to Docker for reproducible research. ACM SIGOPS Operating Systems Review, 49(1), 71-79.


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
