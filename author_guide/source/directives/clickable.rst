Clickable Area
==============
The ``clickablearea`` directive defines an assessment that interprets mouse clicks in the content area.


Synopsis
--------
The general format of the ``clickablearea`` directive is:

.. code-block:: rst

   .. clickablearea:: unique_id
      :required: parameter value

      + --- Content area ---
      |
      | A table in docutils 'grid table format'
      |
      | or
      |
      | text with :click-correct: text :endclick: 
      | and
      | text with :click-incorrect: text :endclick:
      | markup
      |
      + --------------------

Required Arguments
------------------

unique id
    A unique identifier after a space and the ``::`` in the ``clickablearea`` directive.
    Valid identifiers must not contain spaces.
    You should also avoid the characters `` ` ``, ``,``, ``:``, and ``*``.

content area
    The ``clickablearea`` directive must contain at least one line of content.

    The content area has relatively strict formatting requirements.
    The content area must contain either a table
    in `grid table format <http://docutils.sourceforge.net/docs/ref/rst/restructuredtext.html#grid-tables>`__
    or text with special formatting options embedded in the text.

    If the content area contains a table, the ``:table:`` option must be set.

    If the content area contains anything else, the ``:iscode:`` option must be set.

    A space must separate the last directive option from the content area.


question
    ``String``. Instructions describing what is expected for a correct response.

iscode
    ``Boolean``. If present, the content area will expect text with special format strings

    - ``:click-correct:`` -- define the start of a correct section of text.
    - ``:click-incorrect:`` -- define the start of an incorrect section of text.
    - ``:endclick:`` -- define the end of a marked section of text, either correct or incorrect.

      Each click must end with a matching ``:endclick:``

    For example:

    .. code-block:: rst

       .. clickablearea:: question1
          :question: Click the rainbow color(s)
          :iscode:

          :click-correct:Red:endclick:
          :click-incorrect:Gold:endclick:
          :click-correct:Blue:endclick:
          :click-incorrect:Black:endclick:

table
    ``Boolean``. If present, the content area must contain a 
    `grid table <http://docutils.sourceforge.net/docs/ref/rst/restructuredtext.html#grid-tables>`__
    and the directive must set the ``:correct:`` and ``:incorrect:`` options.

    For example:

    .. code-block:: rst

       .. clickablearea:: question2
          :question: Click the rainbow color(s)
          :table:
          :correct: 1,0;2,2;3,1;3,3;4,2
          :incorrect: 2,1;2,3;3,2;4,1;4,3

          +-------+---------+--------+
          |  Red  |  Orange | Yellow |
          +-------+---------+--------+
          | White |  Green  | White  |
          +-------+---------+--------+
          |  Blue |  White  | Indigo |
          +-------+---------+--------+
          | White |  Violet | White  |
          +-------+---------+--------+

    Table location numbering begins at 1.
    When referring to table cells, the upper left cell ('Red' in this example) is location ``1, 1``.
    The bottom right cell is at location ``4, 3``.

correct
    ``Formatted List``. A list of table coordinates that are marked as correct when clicked.


incorrect
    ``Formatted List``. A list of table coordinates that are marked as correct when clicked.

For both of the formatted lists, the list is built of cell coordinates.

- The first number is the table row.
- The second number is the table column.

  A column coordinate equal to ``0`` means all columns are selected.

- Each table coordinate is separated with ``;``.
- No white space is allowed.

Optional Arguments
------------------

feedback
    ``String``. Define incorrect feedback displayed when the **Check Me** button is pressed.

    The default is:
    
    .. code-block:: none

        Incorrect. You clicked on X of the Y correct elements and A of the B incorrect elements.

    The feedback for correct responses is always::

        You are Correct!


Languages supported
-------------------

The ``clickablearea`` directive is language agnostic.
Nothing is actually executed or interpreted.
It is up to the author to ensure the syntax and grammar within a clickable area
makes sense - no syntax checking is performed.

Sphinx configuration options
----------------------------

No directive specific configuration options exist.

Internationalization
....................

tbd.

Known limitations
-----------------

No syntax highlighting for ``:iscode:`` examples.

The text for all options (question, feedback, etc.) must appear on a single line.
No newlines are allowed.

There is no way to suppress carriage returns in the source,
which can make for long lines of text.
If your text editor wraps, this can make the source difficult to read.

There is no way to set the width or alignment of a table rendered using ``:table:``.
Columns widths will automatically adjust to fill the available space.

Examples
--------
A simple table example.

.. tabbed:: example1

   .. tab:: Source

      .. literalinclude:: clickable_examples/ca-ex1.txt
         :language: rst

   .. tab:: Try It

      Does any content show up in the tab or is it just includes?
      
      .. include:: clickable_examples/ca-ex1.txt

An ``:iscode:`` based example.

Note:
- The content are can contain whitespace.
- Multiple ``correct`` and ``incorrect`` sections can be specified on a single line.

.. tabbed:: example2

   .. tab:: Source

      .. literalinclude:: clickable_examples/ca-ex2.txt
         :language: rst

   .. tab:: Try It

      .. include:: clickable_examples/ca-ex2.txt

Another code-based example in which the complete text of every line is wrapped in either a
correct or incorrect section.
Note that the content area preserves white space everywhere it appears in the content area.

.. tabbed:: example3

   .. tab:: Source

      .. literalinclude:: clickable_examples/ca-ex3.txt
         :language: rst

   .. tab:: Try It

      .. include:: clickable_examples/ca-ex3.txt


.. tabbed:: example4

   .. tab:: Source

      .. literalinclude:: clickable_examples/ca-ex4.txt
         :language: rst

   .. tab:: Try It

      .. include:: clickable_examples/ca-ex4.txt



