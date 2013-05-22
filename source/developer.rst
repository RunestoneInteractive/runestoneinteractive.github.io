Developer Documentation for Runestone Interactive Tools
=======================================================

Content Authors
---------------

The runestone system uses restructuredText as its primary markup language.  restructuredText is easy to read in plain text form, and can be transformed into html, latex, epub, or our own interactive book format.

Its probably easiest to get started by simply checking out the runestone repository, and then starting your project as a subdirectory.  Here are the relevant pieces from the README on github.

Dependencies
~~~~~~~~~~~~

There are a couple of prerequisites you need to satisfy before you
can build and use this eBook.

First get Sphinx, Version 1.1.x is current as of this writing.

http://sphinx.pocoo.org

Follow the instructions there to download and install Sphinx.

Next install paver, version 1.2.0 is current as of this writing.  If you have ``pip`` installed its as easy as ``pip install paver`` if not, then follow the instructions `On the paver github page <http://paver.github.com/paver/#installation>`_

Once paver is installed you will also need to install sphincontrib-paverutils, again the easiest route is to use ``pip install sphinxcontrib-paverutils``

.. admonition:: Warning

   paver-1.2 introduced some backward incompatibilities.  These have not yet been fixed in the official paverutils repository but you can grab my fixed version and build it using the ``python setup.py install`` method. Download `my fixed version <../_static/sphinxcontrib-paverutils-1.4.1.tar>`_  Untar the download file, change into the sphinxcontrib-paverutils-1.4 folder and run the setup command.
   

If you want to run a full blown server -- so you can save activecode assignments etc. then you will need to download and install web2py.  http://web2py.com

After you install web2py go to the applications folder and check out this repository.  This will be installed as a web2py application automatically.

Cloning The Runestone Project and its submodules
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This project consists of the main repository, plus *submodules* for codelens, parsons-problems, and skulpt.  In order to get all of the source you need you will need to do the following:

::

    $ git clone https://github.com/bnmnetp/runestone.git
    $ cd runestone
    $ git submodule init
    $ git submodule update

If you are using a GUI git client you may simply get prompted to update the submodules and all will be taken care of for you.  Newer versions of git also support::

    $ git clone --recursive https://github.com/bnmnetp/runestone.git


Building the prexisting Books
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Once you the above installed, you can type ``paver allbooks`` from the command
line and that will build the following targets:

* How to Think Like a Computer Scientist
* Problem Solving with algorithms and Data Structures using Python
* A development version of everything combined (devcourse)


You can quickly check the build by opening the file static/devcourse/index.html in your browser.


Starting a Document
~~~~~~~~~~~~~~~~~~~

You can start a new document using the sphinx-quickstart command.  Choose a folder other than the generic source folder to contain your own document.

Using Runestone Extensions
--------------------------

Video
~~~~~

The video directive is perhaps the easiest, so I'll start by describing that one.  As you may imagine, the job of the video directive is to include a video in the final product.  Here is what it looks like in restructuredText.

**Example**

::

    .. video:: list_unique
       :controls:
       :thumb: ../_static/videothumb.png

       http://media.interactivepython.org/pythondsVideos/list_unique.mov
       http://media.interactivepython.org/pythondsVideos/list_unique.webm

**Description**

All directives start out with ``..`` followed by the name of the directive, in this case ``video::``  Any required arguments follow after the ``::``.

**Required Arguments**

The video directive has one required argument which is a unique identifier for the video. This is for logging purposes, as well as a Javascript necessity for managing the thumbnail and controls.

**Optional Arguments**

There are two optional arguments to the video directive.

``:controls:``  The controls argument is a flag that if present tells sphinx to generate the usual set of video controls, play, pause, rewind, fast forward. If not present the video will automatically play when the page is loaded.

``:thumb:`` references an image that will serve as the thumbnail for this video. If this parameter is used, then a thumbnail image will take the place of the video on the page until the reader clicks on the thumbnail.  clicking on the thumbnail will cause the full video to appear at full size.   If the ``:thumb:`` directive is not present then the video will appear on the page in its full size.


**Content**

The content lines of the video directive let you specify as many video sources as you need.  Usually I specify two videos, one in mov format and the other in webm format.  This seems to cover all the browsers.


To give you an idea of what happens when sphinx processes a video directive here is the html and javascript output:

