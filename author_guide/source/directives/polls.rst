Poll
====
The ``poll`` directive allows students to vote or rate topics on a scale.

Synopsis
--------
The general format of the ``poll`` directive is:

.. code-block:: rst

   .. poll:: unique_id
      :optional: parameter value

      + --- Content area ---
      |
      | A question or prompt
      |
      + --------------------

Required Arguments
------------------

unique id
    A unique identifier after a space and the ``::`` in the ``poll`` directive.
    Valid identifiers must not contain spaces.
    You should also avoid the characters `` ` ``, ``,``, ``:``, and ``*``.

Optional Arguments
------------------

content area
    The ``poll`` directive should contain at least one line of content to
    serve as a prompt for the poll.

allowcomment
    ``Boolean``. If present, renders a comment box underneath the poll.
    Default is no comment box.

option_N (through 10)
    ``String``. Define up to 10 a manually specified entries.
    The provided parameter defines the text displayed for this option.

    - The value after the underscore must be in the range ``1`` through ``10``.  
    - Plain text only.
    - The order defined also specifies the rendering order.
    - This option is ignored if ``:scale:`` is present.

scale
    ``Integer``. Implements the "On a scale of 1 to N" type method of poll.
    The provided parameter defines the maximum scale value.

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
Polls require a backing database to be useful.

Polls are always oriented vertically.
There is no way to change the orientation of the option buttons.

The question text must be plain text.
No embedded Sphinx markup or HTML formatting is allowed.

There is no upper bound on the ``:scale:`` value.
A large value could cause long page loads and take large amounts of space.

There is no check when using both both ``:scale:`` and ``:option_N:``.
If the scale option is used, 
then the ``:option_N:`` options are ignored.

Examples
--------
A simple example using the ``:scale:`` option with comments enabled.

.. tabbed:: example1

   .. tab:: Source

      .. literalinclude:: poll_examples/poll-ex1.txt
         :language: rst

   .. tab:: Try It

      .. include:: poll_examples/poll-ex1.txt

An example using ``:option_N:`` options to manually configure choices.

.. tabbed:: example2

   .. tab:: Source

      .. literalinclude:: poll_examples/poll-ex2.txt
         :language: rst

   .. tab:: Try It

      .. include:: poll_examples/poll-ex2.txt

Note that a 'null poll' won't throw any warnings, but does not render anything useful in your book.

.. tabbed:: example3

   .. tab:: Source

      .. literalinclude:: poll_examples/poll-ex3.txt
         :language: rst

   .. tab:: Try It

      .. include:: poll_examples/poll-ex3.txt

This might happen if you make a mistake indenting your poll markup.

