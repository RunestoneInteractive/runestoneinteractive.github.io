Timed Assessment
================
The ``timed`` directive is a container that adds a timer to any Runestone assessment or :doc:`activecode` directive.

Synopsis
--------

.. code-block:: rst

   .. timed:: unique_id
      :timelimit:

      + --- Content area ---
      |
      | one or more assessment directives, or an activecode directive
      |
      + --------------------

By default the feedback will be shown after the user clicks the "Finish Exam" button or 
after the time runs out for an exam with a specified duration.

To start the exam click on the "Start" button.

- Pause the time by clicking on the "Pause" button 
- Start it again by clicking on the "Resume" button.

When you pause the exam the questions will be hidden.  
There is also a clock icon that will display the time remaining 
if it is a timed exam and the time used otherwise when the reader hovers over it.
Questions are presented one at a time.

Because ``timed`` tests always display questions one at a time,
time limit or not,
a 'timed' assessment with 

- ``:nofeedback:``
- ``:noresult:``
- ``:notimer:``

provide a means to present many questions, one at a time,
but with no time or other statistics displayed.

A "Reset" button allows restarting a timed assessment under certain conditions.
Reset is only available if there is no record of a completed exam and the
localStorage does not reflect a partially completed exam.

Required Arguments
------------------

unique id
    A unique identifier after a space and the ``::`` in the timed directive.
    Valid identifiers must not contain spaces.
    You should also avoid the characters `` ` ``, ``,``, ``:``, and ``*``.

content area
    The timed directive must contain at least one line of content.

Optional Arguments
------------------

timelimit
    ``Integer``. Maximum time allowed to complete all assessment items in the container.

    Specify the maximum duration of the exam in minutes and it will display the time remaining.  
    If you don't include a duration it will keep track of the amount of time used and 
    give the user unlimited time to finish the exam.   

fullwidth
    ``Boolean``. Allows the items in the timed assessment to take the full width of the screen.

    Default is ``false``.

nofeedback
    ``Boolean``. Do not display feedback if defined.

    Default displays feedback.

noresult 
    ``Boolean``. Do not display score if defined.

    Default displays score.

notimer
    ``Boolean``. Do not display timer if defined.

    Default displays timer.


Languages supported
-------------------

tbd.

Sphinx configuration options
----------------------------

tbd.

Internationalization
....................

tbd.

Known limitations
-----------------

Runestone currently only supports one timed assessment per html page.  

ActiveCode questions are not graded, even if they contain unit tests.

'Hidden' assessment questions can be seen by students if they choose to examine the raw source of a web page.
Do not assume that 'hidden' assessment information is hidden from everyone.

The 'Reset' button does not reset exams.

Examples
--------

.. tabbed:: time-ex1

   .. tab:: Source

      .. literalinclude:: timed_examples/time-ex1.txt
         :language: rst

   .. tab:: Try It

      .. include:: timed_examples/time-ex1.txt

.. tabbed:: time-ex2

   .. tab:: Source

      .. literalinclude:: timed_examples/time-ex2.txt
         :language: rst

   .. tab:: Try It

      .. include:: timed_examples/time-ex2.txt


