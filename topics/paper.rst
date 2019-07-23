Writing and reproducing an open science paper
=============================================

Components of a reproducible paper
----------------------------------

Based on overview from Buckheit and Donoho 1995, Peng 2011,
Rodríguez-Sánchez et al. 2016, and Marwick 2016:

* text: textual (natural language) document describing the research
* data: values of all variables (both original data and results)
* code: machine readable instructions to get results from original data
* versions: differences and updates of all versions over time

Based on lectures in this course:

* text: background, methods, results, discussion, conclusion (PDF, HTML)
* data: included directory or as links to established repositories (plain text, open formats)
* specific code: scripts to perform analysis (Python, R, Bash, ...)
* reusable code: methods as a general software or part of larger project (GRASS GIS, R, ...)
* environment: details about all dependencies and the code (Docker, Vagrant, ...)
* versions: revision control system and repository (Git, Subversion, ...)

For example, Buckheit and Donoho 1995 referring to Jon Claerbout of
Stanford say about the importance of text versus code and environment
the following:

    An article about computational science in a scientific publication
    is not the scholarship itself, it is merely advertising of the scholarship.
    The actual scholarship is the complete software development environment
    and the complete set of instructions which generated the figures.

Resources
---------

Slides
``````

* `Reproducible paper <../lectures/paper.html>`_

Videos
``````

* `A reproducible paper: Overview of tools <http://fatra.cnr.ncsu.edu/open-science-course/paper-overview.mp4>`_ (recording from the class, 13 mins)
* `A reproducible paper: Evaluating the tools in context of various open science concepts <http://fatra.cnr.ncsu.edu/open-science-course/paper-terms-and-evaluation.mp4>`_ (recording from the class, 15 mins)

References
``````````

* J. Buckheit and D. L. Donoho. Wavelets and Statistics, chapter Wavelab and reproducible research. Springer-Verlag, Berlin, New York, 1995.
* Peng, R. D. (2011). Reproducible research in computational science. Science, 334(6060), 1226-1227. DOI: 10.1126/science.1213847
* Rodríguez-Sánchez, F., Bartomeus, I., Varela, S., Pérez-Luque, A.J., Ciencia reproducible: qué, por qué, cómo. Ecosistemas [en linea] 2016, 25 (Mayo-Agosto) [Fecha de consulta: 4 de abril de 2017] Disponible en:<http://www.redalyc.org/articulo.oa?id=54046745011> ISSN 1132-6344
* Marwick, B. (2016). Computational reproducibility in archaeological research: basic principles and a case study of their implementation. Journal of Archaeological Method and Theory, 1-27. DOI: 10.1007/s10816-015-9272-9

Assignment
----------

Try to reproduce figures from the following paper:

* https://doi.org/10.1186/s40965-017-0021-8

Report on how that went and how far did you get.
Based on the last lecture, identify what may prevent others from
reproducing the results of this paper and based on the whole class,
identify what may prevent others from reusing methods and code presented
in the paper. Consider how that may work in the future and consider
also different potential audiences.

As you have surely noticed, there are no instructions here on how to
reproduce the above paper. The paper itself gives instructions on how
to do that. Hint: Don't read the whole paper, but look for the tools,
platforms or any reproducibility-related information you
would expect based on what you learned. More than one way of
reproducing is provided, but one way is much simpler than the others.