::

    <a id="list_unique_thumb" > <img src="../_static/videothumb.png" /></a>
    <div id="list_unique" class="video_popup" >
    <video controls  >
        <source src="http://knuth.luther.edu/~pythonworks/pythondsVideos/list_unique.mov" type="video/mp4"></source>
        <source src="http://knuth.luther.edu/~pythonworks/pythondsVideos/list_unique.webm" type="video/webm"></source>
        No supported video types
    </video>
    </div>
    <script>
       jQuery(function($) {
          $('#list_unique_thumb').click(function(e) {
             $('#list_unique').show();
             $('#list_unique_thumb').hide();
             logBookEvent({'event':'video','act':'play','div_id': 'list_unique'});
             // Log the run event
          });
       });
    </script>

**TODO**

* embed Vimeo
* embed youtube


Activecode
~~~~~~~~~~

The activecode directive allows you to create executable example code.  Not only is the code executable, so you know your examples will be syntactically correct, but it is also editable which allows your students to experiment with your examples by changing them and running them over and over again.

**Example**

::

    .. activecode:: ac_example1
       :nopre:
       :nocanvas:
       :caption: This is my caption
       :include: activecode_id, [activecode_id,...]

       for i in range(10):
           print('hello world %d\n' % i)



**Description**

The activecode directive creates a runnable python listing.  It looks like this:

.. activecode:: ac_example1
   :caption: This is my caption

   import turtle
   t = turtle.Turtle()

   for i in range(4):
       t.forward(100)
       t.left(90)


The most important thing to remember about an activecode example is that it is running in the browser.  There is no need to connect to a server to even be online for these examples to work.  The activecode directive makes use of a Skulpt (www.skulpt.org).  Skulpt is an open source javascript implementation of Python.

Normally and output from a print statment is appended to a ``<pre></pre>`` element in the page.  Graphical output, such as the turtle graphics program in the example, is done on a ``<canvas>``.

**Arguments**

The identifier after the ``:: `` must be unique.


**Optional Arguments**

``:nopre:``  -- This flag prevents a ``<pre></pre>`` element from getting created.

``:nocanvas:``  -- This flag prevents a ``<canvas>`` element from getting created.

``:caption:``  The text argument to this parameter is formatted as a caption, underneath the activecode block

``:include:``  This option allows you to pre-prend other clode blocks.  It is nice because it allows you to write individual activecode examples that build on each other without having to duplicate all the code and force the user to scroll through the code to find the newly introduced content.


Codelens
~~~~~~~~


The codelens directive creates an interactive environment for you to step through small code examples.  codelens displays the values of variables and shows the contents and links between your objects.  Unlinke a normal debugger, codelens lets you step forward and backward through the code.

The way codelens works is that when the book is built, it takes the code and runs it through the python debugger where a series of stack frames are collected.  I will refer to this list of stack frames as the trace data.  The trace data is then embedded into the page, so when a student is reading the book and wants to step through a codelens example the trace data is visualized for the student.

In addition to stepping through the code you as an author can embed a question into the example.  You may ask the student to predict how the value of a variable will change, or you may ask the student to predict which line of code will be executed next.  This is an excellent way to help students develop a good mental model of how python works.

It is worth noting that you can also make use of codelens in a live environment where you can edit code and run new examples.  To use codelens interactively go here:  http://www.pythontutor.com/


**Example**

::

    .. codelens:: secondexample

        fruit = ["apple","orange","banana","cherry"]
        numlist = [6,7]
        newlist = fruit + numlist
        zeros = [0] * 4

        zeros[1] = fruit
        zeros[1][2] = numlist

**Description**

Here is an example of codelens in action:

.. codelens:: secondexample

    fruit = ["apple","orange","banana","cherry"]
    numlist = [6,7]
    newlist = fruit + numlist
    zeros = [0] * 4

    zeros[1] = fruit
    zeros[1][2] = numlist


**Arguments**

The identifier after the ``:: `` must be unique.

**Optional Arguments**

``:tracedata:``  Normally this value is filled in automatically, but you can provide your own tracedata if you wish.

``:caption:``  The text provided for this option will be formatted as a caption on the bottom of the page.

``:showoutput:``  Sometimes it is desireable to ignore any output from print statements.  Or sometimes you just want to save space and not show output.

