Codelens
========

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



