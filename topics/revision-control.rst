Revision control systems and wiki technologies
==============================================

Git
---

Git is a revision (version) control system.
Git is free and open source software:

    Git is released under the GNU General Public License version 2.0,
    which is an open source license. The Git project chose to use GPLv2
    to guarantee your freedom to share and change free software-to
    make sure the software is free for all its users.

Install Git on your computer. You can obtain the instructions and
download file on the official Git website:

https://git-scm.com/

Using Overleaf with Git
-----------------------

You will need some experimental document in Overleaf
(i.e. some document which is yours only and you can break it).
Go to this document and go to *Share* and use the *Clone With Git*
option. Use this in your local Git installation to clone the repository.
In command line, the operation looks like::

    git clone https://git.overleaf.com/somehash

Make some changes in the main TeX file (``main.tex``) using a text
editor. Now let's see the status of the repository::

    git status

This should show that one file was modified. Let's see what are the
changes::

    git diff

This showed the changes line by line. For text, it might be good to see
changes word by word::

    git diff --word-diff

After reviewing the changes, tell Git to record the current state
using ``git commit``. Specify also the message to describe the changes::

    git commit -am "a test change"

No let's put the these changes to Overleaf using::

    git push

Now check if you see the changes you made in Overleaf.
Then make some changes in Overleaf and get them synchronized to your
computer::

    git pull

Starting with repository on your computer
-----------------------------------------

Create a new empty directory and navigate your command line to it.
Then initialize a Git repository there::

    git init

Create a new plain text file using your text editor.
Put there few lines of text.
Once you created a new file, you have to tell Git to start tracking it::

    git add some_file.txt

To see what files where changed, added or deleted use::

    git status

Now commit the changes::

    git commit -am "a file with trivial content"

Now do some changes in the file; add some lines, remove some lines,
and edit some lines.
To review the changes in the files use::

    git diff

Now again commit the changes::

    git commit -am "a file with trivial content"

Let's review the states we have recorded::

    git log

The are GUIs for this, but depending on the occasion we may want to use
some command line parameters to get a differently formated revision tree
in the command line, for example::

    git log --oneline --graph --decorate --all

Branches in Git
---------------

So far we were working in a single branch called ``master``.
Now we will create a new branch. This can be done using
``git branch`` and then you would switch to the newly created branch
using ``git checkout``. Usually this is done together in one command::

    git checkout -b experiment

Now we have a branch called ``experiment`` and we are currently in it.
In other words, the ``experiment`` branch is active now.


Software licenses
-----------------

https://choosealicense.com/

Resources
---------

Texts
`````

* `Basic Git introduction <https://gist.github.com/wenzeslaus/2cb7dbc9cdbb4a3867a2>`_
* `Git and GitHub workshop <http://ncsu-geoforall-lab.github.io/git-and-github-workshop/>`_

Videos
``````

* `Git Tutorial for Beginners: Command-Line Fundamentals <https://www.youtube.com/watch?v=HVsySz-h9r4>`_ by Corey Schafer (2015)
* `Git & GitHub Crash Course For Beginners <https://www.youtube.com/watch?v=SWYqp7iY_Tchttps://www.youtube.com/watch?v=SWYqp7iY_Tc>`_ by Brad Traversy (2017)
* `Git & GitHub (intermixed) <https://www.youtube.com/playlist?list=PLWKjhJtqVAbkFiqHnNaxpOPhh9tSWMXIF>`_ by freeCodeCamp (playlist)

Documentation
`````````````

* `Git documentation <http://git-scm.com/doc>`_
* `Pro Git book <http://git-scm.com/book>`_
* `GitHub documentation <https://help.github.com>`_
* `Try Git online <https://try.github.io>`_

Assignment
----------

The assignment has four parts. First, install Git on your computer.

Second, go to your document in Overleaf
from the last assignment or create some other test document in Overleaf.
Go to *Share* and use the *Clone With Git* option. Use this in your
local Git installation to clone the repository. In command line,
the operation looks something like:

::

    git clone https://git.overleaf.com/somehash

Make some changes, commit, push, and see what happened in Overleaf.
Then make some changes in Overleaf and then pull in your desktop
installation. You can repeat that so you feel comfortable.

Third, create a repository on GitHub, GitLab, Bitbucket, or some other
Git service. The will be a guide, wizard, or form which will lead you
through it. Then clone the repository on your computer and do some
commits.
Again, you can repeat that so you feel comfortable.

Fourth, submit changes to some repository which is not yours.
For this we will use GitHub, but the workflow would be similar in other
cases as well. You can choose from two options how to do that. Different
projects prefer one or the other. We will use the following repository
as the repository we are trying to submit changes to.

URL to be added

You can submit a patch (aka diff) as a file.

You can submit a pull request.
