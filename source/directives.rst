Directives Documentation for Runestone .rst files
=================================================

Each Runestone directive has a particular purpose. Each is detailed below, including:

* What each directive allows you to create
* The syntax for using each directive
* Examples, or links to examples, of how instructors have used these directives in interactive textbook work
* If applicable, how exercises created by these directives can be graded
* Available additional developer documentation that explains how interaction with these directives in an interactive textbook are logged


General Syntax
---------------

All directives start out with ``..`` followed by the name of the directive (e.g. ``video``, as seen below), and then ``::``.

Directives may have **required arguments**. In many cases, an argument that is a unique identifier for that particular directive's ``div`` id, will follow the ``::`` in the directive (example below). 

Further (often optional) additions generally occur below that first line, surrounded by single ``:``s. Some of those require parameters -- for example, the ``:thumb:`` addition for the ``video`` directive  requires a path to a ``.png`` image for the thumbnail image that should appear for the video, which you can see in the video directive **Example in reStructured Text**.


Directives
----------

Video
~~~~~

**Purpose**

The video directive is perhaps the easiest, so I'll start by describing that one.  As you may imagine, the job of the video directive is to include a video in the final product. 

**Example in reStructured Text**

::

    .. video:: interactive_python_vid_1
       :controls:
       :thumb: ../_static/videothumb.png

       http://media.interactivepython.org/pythondsVideos/list_unique.mov
       http://media.interactivepython.org/pythondsVideos/list_unique.webm

**Example**

TODO PUT VIDEO DIRECTIVE HERE

**Required Arguments**

