Reproducible computational environments
=======================================



Official Docker website: https://www.docker.com/



Build an image using content of a GitHub repository::

    docker build github.com/wenzeslaus/Notebook-for-processing-point-clouds-in-GRASS-GIS -t pointcloud-nb

Now run a container based on the newly created image::

    docker run -p 8888:8888 pointcloud-nb


Resources
---------

Slides
``````

* `Lecture slides <../lectures/environments.html>`_ [main resource]

Videos
``````

* `Docker Tutorial - What is Docker & Docker Containers, Images, etc? <https://www.youtube.com/watch?v=pGYAg7TMmp0>`_ (by LearnCode.academy, 8 mins)
* `Introduction to Docker <https://www.youtube.com/watch?v=Q5POuMHxW-0>`_ (by Solomon Hykes at Twitter University, 47 mins)

References
``````````

* Boettiger, C. (2015). An introduction to Docker for reproducible research. ACM SIGOPS Operating Systems Review, 49(1), 71-79.

Assignment
----------

Install Docker and run a Jupyter Notebook inside a Docker container
based on this repository:

https://github.com/wenzeslaus/Notebook-for-processing-point-clouds-in-GRASS-GIS

See the instructions above or in the repository readme.
