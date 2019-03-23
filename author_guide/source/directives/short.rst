Short Answer
============
The ``shortanswer`` directive provides a free-form assessment that is stored
and can be manually graded by an instructor.

Synopsis
--------
The general format of the ``shortanswer`` directive is:

.. code-block:: rst

   .. shortanswer:: unique_id
      :optional:
      
      + --- Content area ---
      |
      | A question or prompt for the assessment.
      |
      + --------------------


A feedback region underneath user content displays

.. code-block:: none

   Your answer has not been saved yet!

in red background, until the 'Save' button is pressed.
Then the feedback region displays

.. code-block:: none

   Your answer has been saved.

in green background.
Each time the content is modified, the save warning is redisplayed
until 'Save' is pressed.

Required Arguments
------------------

unique id
    A unique identifier after a space and the ``::`` in the ``shortanswer`` directive.
    Valid identifiers must not contain spaces.
    You should also avoid the characters `` ` ``, ``,``, ``:``, and ``*``.

content area
    A question or prompt for the assessment.

Optional Arguments
------------------

optional
    ``Boolean``. If present, changes the assessment area background color,
    except for the feedback area, to light green.

Languages supported
-------------------

Not applicable.

Sphinx configuration options
----------------------------

No directive specific configuration options exist.

Internationalization
....................

tbd.

Known limitations
-----------------

Responses must be plain text only.
There is no 'upload' feature.

There is no option to set an initial height or width for the text area,
although users can resize it.

This directive requires a back end server to be useful.

There is no 'reset' or 'undo' as found in other directives.
Simply delete response text to reset to it's initial state.

This directive erroneously labels each assessment twice:

.. code-block:: none

   Q-1: Q-2: What colors are in the rainbow?

in green background.


Examples
--------
The default ``shortanswer`` appearance displays only the feedback region green.

.. tabbed:: example1

   .. tab:: Source

      .. literalinclude:: short_examples/short-ex1.txt
         :language: rst

   .. tab:: Try It

      .. include:: short_examples/short-ex1.txt


When ``:optional:`` is set,
the ``shortanswer`` appearance displays the entire assessment area green.

.. tabbed:: example2

   .. tab:: Source

      .. literalinclude:: short_examples/short-ex2.txt
         :language: rst

   .. tab:: Try It

      .. include:: short_examples/short-ex2.txt


