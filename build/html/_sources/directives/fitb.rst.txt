Fill in the Blank
=================

The fill in the blank Runestone directive, ``.. fillintheblank::``, 
allows you to ask for a value to fill in the rest of a statement (in English or code).

The basic format is the question or problem containing one or more placeholders for blanks to be filled in,
followed by a bulleted list containing sets of possible responses for each blank.

.. code-block:: none

   .. fillintheblank:: unique_identifier_string_no_spaces

      Question text goes here, with at least one |blank|, more are added like this: |blank|.

      - :answer: Feedback for blank 1
        :x: The last item of feedback mathes anything, regardless of content
      - :another: Feedback for the second blank
        :yet more: Feedback
        :.*: A wildcard for the second blank

Answer fields may contain `regular expressions <https://docs.python.org/2/library/re.html>`_.

**How answer fields are parsed**

The text within an answer field is actually interpreted as a
`regular expression <https://en.wikipedia.org/wiki/Regular_expression>`_.
This means that when creating your answer fields, some characters may need ``escaping``.
That is, if you want to use a character in your answer that also is a special character
in a `Python regular expression <https://docs.python.org/2/library/re.html>`_, 
then you'll need to precede it with a ``\`` character.
For example:

.. code-block:: none

   .. fillintheblank:: regexescapes1
      :casei:

      Windows system files are stored in: |blank|. 

      -   :C\:\\Windows\\system: Correct.
          :program files: Third party applications are stored here, not system files.
          :x: Try again.


   .. fillintheblank:: regexescapes2

      Python lists are declared using: |blank|. 

      -   :\[\]: Correct.
          :x: Try again.


Note that in the first example, the ``:`` character also needed an escape.
Although it's not a special character in this context,
it is used by Runestone to determine the start and end of the answer field.

**Examples in reStructured Text**

.. code-block:: none

   .. fillintheblank:: fitb1412
      :casei:

      Fill in the blanks to make the following sentence: "The red car drove away."

      The ``|blank|`` car drove ``|blank|``.

      -   :red: Correct.
          :x: Incorrect. Try 'red'.
      -   :away: Correct.
          :x: Incorrect. Try 'away'.

This example uses a sphinx directive in the content area of the fill in the blank
and checks correct answers against a range of values:

.. code-block:: none

   .. fillintheblank:: fill_2pi

      What is the solution to the following:

      :math:`2 * \pi =` ``|blank|``.

      - :6.28 0.005: Good job.
        :3.27 3: Try higher.
        :9.29 3: Try lower.
        :.*: Incorrect. Try again.

Numbers can be given in decimal, hex (0x10 == 16), octal (0o10 == 8), binary (0b10 == 2), 
or using scientific notation (1e1 == 10), both in answer fields and by the user when answering the question.

If a range of numeric values could be correct, a pair of numbers are used.
The second value indicates the tolerance allowed.

**Examples**

.. fillintheblank:: fitb1412
   :casei:

   Fill in the blanks to make the following sentence: "The red car drove away."

   The ``|blank|`` car drove ``|blank|``.

   -   :red: Correct.
       :x: Incorrect. Try 'red'.
   -   :away: Correct.
       :x: Incorrect. Try 'away'.

.. fillintheblank:: fill_2pi

   What is the solution to the following:

   :math:`2 * \pi =` ``|blank|``.

   - :6.28 0.005: Good job.
     :3.27 3: Try higher.
     :9.29 3: Try lower.
     :.*: Incorrect. Try again.

The fill in the blank directive can be combined with standard sphinx directives or nested within
other Runestone custom directives:

.. reveal:: reveal-skill-check-branch
   :showtitle: Show Skill Check
   :hidetitle: Hide Skill Check

   Given the following C++ program:

   .. code-block:: cpp
      :linenos:

      int main() {
        int a = 7;
        int b = 4;

        if (a<=b) { 
          a = 99;
        } else {    
          int t = a;
          a = b;
          b = t;
        }
        return a;                                     
      }

   .. fillintheblank:: fitb_conditions

      What value is returned from main? 

      - :4: Correct.
        :7: No, because the variable a is always modified in this program.
        :99: No. Since a is greater than b, the code on line 6 is never executed.
        :.*: Sorry, no. What is happening in the else block?



**Required Arguments**

A unique identifier after a space and the ``::`` in the fillintheblank directive. No spaces may be included in this identifier.

A content block with at least 1 blank.

A fillintheblank must end with a list.  The list must contain a field, like ``:this:`` followed by feedback.
Each bullet list item can only contain a single field and feedback pair per line of text.

The bullet list can contain 1 more list item than blanks in the content area,
but it cannot have less.


**Optional Arguments**

``casei``  - Perform case insensitive comparisons between values provided in ``blank`` fields and answer fields.


