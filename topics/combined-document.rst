Combining text, code, results, and software
===========================================

One innovation related to open science are computational notebooks
also known as notebook interfaces or data science notebooks.
These notebooks are electronic, interactive notebooks used for
data analysis, visualization, computations and programming.
Computational notebooks serve as word processing software, software
development tool, and as a record of the result.
We will focus on one specific notebook software called Jupyter,
but there is more similar technologies such as R Markdown which can be
used to create R Notebooks in RStudio.

Jupyter Notebooks (formerly IPython Notebooks) are a tool aspiring to be
a standard way of modern and future data analysis. The notebook format
allows any code and its output to be viewed together and also run again.
Besides the notebooks, Jupyter can be also used as JupyterLab
which is an environment combining multiple notebooks, code editor,
and file browser together.
Jupyter supports different languages including Python, R, Julia,
Haskell, and Ruby as well as access to system command line.

Given all the dependencies and data are right, the computation and
results can be reproduced on any computer.
This is a big goal and Jupyter does not fulfill it by itself,
but tool such as Docker (see below) help with bigger software
portability challenges.


Alternatives to Jupyter
-----------------------

There are both open source and proprietary notebooks. Besides Jupyter,
the open source ones include the aforementioned R Notebooks (R Markdown)
and Apache Zeppelin.
We can find concepts from the notebooks present also in tools which are
usually not considered computational notebooks but can be used in the
same way; examples include Emacs Org mode and LaTeX.


Intro to Jupyter
----------------

Official Jupyter website: https://jupyter.org/

