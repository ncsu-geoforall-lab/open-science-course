Introduction to command line
============================

This topic is an introduction to command line and remote access to
computational resources using GNU/Linux operating system.

Refer to the assignment instructions for instructions where to run
the commands.

Basics commands
---------------

Find which directory you are in::

    pwd

Go the the root directory
(i.e., the directory at the top of the directory tree)::

    cd /

See what is there::

    ls

Go back to your home directory
(``~`` is automatically replaced by your home directory path)::

    cd ~

Edit a file with *nano* (a common default command line editor)::

    nano test1.txt

Write some text. Put the word "apple" on couple of lines together with other text
and make couple of lines with other text without the word "apple."
To exit nano, press Ctrl+X, then
press Y to confirm that you want to save the file, and then Enter to
confirm the file name.

Now list the files in the current directory (you should see the file
you just created)::

    ls

To display its content in the command line, you can use *cat*::

    cat test1.txt

For browsing content of a larger file, use *less*::

    less test1.txt

Search content of a file
````````````````````````

Using *grep*, search for a line which contains ``apple`` in the file
called ``test1.txt``::

    grep apple test1.txt

Spaces in the command line
``````````````````````````

Spaces in the command line separate individual parameters
passed to the program. First item in the command line is
the name of the program (or full path to it).
Here we call the program called *echo* with one parameter
which is ``Hello``::

    echo Hello

We will use this program *echo* as an example.
It prints its parameters in the way that the parameters in
the output are separated by spaces.
Given that multiple spaces still are just separating two
parameters from each other, the following will print the same:

    echo Hello World
    echo Hello       World

If you want to pass spaces as part
of the parameter, use quotes::

    echo "Hello       World!"
    echo "Hello
    World!"

Confusion with cat
``````````````````

When you run ``cat`` without any parameters, you get into a strange
situation::

    cat

To get out of it, use Ctrl+D to end the input
(which will consequently end ``cat``)
or Ctrl+C to terminate ``cat``.
These shortcuts will work similarly with other programs
as well.


Redirecting inputs and outputs
------------------------------

Here the output of *cat* goes to the terminal::

    cat test1.txt

Here the output is redirected to a file::

    cat test1.txt > test3.txt

The output file is identical with what we read, that's not that useful
(since we just could use ``cp test1.txt test3.txt`` to create a copy)::

    cat test3.txt

When it starts to be useful, is when we pipe (redirect) the output
to input of another command, here *grep*, before redirecting it to a file::

    cat test1.txt | grep apple > test3.txt
    cat test3.txt

Let's get just the lines which don't contain "apple" using
the ``-v`` option::

    cat test1.txt | grep -v apple
    cat test1.txt | grep -v apple > test3.txt
    cat test3.txt

Similarly to redirection to a file, we can do redirection from a file
to command input::

    grep apple test1.txt
    grep apple < test1.txt

Both input and output can be redirected (connected) to files at the same time::

    grep apple < test1.txt > test3.txt
    cat test3.txt

Now, the *cat* command we were using can also concatenate
multiple files together::

    cat test1.txt test2.txt

The result can be redirected to another command::

    cat test1.txt test2.txt | grep apple

And then redirected to another file::

    cat test1.txt test2.txt | grep apple > test5.txt

Filtering program outputs
-------------------------

The *find* command is good for searching all files matching a pattern,
here we search for all files in the directory ``/bin`` which start with
letter ``z``::

    find /bin -name "z*"

There is couple of programs which have "grep" in their name, we can
filter then out and leave the rest. First see how our filter works::

    find /bin -name "z*" | grep grep

Then tell *grep* to leave them out using the ``-v`` option::

    find /bin -name "z*" | grep -v grep

Now we can use *wc* to count lines, words, and characters in this
output::

    find /bin/ -name "z*" | grep -v grep | wc

To get just the number of lines, we can use ``-l`` option::

    find /bin/ -name "z*" | grep -v grep | wc -l

Here is how we can use *find* to search for all files with particular
extension in our home directory::

    find ~ -name "*.txt"

As a side note,
the *find* command is different to *ls* which we often also use with
pattern, but the pattern is not in quotes and is evaluated by the
command line (shell) itself rather than the *ls* program::

    ls /bin/z*

Pausing execution
-----------------

Sometimes, examples are one of the cases, it is good to pause
execution of a script for some time. Try the *sleep* command
in command line::

    sleep 5

Running program in the background
---------------------------------

So far all commands we were running were blocking the command line
and we needed to wait for them to finish::

    sleep 10

If we want to run a long-running program in the background, we can use
ampersand at the end of the line::

    sleep 10 &

This also works in the scripts enabling parallel processing. In that
case you may find *wait* command to be useful for waiting for all
processes to finish.

Ampersand is also useful when running GUI applications from the command
line::

    gedit
    gedit &


Parallel processing
-------------------

In this section, we will execute multiple commands in parallel
which will allow us to take advantage of multiple CPU cores
(processing elements).

