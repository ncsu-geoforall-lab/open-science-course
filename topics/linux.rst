Introduction to command line
============================

This topic is an introduction to command line and remote access to
computational resources using GNU/Linux operating system.

Basics commands
---------------

Find which directory you are in::

    pwd

Go the the root directory::

    cd /

See what is there::

    ls

Go back to your home directory::

    cd ~

Edit a file with nano::

    nano test1.txt

Write some text. Put the word "apple" on couple of lines and make couple
of lines without the word "apple." To exit nano, press Ctrl+X, then
press Y to confirm that you want to save the file, and then Enter to
confirm the file name.

Now list the files in the current directory (you should see the file
you just created)::

    ls

To display its content in the command line, you can use cat::

    cat test1.txt

For browsing content of a larger file, use less::

    less test1.txt

Search content of a file
````````````````````````

Usin grep, search for a line which contains ``apple`` in the file
called ``test1.txt``::

    grep apple test1.txt

Spaces in the command line
``````````````````````````

Spaces separate individual parameters. The command ``echo`` prints
its parameters separated by spaces. If you want to pass spaces as part
of the parameter, use quotes::

    echo Hello
    echo Hello World
    echo Hello       World
    echo "Hello       World!"
    echo "Hello
    World!"

Confusion with cat
``````````````````

When you run ``cat`` without any parameters, you get into a strange
situation::

    cat

To get out of it, use Ctrl+D to end the input (which ends ``cat``)
or Ctrl+C to terminate ``cat``.

Parallel processing
-------------------


First we need to prepare a text file with commands to run::

    nano test2.txt

Use the following as the content of the file. This is just for the
exercise. Each line would be, e.g. a call of a Python script which
does some computations::

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

When we run the program GNU Parallel, systems informs us that we don'
have it::

    parallel

On Ubuntu and similar distributions, we can install it using
``apt-get install``::

    apt-get install parallel

However, only administrator (aka super user or root) can install new
programs. We can execute program in that way using *sudo*::

    sudo apt-get install parallel

Exploring the documentation
```````````````````````````

Now when we have the program, we can get suggestion how to use it
using ``--help`` option::

    parallel --help

A more detailed documetation is in the manual (exit by pressing Q)::

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

When doing actual processing, how much you gain by increasing number of
jobs depends on how many CPUs you actually have available on your
machine.

Redirecting inputs and outputs
------------------------------

Here the output of *cat* goes to the terminal::

    cat test1.txt

Here the output is redirected to a file::

    cat test1.txt > test3.txt

The output file is identical with what we read, that's not that useful
(since we just could use ``cp test1.txt test3.txt`` to create a copy)::

    cat test3.txt

When it starts to be useful, is when we first pipe (redirect) the output
to input of another command, here *grep*::

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

Both input and output can be connected to files at the same time::

    grep apple < test1.txt > test3.txt
    cat test3.txt

The *cat* command can concatenate multiple files together::

    cat test1.txt test2.txt

The result can be redirected to another command::

    cat test1.txt test2.txt | grep apple

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

The *find* command is different to *ls* which we often also use with
pattern, but the pattern is not in quotes and is evaluated by the
command line (shell) itself rather than the *ls* program::

    ls /bin/z*

Pausing execution
`````````````````

Sometimes, an examples are one of the cases, it is good to pause
execution of a script for some time::

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


Remote access using SSH
-----------------------

Although different remote desktop solutions are quite common,
it is even more common to connect to servers and remote computational
resources, such as high performance computing clusters, using SSH.
The whole operation is done in command line and all further interaction
happens in command line as well (see how the command line prompt
changed)::

    ssh anndoe@154.2.15.319 -X

The ``-X`` option is useful for servers which support applications with
GUI, specifically servers with X server, and clients which support this
type of connection (most of Linux distributions support that while
on MS Windows it is harder to get that). When ``-X`` is used, GUI
applications can be started from command line and the GUI appears
on the client side similarly to the applications running on the client.


Bonus: Changing the path variable
---------------------------------

This is how path variable can be changed to enable a program installed
in non-standard location in the command line for the given session
(expects Ubuntu 16.04)::

    ls
    sl
    sudo apt-get install sl
    sl
    echo $PATH
    echo export PATH="/usr/games:$PATH"
    export PATH="/usr/games:$PATH"
    ls
    sl

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
