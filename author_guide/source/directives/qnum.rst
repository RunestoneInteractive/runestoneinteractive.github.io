.. qnum::
   :prefix: Ex-
   :start: 1

Controlling Question Numbering
==============================
The ``qnum`` directive provides control over question numbering.

Synopsis
--------
The general format of the ``qnum`` directive is:

.. code-block:: rst

   .. qnum::
      :prefix: character prefix before assessment number
      :suffix: character prefix after assessment number
      :start: start numbering with this value

The ``qnum`` directive does not use a content block or a unique id.

It does not directly render anything itself, 
but changes question number labels in other assessments.

If only one ``qnum`` directive exists in the file,
then the ``qnum`` directive effects all assessments in the current file.

If more than one ``qnum`` directive exists in the file,
then changes created by the ``qnum`` directive affect the file sequentially.
All questions that follow the ``qnum`` directive use the most recently defined ``qnum``.

``qnum`` values affect only the current file.

Required Arguments
------------------

No arguments are strictly required, however,
a ``qnum`` directive with no options has no effect.

Optional Arguments
------------------

prefix
    ``String``. Define characters before the question number.

    The default is no prefix for :doc:`choice` and ``Q-`` for 
    :doc:`parsons` and :doc:`short`.

suffix
    ``String``. Define characters after the question number.

    The default is no suffix defined.

start
    ``Integer``. Define the start for question numbering. Must be > ``0``.

    The first question encountered will begin with this number and increment by 1 afterwards.

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

Not all Runestone assessments currently render question numbers.
Those that do are:

- :doc:`choice`
- :doc:`parsons`
- :doc:`short`

Those that do not:

- :doc:`clickable`
- :doc:`dnd`
- :doc:`fitb`
- :doc:`polls`
- :doc:`activecode`, when in a :doc:`timed` container.


If **every** assessment in a file exists within a :doc:`tab` container,
then the ``qnum`` directive has no effect.
If even a single assessment is outside a tab group, then
assessments are numbered as expected, both those in and out of tab containers.

The ``:suffix:`` option does not change the ``:`` character between the 
number / suffix and whatever follows.
That is, the ``:`` is not considered part of the suffix.

Examples
--------
Using 

.. code-block:: rst

   .. qnum::
      :prefix: Ex-
      :start: 1

Changes question numbering as follows:

.. mchoice:: qnum-ex1

   Which colors are found in the rainbow?

   - Red

     + Yes, red is a correct rainbow color.

   - White

     - White is not a color found in a rainbow.

   - Blue

     + Yes, blue is a correct rainbow color.

   - Grey

     - Grey is not a color found in a rainbow.


.. parsonsprob:: qnum-ex2

   Construct a block of code that correctly implements 
   the <b>accumulator</b> pattern.
   -----
   x = 0
   for i in range(10):
       x = x + 1

.. shortanswer:: qnum-ex3

   What are the colors in the rainbow?

The following assessment is a timed exam that restarts question numbering
and appends to the numbers:

.. qnum::
   :suffix: -timed
   :start: 1

.. code-block:: rst

   .. qnum::
      :suffix: -timed
      :start: 1

Because the ``:prefix:`` was not set, 
the existing prefix *Ex* continues to be used.

.. timed:: qnum-time-ex1
   :nofeedback:
   :noresult:

   .. mchoice:: timed-q-ex1

      What color is a stop sign?

      -   red

          +   Red it is.

      -   brown

          -   Not brown.

      -   blue

          -   Not blue.

      -   gray

          -   Not gray.

   .. mchoice:: timed-q-ex2
      :multiple_answers:
      :correct: a, c
      :answer_a: red
      :answer_b: brown
      :answer_c: blue
      :answer_d: gray
      :feedback_a: Red it is.
      :feedback_b: Not brown.
      :feedback_c: Blue it is.
      :feedback_d: Not gray.

      What colors might you see in a rainbow?

   .. parsonsprob:: timed-qnum-ex3

       Construct a block of code that correctly implements 
       the <b>accumulator</b> pattern.
       -----
       x = 0
       for i in range(10):
           x = x + 1

   .. shortanswer:: timed-qnum-ex4

       What are the colors in the rainbow?