``:question:``  This is the question text that will be shown to the student.

``:correct:`` This is the correct answer.  This should be specified as a value from the trace data.  for example in the example above you might ask the student for the value of numlist[0].  The correct answer would be specified as globals.numlist[0]

``:feedback:``  If the student gives the wrong answer you can give them a few sentences of feedback.

``:breakline:``  This is the line that you want the program to stop at and ask show the question.


Datafile
~~~~~~~~

The datafile directive works with activecode when you want to have the user read some data from a file.  Because we want the file to come from the browser, not some far away server, or from the users local hard drive we can fake files in two different ways.

1.  We can put the data into ``pre`` element.  The id on the element serves as the filename.

2.  We can put the data into a ``textarea`` element.  Again the id on the element serves as the file name.  However with a text area the file data can be modified.

**Example**

::

    .. datafile:: mydata.dat
       :edit:
       :rows: 20
       :cols: 60

       data line one
       data line two
       data line three

The example will produce a text area that is 20 rows long and 60 columns wide.  The ``:edit:`` flag tells the directive to produce a textarea rather than a pre element.

**Arguments**

The required argument is the 'filename'  In the example it is mydata.dat  This must be unique within the document as it does become the id of the element.

**Optional Arguments**

``:hide:``  -- This makes the file invisible.  This might be good if you have an exceptionally long file that you want to use in an example where its not important that the student see all the data.

``:edit:``  -- This flag makes the file into an editable file in a textarea. This is great if you want your students to be able run their program on different data from a file.  All they have to do is edit the textarea and rerun the program.

``rows``  -- This is for sizing the textarea.  The value has no effect on a pre element.  If the rows value is not provided the directive will do its best to guess the number of rows within a reasonable number.

``cols``  -- Again this is for sizing the text area, and again if not provided the directive will come up with a reasonable value.

Assessments
~~~~~~~~~~~

**Description**

Assessment questions come in several forms.  Single answer multiple choice, multi-answer multiple choice, fill in the blank, parson's problems for coding, and some code tracing prediction tasks.  For example, given some code, the student can step through the code line by line until the system asks them to predict the value of a variable, or to predict the next line that will be executed.

The directives are as follows:

::

    .. mchoicemf
    .. mchoicema
    .. fillintheblank
    .. parsonsprob


**Multiple Choice with Multiple Feedbacks**

**Example**

::

    .. mchoicemf:: question1_1
       :answer_a: Python
       :answer_b: Java
       :answer_c: C
       :answer_d: ML
       :correct: a
       :feedback_a: Yes, Python is a great language to learn, whether you are a beginner or an experienced programmer.
       :feedback_b: Java is a good object oriented language but it has some details that make it hard for the beginner.
       :feedback_c: C is an imperative programming language that has been around for a long time, but it is not the one that we use.
       :feedback_d: No, ML is a functional programming language.  You can use Python to write functional programs as well.

       What programming language does this site help you to learn?

**Description**

.. mchoicemf:: question1_1
   :answer_a: Python
   :answer_b: Java
   :answer_c: C
   :answer_d: ML
   :correct: a
   :feedback_a: Yes, Python is a great language to learn, whether you are a beginner or an experienced programmer.
   :feedback_b: Java is a good object oriented language but it has some details that make it hard for the beginner.
   :feedback_c: C is an imperative programming language that has been around for a long time, but it is not the one that we use.
   :feedback_d: No, ML is a functional programming language.  You can use Python to write functional programs as well.

   What programming language does this site help you to learn?

**Arguments**

**Optional Arguments**

``:answer_a:``, ``:answer_b:``, ``:answer_c:``, ``:answer_d:``, ``:answer_e:``  You can provide up to five different possible correct answers.

``:correct:``  The single correct answer

``:feedback_a:``, ``:feedback_b:``, ``:feedback_c:``, ``:feedback_d:``, ``:feedback_e:``  Each answer can have its own feedback.

``:iscode:``  Tells the directive processor that the question text should be treated as code.


**Multiple Choice Multiple Answer**

This next type of question allows more than one correct answer to be required.  The feedback will tell you whether you have the
correct number as well as the feedback for each.


