Runestone Directives Documentation
==================================

Each Runestone directive has a particular purpose. Each is detailed below, including:

* What each directive allows you to create
* The syntax for using each directive
* Examples, or links to examples, of how instructors have used these directives in interactive textbook work
* If applicable, how exercises created by these directives can be graded
* Available additional developer documentation/notes

General Syntax
---------------

.. sidebar:: Quick Navigation

   .. contents:: Topic Outline

All directives start out with ``..``, then a single space, followed by the name of the directive (e.g. ``video``, as seen below), and then ``::``, followed by a single space.

Most directives have a required argument of a unique identifier, which goes immediately to the right of the directive name. This is for logging purposes. It's also necessary for managing any controls or

Spacing, including indentation consistency, is very important in implementing directives inside ``.rst`` files. Any missed or incorrect space may cause unexpected errors, strange-looking pages, or may cause information not to display on the deployed pages in your online book, so it's worth checking your final product before releasing content to students.

Directives may have **required arguments**. In many cases, an argument that is a unique identifier for that particular directive's ``div`` id, will follow the ``::`` in the directive (example below).

Further (often optional) arguments for a directive generally occur below that first line, surrounded by single ``:`` s. Some of those require parameters -- for example, the ``:thumb:`` addition for the ``video`` directive  requires a path to a ``.png`` image for the thumbnail image that should appear for the video, which you can see in the video directive example.

When reStructured Text files are *built* into static files in your Runestone textbook, the directives result in HTML and JavaScript inside those HTML files that make up your book.

We are in the process of creating a full set of documentation for the HTML and JavaScript created by our special Runestone directives.


Directives
----------

Video
~~~~~

**Purpose**

As you may imagine, the job of the video directive is to embed a video in a page.

**Example in reStructured Text**

::

    .. video:: interactive_python_vid_1
       :controls:
       :thumb: ../_static/videothumb.png

       http://media.interactivepython.org/pythondsVideos/list_unique.mov
       http://media.interactivepython.org/pythondsVideos/list_unique.webm


**Example**

.. video:: interactive_python_vid_1
   :controls:
   :thumb: ../_static/videothumb.png

   http://media.interactivepython.org/pythondsVideos/list_unique.mov
   http://media.interactivepython.org/pythondsVideos/list_unique.webm

**Required Arguments**

A unique identifier for the video. No spaces. This goes to the right of the ``.. video::`` term. In the example, the unique identifier chosen is ``interactive_python_vid_1``.

**Optional Arguments**

There are two optional arguments to the video directive.

``:controls:`` -  The controls argument is a flag that, if present, allows the library that runs these directives to generate the usual set of video controls: *play, pause, rewind, fast forward*. If ``:controls:`` is not present, the video will automatically play when the page is loaded.

