What is Runestone
=================

Runestone Interactive started out as a moment of clarity, with a vision of how I wanted to write textbooks.  Over the last five years it has evolved and changed in unexpected ways.  Even amongst people who care about this project a lot it was hard to pin down a way to communicate exactly what Runestone Interactive has become.  So I want to use this post to try to nail it down.

Online Open Source Interactive Textbooks
----------------------------------------

Most people know Runestone because of our textbooks.   What started out as *How to Think Like a Computer Scientist: Interactive Edition* has grown to include *Problem Solving with Algorithms and Data Structures using Python*, *Programs, Information, and People*, The *AP CS A  Review in Java*, *Big Ideas in Computer Science* and more.  The fact that they continue to be served from interactivepython.org is (as Douglas Adams would say) "increasingly inaccurate."   As of this writing over 500 high schools and colleges have adopted one or more of these textbooks In their curricula.

When an instructor decides to adopt a Runestone book for use in their course they can do so in two ways.   They may choose to give their students a link to one of the "open books" or they may choose to build a "custom course."  The open books are simply versions of each textbook that do not require a login.  These books are great for individual learners that want to work through a book on their own time at their own pace.  When an instructor chooses to build a custom course they get a copy of the book at a unique URL just for their class.  There are a number of benefits to going this route:

* The teacher can decide when or if to incorporate changes from the master copy of the textbook.
* The teacher can customize the book by reordering chapters or even removing chapters from the book.
* The teacher can create and publish assignments for their students
* The teacher can grade assignments and provide feedback for their students
* The teacher can observe the progress of the class or review the activities of an individual student.  Knowing what your students really do is a great help in preparing for class.
* Soon, Runestone will integrate with popular learning management systems.  Both sides have a ways to go before the integration is seamless, and both sides are working on it.

We never set out to make a course management system (lite) but there are just so many advantages to having all the data collection capabilities of an interactive textbook that we feel they are important.

Authoring Tools
---------------

What we did set out to make initially is a great set of interactive book authoring tools.  Our Big Hairy Audacious Goal was and is to become the LaTeX of the interactive textbook publishing world.  In the beginning writing an interactive textbook was equal parts writing and coding.  Runestone aims to remove the coding part so you can just focus on the writing.

To accomplish this we have created a set of HTML components for things like multiple choice questions, interactive code, code visualizations and many more.  If you don't have a sense for what kinds of things you can do with Runestone Interactive you should take a look at `The Overview <https://runestone.academy/runestone/static/overview.html>`_.  When the page is loaded simple the HTML components are rendered by a bunch of JavaScript and CSS to create the Runestone Components you see in the interactive books.

But nobody wants to write books in HTML!  So, we created a set of extensions for a simple markup language called `restructuredText <http://docutils.sourceforge.net/docs/user/rst/quickref.html>`_.  The restructuredText markup language lets you do all of the things you would expect to do in a language for writing, make lists, include images, footnotes, etc. etc.  In addition our extensions make it really easy to add   interactive components to your document.  For example to make an activecode component with runnable, editable code you would simply write the following in your text:

::

    .. activecode:: codeid
       :language: python

       print("hello world!")

The restructured text would be compiled into the html component:

::

    <textarea data-component="activecode" data-language="python">
    print("hello world")
    </textarea>

In the interactive textbook, after the Javascript and CSS do their magic  it looks like this:

.. image:: images/activecode.png

This three step process may seem complicated but it provides a lot of flexibility.  If you prefer  `markdown  <http://zverovich.net/2016/06/16/rst-vs-markdown.html>`_ over restructuredText you can still write an interactive book by just dropping in the html into your markdown document.  If you prefer another language like mediaWiki or something that supports its own macros, you can even write your own macros for that language that compile to the HTML.

The best thing is, you don't have to write an entire book to take advantage of the interactive tools.  You can use Runestone to make lecture demonstrations, or set up labs or short tutorials for your students.  If you do that you can even host them on your own computer very easily.

Full documentation for all of the Runestone Components can be found at `The Runestone Home <http://runestoneinteractive.org/build/html/directives.html>`_   If you have a suggestion for a new interactive component, or would like to help with the development and documentation of the Runestone Components please visit our page on `Github <https://github.com/RunestoneInteractive/RunestoneComponents>`_. If you would like to help out with any of the books they are all freely available `on github <https://github.com/RunestoneInteractive>`_.

The Runestone Server
--------------------

The last piece of the Runestone puzzle is the Runestone Server.  Most people can probably live a long and happy life without having to even think about the Runestone server.  It is the thing that provides web services to all of the Runestone Components and drives the instructor tools.  The server started out life as a necessity for me to use Runestone in my own classroom.  It has grown into a "textbook as a service" size server today, supporting over 13,000 students a day from all over the world.

However there are a handful of others out there who for whatever reason, privacy concerns, scalability concerns, or just more control, want to run their own server.  This is good as it makes the server better and provides a small base of others who can help add features and fix bugs.

The Runestone Server is built on top of the `web2py <http://web2py.com>`_ application framework.  I know, you've never heard of web2py, why would I do such a thing?  In 2011 it seemed like the right choice.  If I were starting again today it would definitely be a `Flask <http://www.pocoo.org/flask>`_ application.  I still hope to port everything to Flask one day.  But when I think about the opportunity cost of taking an entire summer to port the code versus using the summer to add new features to what is there, I lean heavily towards the new thing.  Eventually all of the bad decisions and shortcuts I've taken over the years will force me to do a rewrite.

If you're still with me, and are interested in helping out with server check out our `Github <https://github.com/RunestoneInteractive/RunestoneServer>`_ page, in particular have a look at the CONTRIBUTING document.
