Codelens
========

The ``codelens`` directive creates an interactive environment for you to step through small python code examples. 

Synopsis
--------
The general format of the ``codelens`` directive is:

.. code-block:: rst

   .. codelens:: unique_id
      :options:

      + --- Content area ---+
      | 
      | one or more lines of python code
      | 
      + --------------------+

Codelens displays the values of variables and shows the contents and links between your objects.  
Unlike a normal code debugger intended for solving bugs, 
``codelens`` lets you step forward and backward through the code.

In addition to stepping through the code,
you as an author can embed a single question into the ``codelens`` example.  
You may ask the student to predict what the value of a variable will be after a line executes, 
what the value of an element on the heap is at the point you pause the code 
(if the term ``heap`` is unfamiliar to you, 
you need note only that you should be asking questions about values of variables, 
not e.g. an element of a Python list), 
or you may ask the student to predict which line of code will be executed next. 
This is an excellent way to help students develop a good mental model of how python works. 

It's worth noting that you can also make use of ``codelens`` in a 
live environment where you can edit code and run new examples.  
To use ``codelens`` interactively go to http://www.pythontutor.com/.

Although ``codelens`` in Runestone currently supports python only, 
the core visualization available within ``codelens`` is also available for any
language supported by `pythontutor <http://www.pythontutor.com/>`_, which currently includes C, C++, Java, Ruby and others.

Required Arguments
------------------

