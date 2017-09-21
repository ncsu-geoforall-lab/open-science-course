Introduction to command line
============================

This topic is an introduction to command line and remote access to
computational resources using GNU/Linux operating system.

Basic commands
--------------

::

    pwd
    cd /
    ls
    cd ~
    nano test1.txt
    ls
    cat test1.txt
    less test1.txt

Search content of a file
````````````````````````
::

    grep line test1.txt

Spaces in the command line
``````````````````````````

::

    echo Hello
    echo Hello World!
    echo Hello       World!
    echo "Hello       World!"
    echo "
    "

Confusion with cat
``````````````````

::

    cat

Parallel processing
-------------------

Editing with nano
`````````````````

::

    nano test2.txt


Installing a program
````````````````````

::

    parallel
    apt-get install parallel
    sudo apt-get install parallel

Exploring the documentation
```````````````````````````

::

    parallel --help
    parallel --license
    man parallel

Running in parallel
```````````````````

::

    parallel -j 2 -a test2.txt

::

    time parallel -j 1 -a test2.txt
    time parallel -j 2 -a test2.txt
    time parallel -j 4 -a test2.txt

Redirecting inputs and outputs
------------------------------

::

    cat test1.txt
    cat test1.txt > test3.txt
    cat test3.txt
    cat test1.txt | grep line > test3.txt
    cat test3.txt
    cat test1.txt | grep -v line > test3.txt
    cat test3.txt
    grep line test1.txt
    grep line < test1.txt
    cat test1.txt test2.txt
    nano test1.txt
    cat test1.txt test2.txt
    nano test1.txt
    cat test1.txt test2.txt | grep apple
    grep line test1.txt
    grep line < test1.txt
    grep line < test1.txt > test3.txt
    cat test3.txt
    ls /
    ls /bin/
    ls /bin/z*
    find / -name "z*"
    find /bin/ -name "z*"
    find /bin/ -name "z*" | grep grep
    find /bin/ -name "z*" | grep -v grep
    find /bin/ -name "z*" | grep -v grep > test3.txt
    less test3.txt
    less /bin/zgrep
    find /bin/ -name "*.txt"
    find ~ -name "*.txt"
    file /bin/zgrep
    find /bin/ -name "z*" | grep -v grep
    find /bin/ -name "z*" | grep -v grep | wc
    find /bin/ -name "z*" | grep -v grep | wc -l


Running program in the background
---------------------------------

::

    gedit
    gedit &

Pausing execution
`````````````````

::

    sleep 5

Remote access using SSH
-----------------------

::

    ssh vpetras@152.1.13.217 -X


Bonus: Changing the path variable
---------------------------------

::

    ls
    sl
    sudo apt-get install sl
    sl
    echo $PATH
    echo export PATH="/usr/games:$PATH"
    export PATH="/usr/games:$PATH"
    sl
    ls
    sl

Resources
---------

* `What do 'real', 'user' and 'sys' mean in the output of time(1)? <https://stackoverflow.com/questions/556405/what-do-real-user-and-sys-mean-in-the-output-of-time1>`_

Videos
``````

* `World Without Linux Final Episode #6 Free Burger <https://www.youtube.com/watch?v=fvPSNK8iB0Y>`_

Assignment
----------

Go through the above instructions. You can use NCSU VCL, one of the
Ubuntu machines. When you login in into the machine, use terminal
to input commands. Alternatively, you can use terminal on Mac OS or
Git Bash from last class if you are using MS Windows. If you were in the
class, you can skip this part and do the next one right away.

In some Linux command line, find out how many CPUs has the machine
you are working on. To find out that information, use file called
``/proc/cpuinfo`` which contains information about CPUs. Construct
command line which will in one command print the number of CPUs,
but nothing more.