``:thumb:`` - The thumb argument references an image that will serve as the thumbnail for this video. It requires an additional parameter: the path to the image that should serve as the thumbnail (in the example, that path is ``../_static/videothumb.png`` (relative paths to the location of the ``.rst`` file you are currently working in are fine). If the ``:thumb`` argument is used, then a thumbnail image will take the place of the video on the page until the reader clicks on the thumbnail. Clicking on the thumbnail will cause the full video to appear at full size on the page.  If the ``:thumb:`` directive is not present, then the video will appear on the page in its full size.


**Content**

The content lines of the video directive are the lines that follow the arguments, preceded by a blank line. You can specify as many video sources as you need.  (Usually I specify two videos, one in ``.mov`` format and the other in ``webm`` format.  This seems to cover all browsers.)

**Logs & Grading**

Video directives are not tied to the grading interface. Interactions logged in the database: each time a video is played, it is logged (so if you have logged-in users, you can have a log of who has played it; regardless, you can have a log of how many times it has been played).

**Uses**

Teachers have used the video directive to include demonstrative video to accompany conceptual explanations, or to bring in video explanations from other openly licensed sources (e.g. Khan Academy, interactivepython.org).


Activecode
~~~~~~~~~~

The activecode directive allows you to create executable, editable example code. This allows your students to experiment with your examples by changing them and running them over and over again.

In an **activecode** window, if logged in to a Runestone project with an account, each time you run the code, if it is has been edited since the last run, the version is saved. Each logged in user can view their own history, version by version, of the code they've edited in the window. (Screenshots are provided below of this behavior, since this example is shown outside a logged-in account.)

Activecode windows can be graded in the Runestone interface and can be tied to assignments containing multiple problems. You can also include hidden code and data files in these windows, for instance, so students can invoke functions without seeing the function definitions. (See more on this below, in the optional arguments section.)

One of the great things about activecode is that you can experiment with the code in the windows as much as you want. This can be very helpful as you are learning to program.

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

::

    .. activecode:: ac_example1
       :caption: A Turtle making a square

       import turtle
       t = turtle.Turtle()

       for i in range(4):
           t.forward(100)
           t.left(90)


**Examples**

Here is the second example above:

.. activecode:: function2_3

    def square(x):
        y = x * x
        return y

    result = square(5)
    print result


The turtle example with a canvas.

.. activecode:: ac_example1
   :caption: A Turtle making a square

   import turtle
   t = turtle.Turtle()

   for i in range(4):
       t.forward(100)
       t.left(90)


**Required Arguments**

A unique identifier after a space and the ``::`` in the activecode directive. No spaces may be included in this identifier.

This unique identifer will be the ``div`` id that contains this particular code snippet; this unique identifier allows you to tie activecode blocks to a grading interface, or any other groupings for assessment within the Runestone interface, for instance if you wanted students to complete a problem in an activecode window. For this reason, we recommend that you follow some type of naming convention in determining these unique identifiers for directives, especially activecode directives, since they are the most common place for users to edit and potentially save content repeatedly.

**Optional Arguments**

``:nopre:``  -- This flag prevents a ``<pre></pre>`` element from getting created in the page. (You might use this if you did not want to see the results of print statements from an included code segment but otherwise wanted it to be runnable.)

``:nocanvas:``  -- This flag prevents a ``<canvas>`` element from getting created. A canvas element is generally created e.g. when a program using the ``turtle`` library is run (see above).

``:caption:`` If used, this requires a text parameter. The text parameter to this argument is formatted as a caption, underneath the activecode block. You can see one in the example above, where the caption is ``A Turtle making a square``.

``:language:`` The text argument to this parameter can be python, javascript, or html.  TODO TODO is this still true, and what is the default if you leave it off, is it Python?

``:include:``  This option allows you to prepend other code blocks to this activecode block. It is useful because it allows you to write individual activecode examples that build on each other without having to duplicate all the code and force the user to scroll through the code to find the newly introduced content. For example, if you write a function definition in one activecode block, you can include that block in a later activecode block using the ``:include:`` argument, and thus can invoke that function in the current activecode block without redefining it. This argument requires at least one, and can take multiple, parameters: the unique identifiers of the activecode blocks that you want to include. (See the examples in reStructured text for an example of how you can use this.)

``:hidecode:`` This will make the activecode editor initially hidden, and add a button to automatically show the editor. You might use this if you want to put an activecode block in the page in order to include it in another activecode block, but you don't need or want students to see it right away.

``:autorun:`` This flag sets up an event so that your activecode example will begin running as soon as the web page is fully loaded.

``:above:`` This positions the canvas above the editor.

``:nocodelens:`` This activecode will not have a button to show the code in an interactive codelens widget (more explanation of what this is follows in the **codelens directive** section).

``:tour_{1,2,3,4,5}``  Used for audio tours of the code.  You can have up to five different audio tours of the same code.  The format of a tour directive is ``tour name; line: audio_file_for_line`` where ``audio_file_for_line`` is the path to the audio file. See `this tool <https://github.com/CSLearning4U/AudioTourTool>`_ for easy creation of activecode blocks with audiotours.

Here is an example of an activecode block using ``:tour_#`` argument(s):

::


    .. activecode:: tour_example
       :tour_1: "Line by Line Tour"; 1: file_name_for_one; 2: file_name_for_two

       print "line one"
       print "line two"


A tool has been developed to easily record and create the directive syntax for an audiotour of an active code window. You can find it `here <https://github.com/CSLearning4U/AudioTourTool>`_.

**Developer Notes**

Each activecode window is running in the browser.  There is no need to connect to a server, or to even be online, for these examples to work.  The activecode directive makes use of **Skulpt** (``www.skulpt.org``), which is an open source javascript implementation of Python.

Normally an output from a print statment is appended to a ``<pre></pre>`` element in the web page.  Graphical output, such as the turtle graphics program in the example, is done on a ``<canvas>``.

**Logs & Grading**

Each version of code in an activecode block which is run is simultaneously saved, and therefore versioned. (Previously, you could save edits to an activecode block and load the most recently saved version on page load by pressing the **Load** button.)

Logged in to a book, the load history appears like so:

.. image:: images/scrubber2.png
   :alt: image of a code window, below a bar with save and run on the left and a bar showing a timestamp of last save
   :align: center

.. image:: images/scrubber3.png
   :alt: image of a bar with save and run on the left and a bar showing a timestamp of last save, later than the last, with different code
   :align: center


See the instructor documentation [LINK TBA] for explanation of how to associate activecode blocks with graded assignments.


Codelens
~~~~~~~~

The codelens directive creates an interactive environment for you to step through small code examples. (With the ``:codelens:`` argument to an activecode window, it can be used for any activecode code block.)

Codelens displays the values of variables and shows the contents and links between your objects.  Unlike a normal code debugger intended for solving bugs, codelens lets you step forward and backward through the code.

In addition to stepping through the code you as an author can embed a single question into the codelens example.  You may ask the student to predict what the value of a variable will be after a line executes, what the value of an element on the heap is at the point you pause the code (if the term ``heap`` is unfamiliar to you, you need note only that you should be asking questions about values of variables, not e.g. an element of a Python list), or you may ask the student to predict which line of code will be executed next. (This is an excellent way to help students develop a good mental model of how python works.) The codelens directive shows a codelens window initially, which looks as shown below, rather than an activecode window with the option of running through the code using codelens.

It's worth noting that you can also make use of codelens in a live environment where you can edit code and run new examples.  To use codelens interactively go to ``http://www.pythontutor.com/``.

**Examples in reStructured Text**

::

    .. codelens:: simpleexample

        fruit = ["apple","orange","banana","cherry"]
        numlist = [6,7]
        newlist = fruit + numlist
        zeros = [0] * 4

        zeros[1] = fruit
        zeros[1][2] = numlist

::

    .. codelens:: question_example
       :question: What is the value in b after line 4 executes?
       :feedback: When d is set to a copy of the value of b it doesn't change the value of b.
       :breakline: 4
       :correct: globals.b

       a = 1
       b = 12.3
       c = "Fred"
       d = b

::

    .. codelens:: Ketchup_Speed
       :question: What line will be executed after the current line executes?
       :feedback: This code is executed one line at a time from top to bottom. (No loops.)
       :breakline: 3
       :correct: line

       dripMPH = .028
       FPM = 5280.0
       dripFPH = dripMPH * FPM
       MPH = 60
       dripFPM = dripFPH / MPH
       print("Ketchup speed in feet per minute:")
       print(dripFPM)
       print("Ketchup speed to move 4 feet in a minute:")
       print(4 / dripFPM)


**Examples**

Here are the above examples of codelens in action:

.. codelens:: simpleexample

    fruit = ["apple","orange","banana","cherry"]
    numlist = [6,7]
    newlist = fruit + numlist
    zeros = [0] * 4

    zeros[1] = fruit
    zeros[1][2] = numlist

.. codelens:: question_example
       :question: What is the value in b after line 4 executes?
       :feedback: When d is set to a copy of the value of b it doesn't change the value of b.
       :breakline: 4
       :correct: globals.b

       a = 1
       b = 12.3
       c = "Fred"
       d = b


.. codelens:: Ketchup_Speed
   :question: What line will be executed after the current line executes?
   :feedback: This code is executed one line at a time from top to bottom. (No loops.)
   :breakline: 3
   :correct: line

   dripMPH = .028
   FPM = 5280.0
   dripFPH = dripMPH * FPM
   MPH = 60
   dripFPM = dripFPH / MPH
   print("Ketchup speed in feet per minute:")
   print(dripFPM)
   print("Ketchup speed to move 4 feet in a minute:")
   print(4 / dripFPM)


**Required Arguments**

The identifier after the ``::`` must be unique. No spaces.

**Content**

The content of a codelens directive is the same as an activecode directive block: lines of code.

Note that if your code has any errors, it will definitely cause a problem when tracing through the codelens example, so make sure to test your code before deploying your book!

**Optional Arguments**

``:caption:``  The text provided for this option will be formatted as a caption on the bottom of the codelens window.

``:showoutput:``  Sometimes it is desirable to ignore any output from print statements, in which case you would include this argument.  Or sometimes you just want to save space and not show console output, in which case you should not use this argument.

``:question:``  This is the question text that will be shown to the student. (Only one question per codelens for now.)

``:correct:`` This is the correct answer to the question.  This should be specified as a value from the trace data (see above).  For example in the first example above, where you want to know the value of variable ``b``, the correct answer parameter is ``globals.b``. Note also that if you are asking a question about what line will be next executed, you can use the variable ``line`` (see example above), which refers to the line number that will be *next* executed (which may be a complex question if the code includes a loop or a conditional statement).

``:feedback:``  If the student gives the wrong answer you can give them a few sentences of feedback; the parameter to this argument is any string. The feedback will be the same for every wrong answer, so it's a good idea to make the feedback generic reminders or hints.

``:breakline:``  This is the line number that you want the program to stop at and ask  the question. Note that the lines in the code start at 1, and the breakpoint at which the code will stop and ask you the question breaks BEFORE executing the line you specify in the breakline.

``:tracedata:``  Normally this value is filled in automatically with a JavaScript object of the stack trace, but you can provide your own tracedata if you wish. The **tracedata** is the object from which you access the value of the ``:correct:`` answer (see below) if you are including a question in the codelens directive.

**Developer notes for tracedata:** You can see an example of the tracedata of a codelens directive by writing the codelens directive with content, building your book, and then looking in the html document that was built from your ``.rst`` file, which you can find in the ``build`` folder, in the corresponding directory to the directory in ``_sources`` where you saved your current ``.rst`` file (e.g. if your current rst file is in ``_sources/Functions/introduction.rst``, you can see the tracedata for a codelens example in ``build/Functions/introduction.html``. You can index into that **tracedata** object with dot notation, but index into any list within it with ``[]``, as usual in Python.

Here is an example of a set of tracedata.

Note that ``globals`` are the variables in the global scope. ``locals`` is populated only if the codelens question refers to an inner, local scope within the program, and elements within lists, for example, are stored on the ``heap``.

**Further Developer Notes**

The way codelens works is that when a Runestone book is built, codelens takes the code and runs it through the python debugger where a series of stack frames are collected.  I will refer to this list of stack frames as the trace data.  The trace data is then embedded into the page, so when a student is reading the book and wants to step through a codelens example the trace data is visualized for the student.

**Logs & Grading**

Clicks are logged. Answers to questions are also logged, but are currently not plugged into the grading interface and are used solely as a tool for checking understanding.


Datafile
~~~~~~~~

The datafile directive works with activecode when you want to have the user read some data from a file.  Because we want the file to come from the browser, not some far away server, or from the user's local hard drive, we can fake files' existence in two different ways.

1.  We can put the data into ``pre`` element.  The id on the element serves as the filename.

2.  We can put the data into a ``textarea`` element.  Again the id on the element serves as the file name.  However, with a text area, the file data can be modified.

Both of these options can be achieved with the ``datafile`` directive.

**Examples in reStructured Text**

::

    .. datafile:: mydata.txt
       :edit:
       :rows: 20
       :cols: 60

       here is the first line in the data file
       also, this is the second line in the data file
       and this is the third line

::

    .. datafile:: mydata2.txt
       :rows: 20
       :cols: 60

       here is the first line in the data file
       also, this is the second line in the data file
       and this is the third line


This example will produce a text area that is 20 rows long and 60 columns wide.  The ``:edit:`` flag tells the directive to produce a textarea rather than a pre element.

**Examples**

.. datafile:: mydata.txt
   :edit:
   :rows: 20
   :cols: 60

   here is the first line in the data file
   also, this is the second line in the data file
   and this is the third line

.. datafile:: mydata2.txt
   :rows: 20
   :cols: 60

   here is the first line in the data file
   also, this is the second line in the data file
   and this is the third line



**Arguments**

The required argument is the 'filename' (this is not reliant on any actual filename, but is the filename you must inform users of so that they can perform file reading operations in activecode windows). In the examples it is ``mydata.txt`` and ``mydata2.txt``. This must be unique within the document as it does become the id of the element.

**Optional Arguments**

``:hide:``  -- This makes the file invisible.  This might be good if you have an exceptionally long file that you want to use in an example where it is not important that the student see all the data, or in an example when you want students to solve a problem dependent on file reading operations in which they should not be able to determine the answer by looking at the file. It will simply be included in the page so that the file can be used in programs (activecode blocks, etc).

``:edit:``  -- This flag makes the file into an editable file in a textarea. This is great if you want your students to be able run their program on different data from a file.  All they have to do is edit the textarea and rerun the program. TODO are edits saveable by users??

``rows``  -- This is for sizing the textarea.  The value has no effect on a pre element.  If the rows value is not provided, the directive will do its best to guess the number of rows within a reasonable number.

``cols``  -- Again this is for sizing the text area, and again, if not provided, the directive will come up with a reasonable value.


Multiple Choice
~~~~~~~~~~~~~~~

The multiple choice directive, ``..mchoice::``, allows for insertion of multiple choice questions, either with a single correct option or a checkbox question with multiple correct answers (there must be at least one correct answer for a multiple choice question).

(Previously, these directive options were in two different directives:  ``mchoicemf`` and ``mchoicema``. For now, these work, but they are deprecated -- you should use ``mchoice`` if you are writing new questions.)


**Examples in reStructured Text**

Multiple Choice with One Correct Answer

::

    .. mchoice:: question1_1
       :answer_a: Python
       :answer_b: Java
       :answer_c: C
       :answer_d: ML
       :correct: a
       :feedback_a: Yes, Python is a great language to learn, whether you are a beginner or an experienced programmer. You can write many different styles of programs using the Python language.
       :feedback_b: Java is a good object oriented language but it has some details that make it hard for the beginner.
       :feedback_c: C is an imperative programming language that has been around for a long time, but it is not the one that we use.
       :feedback_d: No, ML is a functional programming language.  (You can use Python to write functional programs as well!)

       What programming language does this site help you to learn?

Multiple Choice with Multiple Answer(s)

::

    .. mchoice:: question1_2
       :multiple_answers:
       :answer_a: xyZ
       :answer_b: new_var_3
       :answer_c: 3things
       :answer_d: hello-there
       :correct: a,b
       :feedback_a: Any combination of letters is a valid variable name in Python.
       :feedback_b: Underscores are acceptable to include in Python variable names, as long as they are not the first character in the variable name.
       :feedback_c: Variable names can't begin with digits in Python.
       :feedback_d: Hyphens and dashes are not acceptable characters to include in variable names in Python.

       Which of these are valid variable names in Python? (Choose all that are correct)

**Examples**

.. mchoice:: question1_1
    :answer_a: Python
    :answer_b: Java
    :answer_c: C
    :answer_d: ML
    :correct: a
    :feedback_a: Yes, Python is a great language to learn, whether you are a beginner or an experienced programmer. You can write many different styles of programs using the Python language.
    :feedback_b: Java is a good object oriented language but it has some details that make it hard for the beginner.
    :feedback_c: C is an imperative programming language that has been around for a long time, but it is not the one that we use.
    :feedback_d: No, ML is a functional programming language.  (You can use Python to write functional programs as well!)

    What programming language does this site help you to learn?

.. mchoice:: question1_2
    :multiple_answers:
    :answer_a: xyZ
    :answer_b: new_var_3
    :answer_c: 3things
    :answer_d: hello-there
    :correct: a,b
    :feedback_a: Any combination of letters is a valid variable name in Python.
    :feedback_b: Underscores are acceptable to include in Python variable names, as long as they are not the first character in the variable name.
    :feedback_c: Variable names can't begin with digits in Python.
    :feedback_d: Hyphens and dashes are not acceptable characters to include in variable names in Python.

    Which of these are valid variable names in Python? (Choose all that are correct)

**Required Arguments**

Unique identifier for the question, e.g. ``question1_2``. You also must have at least ``answer_a``, and the ``correct`` argument.

The value for the ``correct`` argument must correspond to an answer you've included, e.g. if you have included ``:answer_a:`` and ``:answer_b:`` only, you cannot use ``:correct: c``.

For *Multiple Choice Multiple Answer*, you may have more than one correct answer, comma-separated, as seen in the raw RST examples above. For *Multiple Choice Single Answer*, you must have only one correct answer.

**Optional Arguments**

``:multiple_answer:`` - This argument determines whether the question may have multiple correct answers with checkboxes, as above (including this option means you get the multiple answers format).

*Multiple Choice Single Answer*

``:answer_a:``, ``:answer_b:``, ``:answer_c:``, ``:answer_d:``, ``:answer_e:``  You can provide up to five different possible correct answers, like so. (See **required arguments** above.)

``:feedback_a:``, ``:feedback_b:``, ``:feedback_c:``, ``:feedback_d:``, ``:feedback_e:``  Each answer can have its own feedback. If there is feedback for one answer, there should be feedback for each answer. We recommend that thoughtful feedback be included for every multiple choice question.


*Multiple Choice Multiple Answer*

``:answer_a:``, ``:answer_b:``, ``:answer_c:``, ``:answer_d:``, ``:answer_e:``  You can provide up to five different possible correct answers. (See **required arguments** above.)

``:feedback_a:``, ``:feedback_b:``, ``:feedback_c:``, ``:feedback_d:``, ``:feedback_e:``  Each answer can have its own feedback. If there is feedback for one answer, there should be feedback for each answer. We recommend that thoughtful feedback be included for every multiple choice question, and that question writers consider how feedback may be useful for questions which have multiple correct answers!


Fill in the Blank
~~~~~~~~~~~~~~~~~

The fill in the blank Runestone directive, ``.. fillintheblank::``, allows you to ask for a value to fill in the rest of a statement (in English or code).  You can test for the value submitted using JavaScript regular expressions.

The basic format is like so:

::

  .. fillintheblank:: unique_identifier_string_no_spaces
     :iscode: boolean
     :correct: somestring in js regexp format
     :feedback: this string will always be displayed if wrong
     :feedback: ('regexp2 here', 'this message appears if that regexp2 matches submission')
     [note that you can have up to 3 extra specific feedbacks]
     Question text goes here.


**Example in reStructured Text**

::

    .. fillintheblank:: fill1412

        .. blank:: blank1345
            :correct: \\bred\\b
            :feedback1: (".*", "Try 'red'")

            Fill in the blanks to make the following sentence: "The red car drove away" The

        .. blank:: blank52532
            :correct: \\baway\\b
            :feedback1: (".*", "Try 'away'")

            car drove


**Warning**  We are looking at ways to simplify the syntax of fillintheblank so the syntax of this one may change.

.. fillintheblank:: fill1412

    .. blank:: blank1345
        :correct: \\bred\\b
        :feedback1: (".*", "Try 'red'")

        Fill in the blanks to make the following sentence: "The red car drove away" The

    .. blank:: blank52532
        :correct: \\baway\\b
        :feedback1: (".*", "Try 'away'")

        car drove


**Required Arguments**

Unique identifier for the question, e.g. ``baseconvert1``.

``:correct:`` - The regular expression for the correct answer/answer set.

``:blankid:`` - The id of the blank, any string.

Note the need for a ``:textfield:`` in the question with the ``:blankid`` id.

**Optional Arguments**


Parson's Problems
~~~~~~~~~~~~~~~~~

Parson's Problems:

Question text comes first, then ``-----`` separates the question text from the code.  You provide the correct code, and the javascript takes care of mixing it up.
::

    .. parsonsprob:: question1_100_4

       Construct a block of code that correctly implements the accumulator pattern.
       -----
       x = 0
       for i in range(10)
          x = x + 1


You can also group statements using ``=====``  In the example below the for loop and its body will appear as one block to position in the problem.

::

    .. parsonsprob:: question1_100_4

       Construct a block of code that correctly implements the accumulator pattern.
       -----
       x = 0
       =====
       for i in range(10)
          x = x + 1
       =====
       print(x)


.. parsonsprob:: question1_100_4

   Construct a block of code that correctly implements the accumulator pattern.
   -----
   x = 0
   =====
   for i in range(10)
      x = x + 1
   =====
   print(x)


Disqus
~~~~~~


You can embed disqus discussions:

::

    .. disqus::
        :shortname: Your registered  shortname with disqus
        :identifier: discussion1


Tabs and Tab Groups
~~~~~~~~~~~~~~~~~~~

You can create a section that contains several tabs.  This is useful for exercises, and in other situations where you may want to partially reveal content.

::

    .. tabbed:: exercise1

        .. tab:: Question 1

            Write a program that prints "Hello, world".

            .. activecode:: helloworld

                print("Hello, world")

        .. tab:: Discussion

            .. disqus::
                :shortname: interactivepython
                :identifier: helloworlddiscussion


.. tabbed:: exercise1

    .. tab:: Question 1

        Write a program that prints "Hello, world".

        .. activecode:: helloworld

            print("Hello, world")

    .. tab:: Discussion

        .. disqus::
            :shortname: interactivepython
            :identifier: helloworlddiscussion


Polls
~~~~~

Allow students to vote or rate things on a scale

::

    .. poll:: pollid1
       :scale: 10
       :allowcomment:

        On a scale from 1 to 10, how important do you think it is to have a polling directive in the Runestone Tools?

.. poll:: pollid1
   :scale: 10
   :allowcomment:

    On a scale from 1 to 10, how important do you think it is to have a polling directive in the Runestone Tools?

Reveal
~~~~~~

Very useful for in class presentations, or for in book exercises where you want to keep a solution hidden.

::

    .. reveal:: revealid1
        :showtitle: Reveal Content
        :hidetitle: Hide Content

        This content starts out hidden. It's visibility can be toggled by using the Show/Hide button.

        The reveal block can also contain other directives (ActiveCode, Disqus block, etc):

        .. activecode:: ac11

            print ("Hello, world")



.. reveal:: revealid1
    :showtitle: Reveal Content
    :hidetitle: Hide Content

    This content starts out hidden. It's visibility can be toggled by using the Show/Hide button.

    The reveal block can also contain other directives (ActiveCode, Disqus block, etc):

    .. activecode:: ac11

        print ("Hello, world")


Drag and Drop
~~~~~~~~~~~~~

::

    .. dragndrop:: identifier
        :feedback: Feedback that is displayed if things are incorrectly matched--is optional
        :match_1: Draggable element text|||Dropzone to be matched with text
        :match_2: Drag to Answer B|||Answer B
        :match_3: Draggable text|||Text of dropzone
        ...etc...(up to 20 matches)

        The question goes here.


Clickable Areas
~~~~~~~~~~~~~~~

::


    .. clickablearea:: identifier
        :question: Question text
        :feedback: Optional feedback for incorrect answer
        :iscode: Boolean that if present will put the content into a <pre>
        :table: Boolean that indicates that the content is a table.
        :correct: An array of the indices of the correct elements, separated by semicolons--if this is a table, each item in the array is a tuple
        with the first number being the row and the second number being the column--use a column number of 0 to make the whole row correct (ex: 1,2;3,0 makes the 2nd data cell in the first row correct as well as the entire 3rd row)
        :incorrect: An array of the indices of the incorrect elements--same format as the correct elements.

        --Content--




Short Answer
~~~~~~~~~~~~

::

    .. shortanswer:: uniqueid
       :optional:

       text of the question goes here


Usage Assignment
~~~~~~~~~~~~~~~~

::

    .. usageassignment:: prep_1
       :chapters: chap_name1[, chapname2]*
       :subchapters: subchapter_name[, subchaptername2]*
       :assignment_name: <str>
       :assignment_type: <int id of the assignment type object; kind of a hack>
       :deadline: <str>
       :sections: <comma separated int ids of the section objects; kind of a hack>
       :pct_required: <int>   :points: <int>

Controlling Question Numbering
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

::

    .. qnum::
       'prefix': character prefix before the number
       'suffix': character prefix after the number
       'start': start numbering with this value

For example:
::

    .. qnum::
       :prefix: turtle-
       :start: 10

Will cause the questions in this section to be displayed as turtle-10, turtle-11, and so on.