.. mchoicema:: question1_2
   :answer_a: red
   :answer_b: yellow
   :answer_c: black
   :answer_d: green
   :correct: a,b,d
   :feedback_a: Red is a definitely on of the colors.
   :feedback_b: Yes, yellow is correct.
   :feedback_c: Remember the acronym...ROY G BIV.  B stands for blue.
   :feedback_d: Yes, green is one of the colors.

   Which colors might be found in a rainbow? (choose all that are correct)

**Optional Arguments**

``:answer_a:``, ``:answer_b:``, ``:answer_c:``, ``:answer_d:``, ``:answer_e:``  You can provide up to five different possible correct answers.

``:correct:``  a comma separated list of the correct answers

``:feedback_a:``, ``:feedback_b:``, ``:feedback_c:``, ``:feedback_d:``, ``:feedback_e:``  Each answer can have its own feedback.

``:iscode:``  Tells the directive processor that the question text should be treated as code.


**Fill in the Blank, or Free form Answer**

Another type of question allows you as the instructor to ask for a value.  You can test for the value using Javascript regular expressions.  For example:

::

    .. fillintheblank:: postfix1
       :casei:
       :correct: \\b10\\s+3\\s+5\\s*\\*\\s*16\\s+4\\s*-\\s*/\\s*\\+
       :feedback1:  ('10.*3.*5.*16.*4', 'The numbers appear to be in the correct order check your operators')
       :feedback2: ('.*', 'Remember the numbers will be in the same order as the original equation')

       Without using the activecode infixToPostfix function, convert the following expression to postfix <br> 10 + 3 * 5 / (16 - 4) ___

**Description**

Here is how the fill in the blank question is formatted.

   .. fillintheblank:: postfix1
      :casei:
      :correct: \\b10\\s+3\\s+5\\s*\\*\\s*16\\s+4\\s*-\\s*/\\s*\\+
      :feedback1:  ('10.*3.*5.*16.*4', 'The numbers appear to be in the correct order check your operators')
      :feedback2: ('.*', 'Remember the numbers will be in the same order as the original equation')

      Without using the activecode infixToPostfix function, convert the following expression to postfix <br> 10 + 3 * 5 / (16 - 4) ___


**Optional Arguments**

``:iscode:``  Tells the processor that the question text is code.

``:correct:``  A regular expression matching the correct answer
``:feedback1:`` (re,text)  a regular expression matching an incorrect answer with feedback specific to that answer.
``:feedback2:``
``:casei:``  Tells the regular expression match to match using a case insensitive match.


**Parson's Problems**

And finally here is a way of giving your students some simple programming problems where the code is already there for them but not indented or in the correct order.  Use drag-and-drop to get everthing right.



**Example**

Here is a simple example:

::

    .. parsonsprob:: question1_100_4

       Construct a block of code that correctly implements the accumulator pattern.
       -----
       x = 0
       for i in range(10)
          x = x + 1

You can also group lines of code together using === to delimit the different blocks.
::

    .. parsonsprob:: question1_100_5

       Solve this problem.
       -----
       def findmax(alist):
       =====
          if len(alist) == 0:
             return None
       =====
          curmax = alist[0]
          for item in alist:
       =====
             if item &gt; curmax:
       =====
                curmax = item
       =====
          return curmax


Notice that you give the code correctly indented and in its correct form.  This is how the processor knows what the correct answer is.  The processor will scramble the code for you each time the page is loaded.  Here is what the parson's problem looks like:

.. parsonsprob:: question1_100_5

   Solve this problem.
   -----
   def findmax(alist):
   =====
      if len(alist) == 0:
         return None
   =====
      curmax = alist[0]
      for item in alist:
   =====
         if item &gt; curmax:
   =====
            curmax = item
   =====
      return curmax



**Optional Arguments**

There are no optional arguments for the parson's problem directive.



Disqus Comment Box
------------------

**Example**

Here is an example:

::

    .. disqus::
        :shortname: interactivepython
        :identifier: overview.html


**Description**
Insert an interactive comment/discussion box, powered by Disqus. Requires registration with Disqus.

**Arguments**
There are 2 required arguments, ``shortname`` and ``identifier``. The shortname is used to identify your site to 
Disqus. You can obtain a shortname by registering with Disqus. The identifier is used to identify the specific pageon your site you want users to be able to comment on.


.. raw:: html

    <script type="text/javascript" charset="utf-8">
        $(document).ready(createEditors);
    </script>