One required argument: a unique identifier for the video. (This is for logging purposes. It's also necessary for managing video thumbnails and other controls in your book.) This goes to the right of the ``.. video::`` term. In the example, the unique identifier chosen is ``interactive_python_vid_1``.

**Optional Arguments**

There are two optional arguments to the video directive.

``:controls:`` -  The controls argument is a flag that, if present, allows the library that runs these directives to generate the usual set of video controls: *play, pause, rewind, fast forward*. If ``:controls:`` is not present, the video will automatically play when the page is loaded.

``:thumb:`` - The thumb argument references an image that will serve as the thumbnail for this video. It requires an additional parameter: the path to the image that should serve as the thumbnail (in the example, that path is ``../_static/videothumb.png`` (relative paths to the location of the ``.rst`` file you are currently working in are fine). If the ``:thumb`` argument is used, then a thumbnail image will take the place of the video on the page until the reader clicks on the thumbnail. Clicking on the thumbnail will cause the full video to appear at full size on the page.  If the ``:thumb:`` directive is not present, then the video will appear on the page in its full size.


**Content**

The content lines of the video directive are the lines that follow the arguments, preceded by a blank line. You can specify as many video sources as you need.  (Usually I specify two videos, one in ``.mov`` format and the other in ``webm`` format.  This seems to cover all browsers.)

**Output** 

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

**Logs & Grading**

Video directives are not tied to the grading interface. Interactions logged in the database: TODO ADD.

**Uses**

Teachers have used the video directive to include demonstrative video to accompany conceptual explanations, or to bring in video explanations from other openly licensed sources (e.g. Khan Academy, interactivepython.org).

 
Activecode
~~~~~~~~~~

The activecode directive allows you to create executable, editable example code. This allows your students to experiment with your examples by changing them and running them over and over again. 

In an **activecode** window, if logged in to a Runestone project with an account, each time you run the code, if it is has been edited since the last run, the version is saved. Each logged in user can view their own history, version by version, of the code they've edited in the window. (Screenshots are provided below of this behavior, since this example is shown outside a logged-in account.)

Activecode windows can be graded in the Runestone interface and can be tied to assignments containing multiple problems. You can also include hidden code and data files in these windows, for instance, so students can invoke functions without seeing the function definitions. (See more on this below, in the **Arguments** section.)

TODO TODO note about most people's purposes, what audience is this aimed at, etc.

**Examples in reStructured Text**

::

    .. activecode:: function_example1
       :nocanvas:
       :language: python

       def example_func(inp):
           return inp + "!!"


    .. activecode:: loop_example3
       :nocanvas:
       :language: python
       :caption: This is my caption
       :include: function_example1, function_example2

       for i in range(5):
           print('hello world {}\n'.format(i))

       # Here, you could use code from any included activecode block, like so
       print example_func("hello again")

::

    .. activecode:: function2_3

       def square(x):
           y = x ** x
           return y

       result = square(5)
       print result


**Examples**

Here is the second example above:

.. activecode:: function2_3

       def square(x):
           y = x ** x
           return y

       result = square(5)
       print result


Here is an example with a canvas.

.. activecode:: ac_example1
   :caption: A Turtle making a 90-degree left turn 

   import turtle
   t = turtle.Turtle()

   for i in range(4):
       t.forward(100)
       t.left(90)


**Required Arguments**

Required: a unique identifier after the ``:: `` in the activecode directive. No spaces in this identifier.

(This unique identifer will be the ``div`` id that contains this particular code snippet; this unique identifier allows you to tie activecode blocks to a grading interface, or any other groupings for assessment within the Runestone interface, for instance if you wanted students to complete a problem in an activecode window. For this reason, we recommend that you follow some type of naming convention in determining these unique identifiers for directives, especially activecode directives, since they are the most common place for users to edit and potentially save content repeatedly.

**Optional Arguments**

``:nopre:``  -- This flag prevents a ``<pre></pre>`` element from getting created in the page. (You might use this if you did not want to see the results of print statements from an included code segment but otherwise wanted it to be runnable.)

``:nocanvas:``  -- This flag prevents a ``<canvas>`` element from getting created. A canvas element is generally created e.g. when a program using the ``turtle`` library is run (see above).

``:caption:`` If used, this requires a text parameter. The text parameter to this argument is formatted as a caption, underneath the activecode block. You can see one in the example above, where the caption is ``A Turtle making a 90-degree left turn``.

``:language:`` The text argument to this parameter can be python, javascript, or html.  TODO TODO is this still true, and what is the default if you leave it off, is it Python?

``:include:``  This option allows you to prepend other code blocks to this activecode block. It is useful because it allows you to write individual activecode examples that build on each other without having to duplicate all the code and force the user to scroll through the code to find the newly introduced content. For example, if you write a function definition in one activecode block, you can include that block in a later activecode block using the ``:include:`` argument, and thus can invoke that function in the current activecode block without redefining it. This argument requires at least one, and can take multiple, parameters: the unique identifiers of the activecode blocks that you want to include. (See the examples in reStructured text for an example of how you can use this.)

``:hidecode:`` This will make the activecode editor initially hidden, and add a button to automatically show the editor. You might use this if you want to put an activecode block in the page in order to include it in another activecode block, but you don't need or want students to see it right away.

``:autorun:`` This flag sets up an event so that your activecode example will begin running as soon as the web page is fully loaded.

``:above:`` This positions the canvas above the editor.

``:nocodelens:`` This activecode will not have a button to show the code in an interactive codelens widget (more explanation of what this is follows in the **codelens directive** section).

``:tour_{1,2,3,4,5}``  Used for audio tours of the code.  You can have up to five different audio tours of the same code.  The format of a tour directive is ``tour name; line: audio_file_for_line``. TODO TODO is this correct? 

Here is an example of an activecode block using ``:tour_#`` argument(s):

::


    .. activecode:: tour_example
       :tour_1: "Line by Line Tour"; 1: file_for_one; 2: file_for_two

       print "line one"
       print "line two"


**Developer Notes**

Each activecode window is running in the browser.  There is no need to connect to a server, or to even be online, for these examples to work.  The activecode directive makes use of **Skulpt** (``www.skulpt.org``).  Skulpt is an open source javascript implementation of Python.

Normally an output from a print statment is appended to a ``<pre></pre>`` element in the web page.  Graphical output, such as the turtle graphics program in the example, is done on a ``<canvas>``.

** Logs & Grading **

Each version of code in an activecode block which is run is simultaneously saved, and therefore versioned. (Previously, you could save edits to an activecode block and load the most recently saved version on page load by pressing the **Load** button.)

Logged in to a book, the load history appears like so:

TODO PUT SCREENSHOTS HERE

See grading interface documentation [REFERENCE TBA] for explanation of how to associate activecode blocks with graded assignments.


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

``:breakline:``  This is the line that you want the program to stop at and ask  the question.


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
      :blankid: postfix1_blank
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

Tabbed Question
---------------

**Example**

Here is an example:

::

    .. tabbed:: tab_div

        .. tab:: Question_1

            Write a program that prints "Hello, world".

            .. activecode:: ac_example1

                print("Hello, world")

        .. tab:: Discussion

            .. disqus::
                :shortname: interactivepython
                :identifier: question1discussion


**Description**
This directive creates a tabbed interface. Each tab can contain one or more of the other directives, question types, or other content. For example, an author could write a question, and provide a tab that has a possible solution as well as a Disqus block so that users could discuss the question.

**Arguments**
The tabbed directive takes 1 argument, the name of the div containing all the tabbed content. The directive also must be provided one or more tab directives, each taking an argument specifiying the name of the tab.



.. raw:: html

    <script type="text/javascript" charset="utf-8">
        $(document).ready(createEditors);
    </script>