We will use a website called Binder (https://mybinder.org) which
allows anybody to run a any public Git repository as a collection of
Jupyter Notebooks.

https://mybinder.org/v2/gh/ncsu-geoforall-lab/open-science-course-notebook/master?filepath=notebook.ipynb

In the notebook Python code, can be executed as expected::

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

One of the things unique to Jupyter is that Python code can be mixed
with command line code (like Bash). To do that, it is enough just to
prefix the command line with an exclamation mark::

    !echo "Result is $c"

The variables from Python code are referenced in the same way as
variables in Bash.

You can see further examples as well as complete guide to Jupyter
at:

https://jupyter.org/try


Adding computational environment
--------------------------------

There is several ways how to add additional software to Binder we used
above. Many of those work also in general for desktop computers.
We will look at one which is the most powerful and most general one
because in case of geospatial software, the other techniques are not
enough and we often need to use this one. Specifically we will use
Docker which is an example of technique which does not wrap just
couple of Python packages or one software but it wraps a whole operating
system together.

Since we are wrapping other software using Docker and we are sharing the
result (as something people can use themselves), it is most
advantageous when the software is open source because this gives us
the freedom to share it and distribute it in various forms.

Docker
``````

Docker is way of separating computational environments. In some ways,
it is similar to virtual machines, but it is lightweight and
configurable in a reproducible way.

Docker is open source under Apache 2.0 license but some additional
components and tools are under different licenses including proprietary
ones.

Official Docker website: https://www.docker.com/

Installing Docker
`````````````````

Docker runs on Linux, macOS and Windows, however we will use
an NCSU VCL Ubuntu machine to simplify things. In the terminal, run
the following set of commands which installs Docker and allows your user
to access it:

::

    sudo apt-get install docker.io
    sudo groupadd docker
    sudo usermod -aG docker $USER

The above changed added a group your user now belongs to.
For this change to take place (specifically the ``usermod`` command),
you need to login again.
Logging out and logging in is one way. A more convenient way
is the following command which logging you again just in the terminal
you are using:

::

    su - $USER

Side note: When you later on decide to install Docker on your computer,
you may need to agree with EULA or some other terms and conditions in
order to install it on MS Windows or macOS version as Docker
installation for the these versions is not completely open source.

Building and running Docker image
`````````````````````````````````

Build an image using content of a GitHub repository::

    docker build -t geo-jupyter github.com/wenzeslaus/geospatial-modeling-course-jupyter/

Now run a container based on the newly created image::

    docker run -p 8888:8888 geo-jupyter

It tells you an URL where you will find the running Jupyter Notebook
(use web browser in the VCL machine). The URL you need to use will be
something like:

    localhost:8888/?token=a_long_token

The ``a_long_token`` is what you need to copy from the command line.

The reason why the above works is that the Git repository contains
a *Dockerfile* which defines what software to install. Docker follows
the instructions in the Dockerfile, constructs a Docker *image*,
here named ``geo-jupyter`` and we then run a Docker *container*
based on this image.

Docker is what Binder is using in the background and you can prepare
an environment for Binder using a Dockerfile.


Resources
---------

Videos
``````

* `Introduction to Jupyter <http://fatra.cnr.ncsu.edu/open-science-course/notebooks-jupyter-intro.mp4>`_ (recording from the class, 14 mins)
* `Publishing a Jupyter Notebook <http://fatra.cnr.ncsu.edu/open-science-course/notebooks-jupyter-publish.mp4>`_ (recording from the class, 6 mins)
* `Files in Jupyter <http://fatra.cnr.ncsu.edu/open-science-course/notebooks-jupyter-files.mp4>`_ (recording from the class, 8 mins)
* `Installing Jupyter and GRASS GIS on Ubuntu <http://fatra.cnr.ncsu.edu/open-science-course/notebooks-jupyter-install-linux.mp4>`_ (recording from the class, 18 mins)
* `Installing Jupyter on MS Windows with OSGeo4W <http://fatra.cnr.ncsu.edu/open-science-course/notebooks-jupyter-install-mswindows.mp4>`_ (recording from the class, 14 mins)
* `Reproducible computational environments: Overview of tools <http://fatra.cnr.ncsu.edu/open-science-course/environments-intro.mp4>`_ (recording from the class, 24 mins)
* `Reproducible computational environments: Docker <http://fatra.cnr.ncsu.edu/open-science-course/environments-docker.mp4>`_ (recording from the class, 20 mins)
* `Reproducible computational environments: How to use Docker <http://fatra.cnr.ncsu.edu/open-science-course/environments-docker-how.mp4>`_ (recording from the class, 40 mins)
* `Reproducible computational environments: About Docker isolation <http://fatra.cnr.ncsu.edu/open-science-course/environments-docker-isolation.mp4>`_ (recording from the class, 2 mins)

Slides
``````

* `Reproducible computational environments <../lectures/environments.html>`_

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

Running Jupyter Notebook through Docker (mandatory)
```````````````````````````````````````````````````

Get familiar with Jupyter Notebooks using the
instructions and links above. If needed, use one of the linked resources
above to learn about Jupyter.

Using the instructions above, install Docker on NCSU VCL Ubuntu
machine and run the notebook (from the instructions).
It is in fact collection of notebooks, so once you see them all in the
web browser, pick one (``buffers_cost_python.ipynb`` is a good one
to at least try out).

In the web browser, in the notebook itself, add a line stating that this
is your assignment and add you name. Then execute all cells
(*Cell > Run All*) and create a PDF document with the results.

There are two way to create PDF: Either from *File > Download as*
(one or two items will say PDF or pdf) or *File > Print Preview*
and then print to PDF. If this fails for you, do
*File > Download as > HTML*. Submit the resulting file to a Moodle
assignment for this topic.

If you want you can add any further comments about this to Moodle
assignment as text.


Installing Jupyter on your computer (optional)
``````````````````````````````````````````````

If you want to install Jupyter on your computer, you can,
although we are not using it in the course like that.
If you are already using Anaconda, use it to install Jupyter, otherwise
follow the instructions for each operating system.

Linux
+++++

Use system packages or pip packages, e.g. on Ubuntu::

    sudo apt install python-pip
    sudo pip install jupyter

Windows
+++++++

Install OSGeo4W, then run OSGeo4W Shell as administrator. There, update
pip first::

    pip install -U pip

Then update setuptools::

    pip install -U setuptools

Then install Jupyter::

    pip install Jupyter

macOS
+++++

Since we will be using Jupyter with GRASS GIS, run GRASS GIS first
to be sure you will use Python which GRASS GIS uses.

Then in the GRASS GIS terminal run::

    pip install -U pip
    sudo pip install jupyter

Alternatively, if the above does not work, you can try Homebrew.
Use it to install Jupyter::

    brew install jupyter