==================================
Runestone Directives Documentation
==================================

Each Runestone directive has a particular purpose. Each is detailed below, including:

* What each directive allows you to create
* The syntax for using each directive and parameter
* Examples, or links to examples, of how instructors have used these directives in interactive textbook work
* If applicable, how exercises created by these directives can be graded
* Available additional developer documentation/notes

Custom Runestone directives exist in the following general categories
where more detailed documentation can be found:

================= ===================================
Categories        Directives
================= ===================================
Working with Code .. toctree::
                     :titlesonly:

                     directives/activecode
                     directives/codelens
                     directives/datafile
                     directives/showeval

Containers        .. toctree::
                     :titlesonly:

                     directives/disqus
                     directives/reveal
                     directives/tab
                     directives/timed
                     directives/video
                     directives/youtube

Assessments       .. toctree::
                     :titlesonly:

                     directives/clickable
                     directives/dnd
                     directives/fitb
                     directives/choice
                     directives/parsons
                     directives/polls
                     directives/short
                     directives/qnum
================= ===================================

General Syntax
===============

All directives start out with ``..``, then a single space, 
followed by the name of the directive, and then ``::``, followed by a single space.
Most directives have a required argument of a unique identifier, 
which immediately follows the directive name,
for example:

.. code-block:: rst

   .. video:: interactive_python_vid_1

This unique identifier is used for logging, managing controls, and for testing Runestone components.

    .. admonition:: How unique?

       Most unique id's must be unique within the **entire** book.
       Some only need to be unique within a single document.
       We will mention which is which,
       in the documentation for each directive.
       However, in general you are best served defining a convention for globally unique id's
       and sticking with it for all Runestone directives.
       
       A duplicate id may or may not generate a warning and *will* cause problems.

Spacing, including indentation consistency, 
is very important in implementing directives inside ``.rst`` files. 
Any missed or incorrect space may cause unexpected errors, 
strange-looking pages, or may cause information not to display on the deployed pages in your online book, 
so it's worth checking your final product before releasing content to students.

Directives may have **required arguments**. 
In many cases, an argument that is a unique identifier for that particular directive's ``div`` id, 
will follow the ``::`` in the directive:

.. code-block:: rst

    .. video:: interactive_python_vid_1
       :thumb: ../_static/videothumb.png

Any required and optional arguments for a directive occur below that first line, 
one argument per line, surrounded by single ``:``'s. 
Some of those require parameters -- for example, the ``:thumb:`` addition for the ``video`` directive 
requires a path to a ``.png`` image for the thumbnail image that should appear for the video.

When reStructured Text files are *built* into static files in your Runestone textbook, 
the directives result in HTML and JavaScript inside those HTML files that make up your book.

Runestone is a `Sphinx <http://www.sphinx-doc.org/en/master/>`_ extension.
That means directives you can use in Sphinx will also work in Runestone.

Ensuring Accessibility in Runestone Components
==============================================
 
Currently we are working on making Runestone books more accessible by 
modifying Runestone Components. 
For general changes to accessibility see accessibility.css, 
located in RunestoneComponents/runestone/common. 
Current efforts to make our ebooks more accessible are as follows:
 
* Modifying highlight color of navigation bar for non-mouse and mouse users
* Styling Bootstrap buttons to improve contrast ratio up to WCAG AA compliance
* Inverting color of Bootstrap buttons in order to make selection more obvious for the visually impaired
 
Individual Runestone components can also be modified for more accessibility to users. 
Current efforts to modify the accessibility of individual components can be found below:
 
* Improving tabbing functionality in Activecode questions for non-mouse users
 
Helpful sites to learn about how to improve accessibility in Runestone ebooks include:
 
* https://www.w3.org/WAI/intro/wcag
* https://www.w3.org/WAI/intro/aria
 
Here are some tools to evaluate the above standards:
 
* https://www.w3.org/WAI/eval/Overview
 

