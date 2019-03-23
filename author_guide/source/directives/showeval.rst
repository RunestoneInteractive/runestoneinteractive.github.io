ShowEval
========
The ``showeval`` directive creates an animated sequence.

Synopsis
--------

.. code-block:: rst

   .. showeval:: unique_id
      :trace_mode: boolean

      + --- Content area ---+
      | Pre-requisite information and code
      | ~~~~
      | some {{code}} followed by {{replacement code}}
      | more {{code}} followed by {{replacement code}}  ##with optional comment
      + --------------------+


All prerequisite information that should be displayed above the animation,
such as variable declaration, are separated from the step strings by ``~~~~``.

The step animations follow the ``~~~~`` and are written one per line. 


Required Arguments
------------------

unique id
A unique identifier after a space and the ``::`` in the directive.
Valid identifiers must not contain spaces.
You should also avoid the characters `` ` ``, ``,``, ``:``, and ``*``.

content area
The ``showeval`` directive should contain at least two steps to be useful.
The steps section has special formatting requirements:

- Each step must be wholly contained on a line, one animation step per line.
- Blank lines are OK.
- Use double curly braces: ``{{`` and ``}}`` to mark 
  text replaced during an animation step.
  Only 1 set of replacement text per line.
- The end braces of the original text and start of the replacement braces 
  must be exactly ``}}{{`` - no spaces are permitted.

  The braces surround the part of the line that should be replaced,
  followed by the replacement text delimited using double curly braces. 
  
To add a comment that will appear in a div beside the animation, 
denote that at the end of the step where you would like it to appear with ``##``.


trace_mode
    ``Boolean``. If ``true``, will print out a new line for each step of the animation.

    If ``false``,  will display and animate a single line, 
    overwriting the previous animation, during each animation step.


Optional Arguments
------------------

No optional arguments are defined for this directive.

Languages supported
-------------------

The ``showeval`` directive is language agnostic.
Nothing is actually executed or interpreted.
It is up to the animation author to ensure the syntax and grammar within an animation
makes sense - no syntax checking is performed.

Sphinx configuration options
----------------------------

No sphinx configuration options exist for this directive.

Internationalization
....................

tbd

Known limitations
-----------------

No syntax highlighting is performed for any language.

This directive is intended to help explore the inner workings of a small chunk of code.
To show the more complex interactions between variables and functions, 
consider using :doc:`codelens`.

.. include:: html_content.txt

A bug in ``showeval`` prevents it from working correctly in a :doc:`tab` directive.
Every animation line renders twice.

Examples
--------

The first example shows joining two arrays with showeval in trace mode
and then shows the exact same example in replace mode.
  
Showing the source code with ``:tracemode: true``.

This source code:
 
.. literalinclude:: se_examples/showeval_ex_py.txt
  :language: rst

Created this example:

.. include:: se_examples/showeval_ex_py2.txt

This example shows the exact same code as the previous example,
but with ``:tracemode: false``.

.. showeval:: showEval_false
  :trace_mode: false

  eggs = ['dogs', 'cats', 'moose']
  ~~~~

  ''.join({{eggs}}{{['dogs', 'cats', 'moose']}}).upper().join(eggs)
  {{''.join(['dogs', 'cats', 'moose'])}}{{'dogscatsmoose'}}.upper().join(eggs)
  {{'dogscatsmoose'.upper()}}{{'DOGSCATSMOOSE'}}.join(eggs)
  'DOGSCATSMOOSE'.join({{eggs}}{{['dogs', 'cats', 'moose']}})
  {{'DOGSCATSMOOSE'.join(['dogs', 'cats', 'moose'])}}{{'dogsDOGSCATSMOOSEcatsDOGSCATSMOOSEmoose'}}


Using comments
..............

Comments are optional and appear after ``##`` on any animation line.

A comment is displayed as soon as an animation line is loaded,
**before** the animation executes.
When the *Next Step* button is pressed, the comment is removed.

This source code:
 
.. literalinclude:: se_examples/showeval_ex_cpp.txt
   :language: rst

Created this example:

.. include:: se_examples/showeval_ex_cpp2.txt