Getting ready
`````````````

First we need to prepare a text file with commands to run::

    nano test2.txt

Use the following as the content of the file. The following lines
are spending some time in a program called *sleep* and then
printing a number using *echo*. These are just for the exercise.
In reality, each line would be, e.g., a call of
a Python script doing some useful computation::

    sleep 10 && echo 1;
    sleep 25 && echo 2;
    sleep 10 && echo 3;
    sleep 25 && echo 4;
    sleep 20 && echo 5;
    sleep 10 && echo 6;
    sleep 10 && echo 7;
    sleep 10 && echo 8;


Installing a program
````````````````````

When we run the program GNU Parallel, systems informs us that we don't
have it::

    parallel

On Ubuntu and similar distributions, we can install it using
``apt install``::

    apt install parallel

However, only administrator (aka super user or root) can install new
programs. We can execute program in that way using *sudo*::

    sudo apt install parallel

Exploring the documentation
```````````````````````````

Now when we have the program, we can get suggestion how to use it
using ``--help`` option::

    parallel --help

A more detailed documentation is in the manual (exit by pressing Q)::

    man parallel

Running in parallel
```````````````````

Now run the commands from the text file in parallel::

    parallel -j 2 -a test2.txt

The ``-j`` option specifies the number of jobs (commands) to execute
in parallel at the same time and the ``-a`` option specifies the
file with the commands to execute.

Observe how long it takes to execute the following commands::

    time parallel -j 1 -a test2.txt
    time parallel -j 2 -a test2.txt
    time parallel -j 4 -a test2.txt
    time parallel -j 8 -a test2.txt

When doing actual processing, how much you gain by increasing number of
jobs depends on how many core you actually have available on your
machine.


Remote access using SSH
-----------------------

Although different remote desktop solutions are quite common,
it is even more common to connect to servers and remote computational
resources, such as high performance computing clusters, using SSH.
The whole operation is done in command line and all further interaction
happens in command line as well. You would typically see that the
command line prompt changed to indicate that the terminal is now
connected to a different machine.

::

    ssh anndoe@154.2.15.319 -X

The ``-X`` option is useful for servers which support applications with
GUI, specifically servers with X server, and clients which support this
type of connection (most of Linux distributions support that
and on macOS it is possible to get it working reasonably well while
on MS Windows it is harder to get that). When ``-X`` is used, GUI
applications can be started from command line and the GUI appears
on the client side similarly to the applications running on the client.


Bonus: Changing the path variable
---------------------------------

This is how path variable can be changed to enable a program installed
in non-standard location in the command line for the given session
(the following expects Ubuntu 16.04).

The first command should work, the second should fail.

::

    ls
    sl

We install the missing program::

    sudo apt-get install sl

The following should still fail because this not-so-standard
program is not "on path". It was installed to ``/usr/games``.

    sl

We inspect the ``PATH`` variable if ``/usr/games`` is
really not there::

    echo $PATH

And we add the path to the ``PATH`` variable.
First we use *echo* to inspect how our command will look
like and then we actually run it::

    echo export PATH="/usr/games:$PATH"
    export PATH="/usr/games:$PATH"

Finally, we run our newly installed command::

    sl

If you see train, all went well.

Note that this changes the ``PATH`` variable only temporarily
in the given terminal session which is usually what you should
do (limit yourself to).


Resources
---------

* `Introduction to the Linux Operating System <https://www.guru99.com/introduction-linux.html>`_ from Guru99
* `The Linux Information Project <http://www.linfo.org/>`_
* `Unix—the Bare Minimum <http://heather.cs.ucdavis.edu/~matloff/UnixAndC/Unix/UnixBareMn.pdf>`_ by Norman Matloff
* `Introduction to Linux <http://tille.garrels.be/training/tldp/>`_ by Machtelt Garrels
* `An Introduction to Linux Basics <https://www.digitalocean.com/community/tutorials/an-introduction-to-linux-basics>`_ at DigitalOcean
* `UNIX Tutorial for Beginners <http://www.ee.surrey.ac.uk/Teaching/Unix/>`_ by M. Stonebank
* `Piping and Redirection! <https://ryanstutorials.net/linuxtutorial/piping.php>`_ By Ryan Chadwick
* `What do 'real', 'user' and 'sys' mean in the output of time(1)? <https://stackoverflow.com/questions/556405/what-do-real-user-and-sys-mean-in-the-output-of-time1>`_

Videos
``````

* `Basic commands <http://fatra.cnr.ncsu.edu/open-science-course/linux-pwd-cd-cat-less.mp4>`_ (recording from the class, 14min)
* `Using Tab key <http://fatra.cnr.ncsu.edu/open-science-course/linux-tab-key.mp4>`_ (recording from the class, 1.5min)
* `World Without Linux Final Episode #6 Free Burger <https://www.youtube.com/watch?v=fvPSNK8iB0Y>`_ (many Linux-related terms in under 3 minutes)

Assignment
----------

Go through the above instructions. You can use NCSU VCL, specifically
one of the Ubuntu machines. When you login in into the machine, use
terminal to input commands. Alternatively, you can use terminal on Mac
OS or Git Bash from the last class if you are using MS Windows but you
may not be able to do all the steps. If you were in the class, you can
skip this part and do the next one right away.

In some Linux command line (e.g. in NCSU VCL Ubuntu machine), find out
how many CPUs has the machine you are working on. To find out that
information, use file called ``/proc/cpuinfo`` which contains
information about CPUs. Construct command line which will in one
command print the number of CPUs, but nothing more. Post the command as
a (online) text as assignment in Moodle.

Please do post questions to the forum as you are going through the
provided material, just don't post possible solutions for that CPU
command, so that others can come up with their own solutions.