unique id
    A unique identifier after a space and the ``::`` in the ``codelens`` directive.
    Valid identifiers must not contain spaces.
    You should also avoid the characters `` ` ``, ``,``, ``:``, and ``*``.

content area
    The content of a ``codelens`` directive is the similar to an :doc`activecode` directive block: lines of code.
    There are a few differences:

    * The question text or additional instructions section separated from code content is not supported.
      The book will compile, but the ``codelens`` will not render correctly.
    * The hidden code section is not supported.

    Note that if your code has any errors, 
    it will definitely cause a problem when tracing through the ``codelens`` example, 
    so make sure to test your code before deploying your book!

Optional Arguments
------------------

caption
    ``String``. 
    Define a caption for the bottom of the title frame.

showoutput
    ``Boolean``. 
    Sometimes it is desirable to ignore any output from print statements, 
    in which case you would include this argument.  
    Or sometimes you just want to save space and not show console output, 
    in which case you should not use this argument.

question  
    ``String``. 
    This is the question text that will be shown to the student. 
    
    Only one question per ``codelens`` for now.

correct 
    ``String``. 
    This is the correct answer to the question.  
    This should be specified as a value from the trace data (see above).  
    For example in the first example above, 
    where you want to know the value of variable ``b``, 
    the correct answer parameter is ``globals.b``. 
    Note also that if you are asking a question about what line will be next executed, 
    you can use the variable ``line`` (see example above),
    which refers to the line number that will be *next* executed 
    (which may be a complex question if the code includes a loop or a conditional statement).

feedback  
    ``String``. 
    If the student gives the wrong answer you can give them a few sentences of feedback;
    the parameter to this argument is any string. 
    The feedback will be the same for every wrong answer, 
    so it's a good idea to make the feedback generic reminders or hints.

breakline
    ``Integer``. 
    This is the line number that you want the program to stop at and ask the question. 
    Note that the lines in the code start at 1, 
    and the breakpoint at which the code will stop and ask you the question 
    breaks BEFORE executing the line you specify in the breakline.

tracedata  
    ``JSON Object``. 
    Normally this value is filled in automatically with a JavaScript object 
    of the stack trace, but you can provide your own tracedata if you wish. 
    The **tracedata** is the object from which you access the value of the 
    ``:correct:`` answer (see below) if you are including a question in the ``codelens`` directive.

    .. admonition:: Developer notes

       You can see an example of the tracedata of a ``codelens`` directive by
       writing the ``codelens`` directive with content, building your book, 
       and then looking in the html document that was built from your ``.rst`` file, 
       which you can find in the ``build`` folder, in the corresponding directory to the 
       directory in ``_sources`` where you saved your current ``.rst`` file 
       (e.g. if your current rst file is in ``_sources/Functions/introduction.rst``, 
       you can see the tracedata for a ``codelens`` example in ``build/Functions/introduction.html``. 
        
       You can index into that **tracedata** object with dot notation, 
       but index into any list within it with ``[]``, as usual in Python.

       Note that ``globals`` are the variables in the global scope. 
       ``locals`` is populated only if the ``codelens`` question refers to an inner, 
       local scope within the program, and elements within lists, for example, are stored on the ``heap``.

       **How Tracedata works**

       The way ``codelens`` works is that when a Runestone book is built, 
       ``codelens`` takes the code and runs it through the python debugger where a series of stack frames are collected.  
       I will refer to this list of stack frames as the trace data.  
       The trace data is then embedded into the page, 
       so when a student is reading the book and wants to step through a ``codelens`` example the 
       trace data is visualized for the student.

Languages supported
-------------------

Python only at this time.

It is however to embed the core code visualization feature directly from python tutor.
This workaround lacks the question and answer features of ``codelens``,
and is styled differently.


Sphinx configuration options
----------------------------

No directive specific configuration options exist.

Internationalization
....................

tbd

Known limitations
-----------------

Codelens does not process code containing preambles or hidden code correctly.

Codelens support is for core python only - libraries such as turtle or unittest are not supported.

You can't place a ``codelens`` directive inside a :doc:`tab` directive.

Examples
--------

A ``codelens`` example with zero, or 1 line,
while legal, does not make for a compelling demonstration.

.. codelens:: cl_ex_null

.. tabbed:: cl_null_ex

   .. tab:: Source

      .. code-block:: rst 

         .. codelens:: cl_ex_null

A simple example to help visualize a concept: insertion sort.

.. include:: codelens_examples/cl_ex1.txt

.. tabbed:: cl_simple

   .. tab:: Source

      This example comes from http://pythontutor.com itself.

      .. literalinclude:: codelens_examples/cl_ex1.txt
         :language: rst

This example asks a student to predict the value of a variable:

.. include:: codelens_examples/cl_ex2.txt

.. tabbed:: cl_ex_question2

   .. tab:: Source

      .. literalinclude:: codelens_examples/cl_ex2.txt
         :language: rst

   .. tab:: Raw Trace

      This is the default trace generated by runestone.

      .. code-block:: javascript

         {"code": "a = 1\nb = 12.3\nc = \"Fred\"\nd = b", "trace": [{"ordered_globals": [], "stdout": "", "func_name": "<module>", "stack_to_render": [], "globals": {}, "heap": {}, "line": 1, "event": "step_line"}, {"ordered_globals": ["a"], "stdout": "", "func_name": "<module>", "stack_to_render": [], "globals": {"a": 1}, "heap": {}, "line": 2, "event": "step_line"}, {"ordered_globals": ["a", "b"], "stdout": "", "func_name": "<module>", "stack_to_render": [], "globals": {"a": 1, "b": 12.3}, "heap": {}, "line": 3, "event": "step_line"}, {"ordered_globals": ["a", "b", "c"], "question": {"text": "What is the value in b after line 4 executes?", "div": "question_example_modal", "feedback": "When d is set to a copy of the value of b it doesn't change the value of b.", "correct": "globals.b"}, "stdout": "", "func_name": "<module>", "stack_to_render": [], "globals": {"a": 1, "c": "Fred", "b": 12.3}, "heap": {}, "line": 4, "event": "step_line"}, {"ordered_globals": ["a", "b", "c", "d"], "question": {"text": "What is the value in b after line 4 executes?", "div": "question_example_modal", "feedback": "When d is set to a copy of the value of b it doesn't change the value of b.", "correct": "globals.b"}, "stdout": "", "func_name": "<module>", "stack_to_render": [], "globals": {"a": 1, "c": "Fred", "b": 12.3, "d": 12.3}, "heap": {}, "line": 4, "event": "return"}]}


   .. tab:: Pretty Trace

      This is the raw trace, but formatted.
      The globals object refernced in the directive is at the end of this object.

      .. code-block:: javascript

         {
           "code":"a = 1\nb = 12.3\nc = \"Fred\"\nd = b",
           "trace":[
              {
                 "ordered_globals":[

                 ],
                 "stdout":"",
                 "func_name":"<module>",
                 "stack_to_render":[

                 ],
                 "globals":{

                 },
                 "heap":{

                 },
                 "line":1,
                 "event":"step_line"
              },
              {
                 "ordered_globals":[
                    "a"
                 ],
                 "stdout":"",
                 "func_name":"<module>",
                 "stack_to_render":[

                 ],
                 "globals":{
                    "a":1
                 },
                 "heap":{

                 },
                 "line":2,
                 "event":"step_line"
              },
              {
                 "ordered_globals":[
                    "a",
                    "b"
                 ],
                 "stdout":"",
                 "func_name":"<module>",
                 "stack_to_render":[

                 ],
                 "globals":{
                    "a":1,
                    "b":12.3
                 },
                 "heap":{

                 },
                 "line":3,
                 "event":"step_line"
              },
              {
                 "ordered_globals":[
                    "a",
                    "b",
                    "c"
                 ],
                 "question":{
                    "text":"What is the value in b after line 4 executes?",
                    "div":"question_example_modal",
                    "feedback":"When d is set to a copy of the value of b it doesn't change the value of b.",
                    "correct":"globals.b"
                 },
                 "stdout":"",
                 "func_name":"<module>",
                 "stack_to_render":[

                 ],
                 "globals":{
                    "a":1,
                    "c":"Fred",
                    "b":12.3
                 },
                 "heap":{

                 },
                 "line":4,
                 "event":"step_line"
              },
              {
                 "ordered_globals":[
                    "a",
                    "b",
                    "c",
                    "d"
                 ],
                 "question":{
                    "text":"What is the value in b after line 4 executes?",
                    "div":"question_example_modal",
                    "feedback":"When d is set to a copy of the value of b it doesn't change the value of b.",
                    "correct":"globals.b"
                 },
                 "stdout":"",
                 "func_name":"<module>",
                 "stack_to_render":[

                 ],
                 "globals":{
                    "a":1,
                    "c":"Fred",
                    "b":12.3,
                    "d":12.3
                 },
                 "heap":{

                 },
                 "line":4,
                 "event":"return"
              }
           ]
        }

 
The answer to a question need not relate to a value.
In this example, we ask not for a value from a variable, but rather which line executes next.

.. include:: codelens_examples/cl_ex3.txt

.. tabbed:: cl_simple

   .. tab:: Source

      .. literalinclude:: codelens_examples/cl_ex3.txt
         :language: rst


Workarounds for languages other than Python
-------------------------------------------
Although ``codelens`` is supported only for Python,
that does not mean there is not a code visualization option available.

You can link directly to pythontutor.com.
The site include a facility to generate either a link
or an emdeddable iframe:

.. tabbed:: example-cpp

   .. tab:: Source

      .. literalinclude:: codelens_examples/cl_ex_cpp.txt
         :language: rst

   .. tab:: Frame

      .. include:: codelens_examples/cl_ex_cpp.txt

It's not perfect as the output and visualizations of variables does not flow below
the code.
Also, note that this technique relies on the ``raw`` directive,
which does make your book less portable and flexible.

It is a best practice to wrap markup specific to a single output generator
with an ``only`` directive:

.. code-block:: rst

   .. only:: html

      .. raw:: html

         <iframe ... />

One minor advantage of the embedded iframe over ``codelens`` is the ability to
click on a line of code and set breakpoints.

The back and forward buttons jump to the next breakpoint, if set.

Logs & Grading
--------------

Clicks are logged. Answers to questions are also logged, but are currently not plugged into the grading interface and are used solely as a tool for checking understanding.



