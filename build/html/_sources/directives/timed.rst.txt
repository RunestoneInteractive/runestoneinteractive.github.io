Timed Exam Questions
====================
You can add a timed exam using any of the assessment directives or an activecode directive.

By default the feedback will be shown after the user clicks the "Finish Exam" button or 
after the time runs out for an exam with a specified duration.

To start the exam click on the "Start" button.  You can pause the time by clicking on the "Pause" button and start it again by clicking on the "Resume" button.  When you pause the exam the questions will be hidden.  There is also a clock icon that will display the time remaining if it is a timed exam and the time used otherwise when the reader hovers over it.

Synopsis
--------

.. code-block:: none

   .. timed:: unique_id
      :timelimit:

      + --- Content area ---
      |
      | one or more assessment directives, or an activecode directive
      |
      + --------------------

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

``:timelimit:``
    **Integer**. Maximum time allowed to complete all assessment items

    Specify the maximum duration of the exam in minutes and it will display the time remaining.  
    If you don't include a duration it will keep track of the amount of time used and 
    give the user unlimited time to finish the exam.   

Languages supported
-------------------

tbd

Sphinx configuration options
----------------------------

tbd

Internationalization
....................

tbd

Known limitations
-----------------

Note that Runestone currently only supports one timed exam per html page.  

ActiveCode questions do not appear to get graded, even if they contain unit tests.

Examples
--------

You can embed disqus discussions:

::

    .. timed::
        :required: value 1
        :optional:



