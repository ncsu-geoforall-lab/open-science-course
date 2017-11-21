Reproducible computational environments
=======================================



Docker
------

Official Docker website: https://www.docker.com/

Docker is open source under Apache 2.0 license but some additional
components and tools are under different licenses including proprietary
ones.

Installing Docker
`````````````````

For this week we will need to install Docker. Here are instructions for different operating systems. The version you need to install for MS Windows and Mac OS is called Docker Toolbox. On Ubuntu, the package is currently called docker.io.

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

Slides
``````

* `Lecture slides <../lectures/environments.html>`_ [main resource]

Videos
``````

* `Reproducible computational environments: Overview of tools <http://fatra.cnr.ncsu.edu/open-science-course/environments-intro.mp4>`_ (recording from the class, 24 mins)
* `Reproducible computational environments: Docker <http://fatra.cnr.ncsu.edu/open-science-course/environments-docker.mp4>`_ (recording from the class, 20 mins)
* `Reproducible computational environments: How to use Docker <http://fatra.cnr.ncsu.edu/open-science-course/environments-docker-how.mp4>`_ (recording from the class, 40 mins)
* `Reproducible computational environments: About Docker isolation <http://fatra.cnr.ncsu.edu/open-science-course/environments-docker-isolation.mp4>`_ (recording from the class, 2 mins)
* `Docker Tutorial - What is Docker & Docker Containers, Images, etc? <https://www.youtube.com/watch?v=pGYAg7TMmp0>`_ (by LearnCode.academy, 8 mins)
* `Introduction to Docker <https://www.youtube.com/watch?v=Q5POuMHxW-0>`_ (by Solomon Hykes at Twitter University, 47 mins)

References
``````````

* Boettiger, C. (2015). An introduction to Docker for reproducible research. ACM SIGOPS Operating Systems Review, 49(1), 71-79.

Assignment
----------

See the lecture (slides or videos), install Docker (see above) and run
a Jupyter Notebook inside a Docker container based on this repository:

https://github.com/wenzeslaus/Notebook-for-processing-point-clouds-in-GRASS-GIS

See the instructions above or in the repository readme file on how to
run the notebook. Report on how that went and if you were able to run
the whole notebook. The notebook has a section called Bonus tasks,
skip that. You can run the Python or the Bash notebook or both.
