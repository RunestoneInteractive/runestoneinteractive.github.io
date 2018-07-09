Multiple Choice
===============

The ``mchoice`` directive allows for insertion of multiple choice assessments. 
Questions may have either a single correct answer or a checkbox version with multiple correct 
answers. 


Synopsis
--------
The general format of the ``mchoice`` directive one of either **classic format**:

.. code-block:: rst

   .. mchoice:: unique_id
      :required: one or more answers
      :optional: feedback for answers

      + --- Content area ---
      |
      | A question or prompt with 0 or more lines of content
      |
      + --------------------

or **list format**:

.. code-block:: rst

   .. mchoice:: unique_id
      :optional: parameter value

      + --- Content area ---
      |
      | A question or prompt with 0 or more lines of content
      | followed by
      | A list of answers
      |
      + --------------------

Required Arguments
------------------

unique id
    A unique identifier after a space and the ``::`` in the ``mchoice`` directive.
    Valid identifiers must not contain spaces.
    You should also avoid the characters `` ` ``, ``,``, ``:``, and ``*``.

content area
    The ``mchoice`` directive must contain at least one line of content 
    regardless of the format chosen.

correct
    ``List``. One or more correct answers.

    This option is required if using **classic format**.

    - If a single value, the question renders with single selection buttons (Radio buttons).
    - If a list of values, the question renders with checkboxes, allowing multiple selection.

answer_a (through _e)
    ``String``. Up to 5 possible answers.

    - This option is applicable only if using **classic format**.
    - The value after the underscore must be in the range ``a`` through ``e``.
    - The option ``:answer_a:`` is **required**.
    - Plain text only.
    - The order of answers does not need to be fixed.
      Answers may be randomly shuffled.

Optional Arguments: Classic Format
----------------------------------

feedback_a (through _e)
    ``String``. Feedback specific to an answer.

    - This option is applicable only if using **classic format**.
    - Each answer can have its own feedback. 
    - Plain text only.
    - The value after the underscore must be in the range ``a`` through ``e``.
    - If there is feedback for one answer, there should be feedback for each answer. 
      
    We recommend that thoughtful feedback be included for every multiple choice question, 
    and that question writers consider how feedback may be useful for questions 
    which have multiple correct answers!


multiple_answers
    ``Boolean``. If present, forces checkbox behavior regardless of the actual number of correct answers.

    Implied if the ``:correct:`` option is present and contains a list of correct answers.

    .. literalinclude:: choice_examples/mc-ex1.txt
       :language: rst


random
    ``Boolean``. If present, indicates multiple correct answers are possible.


Optional Arguments: List Format
-------------------------------
An alternative method of specifying answers and feedback: 
Place an `unordered list <http://www.sphinx-doc.org/en/stable/rest.html#lists-and-quote-like-blocks>`__
at the end of the question text, in the following format. 

.. note:: 

   If your question text happens to end with an unordered list, 
   then place a comment, consisting of a paragraph containing only ``..`` at the end of the list. 
   For example:

   .. code-block:: rst

      .. mchoice:: unique_id

         Ask a question, which in this case, is followed by a list.

         -   This list is still part of the question text.

         ..

         -   Text for answer A.

The list format provides more flexibility in multiple choice questions:

- Up to 26 answers and feedback pairs may be provided.
- Unlike classic format, feedback for each answer is **required**.
- Your text may be multiple paragraphs, 
  including `images <http://www.sphinx-doc.org/en/stable/rest.html#images>`_
  and any other `inline <http://www.sphinx-doc.org/en/stable/rest.html#inline-markup>`_ or block markup. 
  For example: :math:`\sqrt(2)/2`. 
- Impossible to mistakenly associate incorrect answers and feedback.
  The classic format solely uses the letter to pair answers with feedback.

As earlier, if your feedback contains an unordered list, end it with a comment.
- Answers are always identified with a standard unordered list bullet: ``-``.
- Use a standard list ``-`` marker to identify feedback for incorrect answers.
- Use a ``+`` marker to identify feedback for correct answers.
- Just as in standard lists, separate a sublist with a blank line.
- An answer may contain only 1 feedback sublist.

Languages supported
-------------------

This directive is language agnostic.
Nothing is actually executed or interpreted.
It is up to the author to ensure the syntax and grammar within a clickable area
makes sense - no syntax checking on code is performed.


Sphinx configuration options
----------------------------

No directive specific configuration options exist.

Internationalization
....................

tbd.

Known limitations
-----------------
The list format directive is sensitive to paragraph spacing:

- The list spacing does not conform to the same rules as for standard 
  Sphinx `unordered lists <http://www.sphinx-doc.org/en/stable/rest.html#lists-and-quote-like-blocks>`__.
- The empty line between a sublist and a following list may be omitted.
- However, the empty line is required between a list and its sublist.

The 'Compare Me' button requires a book connected to a database for collecting grade statistics.
There is no way to disable this button, if not connected to a database.

There is no means to change the numbering of selected items 
(numbered, upper case, lower case, non-latin letters, etc).

There is difference in the spacing between the question and the first answer
in the classic and list formats.

Examples
--------
Multiple Choice with 1 correct answer.

.. tabbed:: example0

   .. tab:: Source

      .. literalinclude:: choice_examples/mc-ex0.txt
         :language: rst

   .. tab:: Try It

      .. include:: choice_examples/mc-ex0.txt


Multiple Choice with multiple correct answers.
This example shows both classic and list formats.

.. tabbed:: example1

   .. tab:: Classic Format

      .. literalinclude:: choice_examples/mc-ex1.txt
         :language: rst

   .. tab:: Try Classic

      .. include:: choice_examples/mc-ex1.txt

   .. tab:: List Format

      .. literalinclude:: choice_examples/mc-ex2.txt
         :language: rst

   .. tab:: Try List

      .. include:: choice_examples/mc-ex2.txt




The ``:multiple_answers:`` option can be used to force presenting the
multiple choice checkbox selections, even when there is only 1 correct answer.

.. tabbed:: example2

   .. tab:: Classic Format

      .. literalinclude:: choice_examples/mc-ex3.txt
         :language: rst

   .. tab:: Try Classic

      .. include:: choice_examples/mc-ex3.txt

   .. tab:: List Format

      .. literalinclude:: choice_examples/mc-ex4.txt
         :language: rst

   .. tab:: Try List

      .. include:: choice_examples/mc-ex4.txt


