Fill in the Blank
=================

The ``fillintheblank`` directive defines an assessment that
allows you to ask for a value to fill in the rest of a statement (in English or code).

Synopsis
--------
The general format of the ``fillintheblank`` directive is:

.. code-block:: rst

   .. fillintheblank:: unique_id

      + --- Content area ---
      |
      | A question or prompt with 0 or more lines of content
      |
      | followed by a list
      | One bullet list item for each blank to be rendered.
      |
      + --------------------

Required Arguments
------------------

unique id
    A unique identifier after a space and the ``::`` in the ``fillintheblank`` directive.
    Valid identifiers must not contain spaces.
    You should also avoid the characters `` ` ``, ``,``, ``:``, and ``*``.

content area
    The ``fillintheblank`` directive must contain a content area.
    The requirements for the content area:

    - The content block may contain zero or more ``|blank|`` literals in the question / prompt.
    - The content area must end with a list.  
      
      - The list must contain a field, like ``:this:`` followed by feedback.
      - Each bullet list item can only contain a single field and feedback pair per line of text.
      - The bullet list can contain more list items than blanks in the content area,
        but it cannot have less.

    For example:

.. code-block:: rst

   .. fillintheblank:: unique_id

      Question text goes here, with at least one |blank|, more are added like this: |blank|.

      - :answer: Feedback for blank 1
        :x: The last item of feedback mathes anything, regardless of content
      - :another: Feedback for the second blank
        :yet more: Feedback
        :.*: A wildcard for the second blank


If ``|blanks|`` are not used, then this directive will sequentially render 1 blank
for each list item encountered.

Answers are expected to match the order of blanks generated.
That is, the first answer must be associated with the first blank defined in the question / prompt area.

Answer fields containing text interpreted as `regular expressions <https://docs.python.org/2/library/re.html>`_.

Optional Arguments
------------------

casei
    ``Boolean``. If present, perform case insensitive comparisons between 
    values provided in ``blank`` fields and answer fields.

    The default performs case sensitive matching.
    
Languages supported
-------------------

The ``fillintheblank`` directive is language agnostic.
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

The markup ``|blank|`` conflicts with the standard Sphinx substitution syntax.
The blank markup should be placed within 'code' markup: \`\`|blank|\`\`,
otherwise Sphinx complains about an undefined reference to ``|blank|``.

Examples
--------
A simple example.

.. tabbed:: example1

   .. tab:: Source

      .. literalinclude:: fitb_examples/fitb-ex1.txt
         :language: rst

   .. tab:: Try It

      .. include:: fitb_examples/fitb-ex1.txt


Numeric answers
...............

The ``fillintheblank`` directive performs special processing if the answer appears numeric.

Numbers can be given in decimal, hex (0x10 == 16), octal (0o10 == 8), binary (0b10 == 2), 
or using scientific notation (1e1 == 10), both in answer fields and by the user when answering the question.

If a range of numeric values could be correct, a pair of numbers are used.
The second value indicates the tolerance allowed.

This example uses a sphinx directive in the content area of the fill in the blank
and checks correct answers against a range of values:

.. tabbed:: example2

   .. tab:: Source

      `sphinx.ext.mathjax <https://www.mathjax.org/>`__
      is required for this example to render correctly.

      .. literalinclude:: fitb_examples/fitb-ex2.txt
         :language: rst

   .. tab:: Try It

      .. include:: fitb_examples/fitb-ex2.txt


If a ``|blank|`` is not present, 
then the directive will append one for each bullet list item in the answer area.

The answer fields are appended immediately after the question content.

.. tabbed:: example3

   .. tab:: Source

      .. literalinclude:: fitb_examples/fitb-ex3.txt
         :language: rst

   .. tab:: Try It

      .. include:: fitb_examples/fitb-ex3.txt

How answer fields are parsed
............................

The text within an answer field is actually interpreted as a
`regular expression <https://en.wikipedia.org/wiki/Regular_expression>`_.
This means that when creating your answer fields, some characters may need *escaping*.
That is, if you want to use a character in your answer that also is a special character
in a `Python regular expression <https://docs.python.org/2/library/re.html>`_, 
then you'll need to precede it with a ``\`` character.
For example:

.. tabbed:: example4

   .. tab:: Source

      Note that in this example, the ``:`` character also needs an escape.
      Although it's not a special character in this context,
      it is used by the ``fillintheblank`` directive 
      to determine the start and end of the answer field.

      .. literalinclude:: fitb_examples/fitb-ex4.txt
         :language: rst

   .. tab:: Try It

      .. include:: fitb_examples/fitb-ex4.txt

Another simple example that requires escapes:

.. tabbed:: example5

   .. tab:: Source

      .. literalinclude:: fitb_examples/fitb-ex5.txt
         :language: rst

   .. tab:: Try It

      .. include:: fitb_examples/fitb-ex5.txt
