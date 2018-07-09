Drag and Drop
=============

The ``dragndrop`` directive defines an assessment to match pairs of concepts using a drag and drop interface.

Synopsis
--------
The general format of the ``dragndrop`` directive is:

.. code-block:: rst

   .. dragndrop:: unique_id
      :optional: parameter value

      + --- Content area ---
      |
      | An optional question or instructions for the assessment.
      |
      + --------------------

Required Arguments
------------------

unique id
    A unique identifier after a space and the ``::`` in the ``dragndrop`` directive.
    Valid identifiers must not contain spaces.
    You should also avoid the characters `` ` ``, ``,``, ``:``, and ``*``.

Optional Arguments
------------------

content area
    The ``dragndrop`` directive may contain a content area.
    Plain text only. The content area is not processed in any way.
    No HTML or Sphinx markup is interpreted.

    The content area is displayed before the drag and drop items.

feedback
    ``String``. Define incorrect feedback displayed when the **Check Me** button is pressed.

    The default is:
    
    .. code-block:: none

        Incorrect. You got X correct and Y incorrect out of Z. You left A blank.

    If ``:feedback:`` is defined, it will appear after the default feedback.
    Otherwise, only the default feedback is displayed.

    Only 1 feedback field is permitted and is displayed regardless of which matches are incorrect.

    The feedback for correct responses is always::

        You are correct!

match_N
    ``String``. Up to 20 source / destination pairs.

    - ``N`` is a value from ``1`` through ``20``.
    - The source / destination pairs are separated using: ``|||``.
    - All other text is passed through without modification.
    - The order of match_N options does not matter.
      They will be randomly shuffled when rendered in your book.

    For example:

    .. code-block:: rst

       :match_1: Draggable element text|||Dropzone to be matched with text

Languages supported
-------------------

The ``dragndrop`` directive is language agnostic.
Nothing is actually executed or interpreted.

Sphinx configuration options
----------------------------

No directive specific configuration options exist.

Internationalization
....................

tbd.

Known limitations
-----------------

The text for matches must appear on a single line.
No newlines are allowed.

Examples
--------
A simple example.

.. tabbed:: example1

   .. tab:: Source

      .. literalinclude:: dnd_examples/dnd-ex1.txt
         :language: rst

   .. tab:: Try It

      .. include:: dnd_examples/dnd-ex1.txt


A completely empty directive is permitted.

.. tabbed:: example2

   .. tab:: Source

      A dnd with no items compiles without warning.

      .. literalinclude:: dnd_examples/dnd-ex2.txt
         :language: rst

   .. tab:: Try It

      But does not render anything useful.

      .. include:: dnd_examples/dnd-ex2.txt

Numbers for 'match' options need not start at 1,
however, they must be unique within a single ``dragndrop`` assessment.

.. tabbed:: example3

   .. tab:: Source

      .. literalinclude:: dnd_examples/dnd-ex3.txt
         :language: rst

   .. tab:: Try It

      .. include:: dnd_examples/dnd-ex3.txt

If a duplicate match is used, the directive will not compile.
The runestone compiler will display an error similar to:

.. code-block:: none

   WARNING: your_file.rst:173: (ERROR/3) Error in "dragndrop" directive:
   invalid option data: duplicate option "match_1".


