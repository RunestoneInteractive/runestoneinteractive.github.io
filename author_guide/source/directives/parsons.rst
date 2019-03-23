Parsons Problems
================

In a Parsons problem, users are provided with the lines / blocks of code and students
must reorder them to create a solution. 


Synopsis
--------
The general format of the parsons directive is:

.. code-block:: rst

   .. parsonsprob:: unique_id
      :options:

      + --- Content area ---
      |
      | one or more lines of instruction for the problem
      | -----
      | one or more lines of text 
      | =====
      | grouped by
      | =====
      | five equals
      |
      + --------------------

Required Arguments
------------------

unique id
    A unique identifier after a space and the ``::`` in the title directive.
    Valid identifiers must not contain spaces.
    You should also avoid the characters `` ` ``, ``,``, ``:``, and ``*``.

content area
    A content block is required for a parsons problem.
    Place the question text after any directive options, if specified.

    Use ``-----`` to separate the question text from the code. 
    The code should be specified in the correct order and indented properly. 
    You can also group lines using ``=====`` as in the problem below. 

    The code blocks will be shuffled randomly in the source area; 
    press the *Reset* button on a problem to see this shuffling in action. 
    To make the problem more difficult, you can enter *distractors* that are not part of the solution. 
    These lines or blocks are marked by placing ``#distractor`` after the line. 
    You can pair one or more distractors with a correct code block by marking it with ``#paired``. 
    When shuffled, paired blocks will be kept together with the correct code block.

    .. note::

       There is no space between the ``#`` and the ``distractor`` or ``paired``

Optional Arguments
------------------

adaptive
    ``Boolean``. Offer to 'adapt', or simplify the problem after a few failed attempts.
    Default is false.

    If specified, then this option will offer help after 3 failed attempts.  
    After more failures, it will incrementally simplify the problem.
    It may remove indentation as part of the problem or remove distractors one at a time.

language
    ``String``. Set the language of the content area.

    The default language is python. 
    In a Parsons problem, the language is only used to control syntax highlighting.

    The default language can be set in the book ``pavement.py`` file.

maxdist
    ``Integer``. Define a maximum number of distractors

    If you specify distractors in the code, 
    then this will specify the maximum number of distractors presented to the user.

noindent
    ``Boolean``. Do not mark against incorrect indentation.

    If you do not want to force correct indentation, 
    then this argument will indent blocks as you specify them. 
    This makes the problem significantly easier to solve.

    By default, code indentation matters. 
    This is semantically meaningful in Python and good code practice in other programming languages. 
    In the problem below, the third line needs to be indented to be correct.

    .. literalinclude:: pa_examples/parson_ex1.txt
         :language: rst

numbered
    ``Enumerated``. Turns on block numbering, either on the left or right.

    Possible values are either ``left`` or ``right``.

order
    ``List``. Define a specific 'shuffled' order

    If you don't want the code to be randomly shuffled, 
    you can specify the order of the blocks in a comma-separated list (e.g., 0,5,3,2,4,1).


Languages supported
-------------------

Any text is supported, however, syntax highlighting is supported for
a limited number of programming languages.
Syntax highlighting is supported for python, java, javascript, html, 
c, c++, ruby, and natural.

The language 'natural' is equivalent to 'none' in docutils,
that is syntax highlighting is disabled.

.. note::
   
   This directive uses 'c++' to refer to C++, whereas the activecode directive uses 'cpp'.

Sphinx configuration options
----------------------------

The following ``options.build.template_args`` values can be set in a book pavement.py file.

language
    The default language for parsons problem directives.

Internationalization
....................

TBD.

Known limitations
-----------------

The correct item to be paired with a ``#paired`` distraction must appear directly prior to the block marked ``#paired``.

Once you have committed to using ``====`` to define groups of lines,
then **every** line must be separated as groups.

.. include:: html_content.txt

Examples
--------
The simplest parsons problems take each line of text,
places each in its own parsons block,
and assesses on both line order and indentation.

.. tabbed:: example1

   .. tab:: Source

      .. literalinclude:: pa_examples/parson_ex1.txt
         :language: rst

   .. tab:: Try It

      .. include:: pa_examples/parson_ex1.txt

   .. tab:: C++

      .. literalinclude:: pa_examples/parson_ex1_cpp.txt
         :language: rst

   .. tab:: Try It

      .. include:: pa_examples/parson_ex1_cpp.txt

Use the ``=====`` markup in the content area to control parsons block definitions.

.. tabbed:: example_groups

   .. tab:: No groups
      
      The default is to split each line of code into it's own block.

      .. literalinclude:: pa_examples/parson_ex_group1.txt
         :language: rst

   .. tab:: Try It

      .. include:: pa_examples/parson_ex_group1.txt

   .. tab:: Groups
      
      If even 1 group is used, then all lines are interpreted as belonging to a group.

      In order to have somelines stand alone, they must be placed in a group.

      .. literalinclude:: pa_examples/parson_ex_group2.txt
         :language: rst

   .. tab:: Try It

      .. include:: pa_examples/parson_ex_group2.txt

   .. tab:: C++

      .. literalinclude:: pa_examples/parson_ex_cpp_group.txt
         :language: rst

   .. tab:: Try It

      .. include:: pa_examples/parson_ex_cpp_group.txt



The ``numbered`` option sets block numbers.

.. tabbed:: numbered

   .. tab:: Source

      .. literalinclude:: pa_examples/parson_ex_numbered.txt
         :language: rst

   .. tab:: Try It

      .. include:: pa_examples/parson_ex_numbered.txt

The ``maxdist`` option limits the number of distractors.

This example also demonstrates the use of ``adaptive`` option
that will attempt to simplify the problem
by removing distractors and helping with indentation after 3 failed attempts.

The ``adaptive`` option also adds a 'Help Me' button used to start the assistance.
Adaptive behaviors do not kick in automatically, but only on request.

.. tabbed:: maxdist

   .. tab:: Source

      .. literalinclude:: pa_examples/parson_ex_maxdist.txt
         :language: rst

   .. tab:: Try It

      .. include:: pa_examples/parson_ex_maxdist.txt

This example shows the use of paired distractors.

The problem has already been simplified by not assessing indentation.

.. tabbed:: paired

   .. tab:: Source

      .. literalinclude:: pa_examples/parson_ex_paired.txt
         :language: rst

   .. tab:: Try It

      .. include:: pa_examples/parson_ex_paired.txt

