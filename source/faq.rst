:orphan:

Frequently Asked Questions
==========================

Updated:  December 16, 2015

What is Runestone Interactive?
------------------------------

Runestone is a project that has three main parts to it:

.. admonition:: Runestone Parts

   1.  A set of tools for writing interactive textbooks in restructuredText and other markup langauges.
   2.  A open source server/API that supports the interactive textbooks

       * Save and reload source code written in the book
       * Retrieve results and answers from quizzes
       * Grade homework problems right in the textbook
       * Create Assignments by grouping exercises

   3.  A set of open source textbooks written using the tools that you are free to use and modify in your own classes.
   4.  A Textbook hosting service that allows you and your students to access any of the textbooks written using the tools.

The Runestone project was originally conceived as only parts 1 and 2.  But it became clear very quickly that few people want to write their own textbooks, so part 3 was born, especially with the encouragement of our publisher at Franklin Beedle who allowed us to put our paper textbook online in interactive form.  Part 4 was conceived when it became clear that part 2 was too hard to install and configure for most people who just want to teach CS and not spend their days and nights configuring server software. :-)

Currently number 4 is being used by over 12,000 students a day in over 400 universities, colleges, and high schools. This number is growing by around 2,000 students each semester.

What Runestone is Not?
----------------------

It sounds better if  you say it in your best Yoda voice.

I never wanted Runestone to be a course management system. I still don't. In my opinion there are already plenty of mediocre to good course management systems out there.  I don't want to make yet another.  However circumstances, and other instructors keep pushing Runestone in that direction.  I'm going kicking and screaming.  I would much rather integrate than reinvent.  Making online grade books is a losing proposition, as everyone has their own idea of how the "best" gradebook should work.  I brought this on myself, the moment I said "hey, self, why not make a nice little grading interface so you can grade all of the assignments right in the book?"  I thought that would be handy, and much better than downloading a bunch from moodle and running them.  They were all right there in the database, just click a button and run the program, then enter the grade.  Later the grades can be copied over to moodle or whatever.

The Rebellion continues, in the Google group I set up for instructors, I don't think I've had a single question about the content of the books.  Every single question and discussion falls under the category of "why  don't you have this <course management> feature?"  sigh.  Feature creep is real.


Help!  I cannot log in.  Every time I try to log in, I have to reset my password!
---------------------------------------------------------------------------------

In 99.99% of the cases, this is because you are confusing your email address with the username you were forced to enter when you register.  So, go through the password reset process and get yourself logged in again.  Then look in the upper right hand corner of the page and pull down the user menu (the one that looks like a person.)  Your username will be displayed at the top of that menu.  Yes, I get that most places just have you use your email address now, but my web development framework is old school.  This will change in the next major upgrade of the server (hopefully summer 2016)

How do I add students to my course?
-----------------------------------

You invite them, either in class or with an email.  Tell them to register at interactivepython.org and then give them the name of the course you created.  During the regsitration process they type in the name you used, and they are registered.  I usually just do this the first day of class to make sure everyone gets registered and then give them a little tour of the book and all of the things they can do.

In the future, we may look into importing a class from some LMS system like Moodle and others.


Can I build my own course and host it here?
-------------------------------------------

Yes, we are currently hosting many courses for many different institutions around the world.  In fact in 2013 one large institution had 800 students using one of the books.

The best approach is to use our system to build your own textbook.  This gives you several advantages as an instructor including:

* a simple grading interface for homework problems at the end of each chapter
* some simple reports on your students activities within the textbook.
* at a glance information about the multiple choice and fill in the blank questions embedded in the text.


How do I build my own course?
-----------------------------

.. admonition::  Steps to Build

   1.  First you should register yourself as a user on this site.  When you register you must pick a course.  Just use thinkcspy or pythonds, it doesn't matter as that will change when you build your own.
   2.  Then go to the `instructors page <http://interactivepython.org/runestone/admin/index>`_.
   3.  On this page you will see the links for listing and grading assignments and lots of other things.  Right now those won't show you anything, so move along to the `Create a Custom Course <http://interactivepython.org/runestone/designer>`_ link.
   4. Fill in the Project Name.  This should be a short one word description of your course like `luther150a.`  When your students register for the course this is the name they will have to type in to join your particular course.   No Spaces allwed in this name.
   5. The description can say a bit more about the course.
   6. The big choice is whether to use a ready-made book or to pick and choose sections from the repository of sections.  Most people just choose one of the pre-made books.
   7.  Its probably just fine to leave this at today's date.  If you set it into the future and then do some experimenting with assignments and quizzes today you won't be able to see your results because you are only shown things that come after the start date.


Is this site reliable enough to use in class?
---------------------------------------------

Yes.  All of the important parts of the book are served as static pages.  Everything else that happens either uses Javascript right in the browser, or background ajax calls that won't have any impact on the primary text.  We host this on a very reliable service and we monitor our traffic constantly. We use a content distribution network for increased scalability and reliability.  In the fall of 2015 we are serving over 12,000 students a day with almost zero downtime.


Why doesn't List and Grade Assignments doesn't show anything?
-------------------------------------------------------------

There could be two reasons.

*  You only see assignments or quiz questions that your students have attempted.  If you or your students haven't attempted any assignments yet then this report will be empty.

*  Check your course starting date.  If the starting date is in the future you won't see anything.  You can change your course start date `here <http://interactivepython.org/runestone/admin/startdate>`_.


Where do the assignments I make in the instructors interface show up for the students?
--------------------------------------------------------------------------------------

They don't.  You need to tell your students either in writing or verbally about the assignments.
This `blog post <http://reputablejournal.com/Organizing-your-Runestone-Course.html>`_ Gives you some good background on how you can write your own problem sets, and communicate your assignments to your students.

I want to reuse my course from last year, what should I do?
-----------------------------------------------------------

You can either just change your course start date, see above, or you can rebuild your course.   We recommend that you rebuild your course every so often to get the latest bug fixes etc.  Here is the link to `rebuild your course <http://interactivepython.org/runestone/admin/rebuildcourse>`_.

All the data from past terms is still saved in the database so students that want to go back and look at things from their past terms will be able to access their information, but nothing prior to your latest course start date will show up in any of your reports.

Unfortunately the assignment interface is not quite as easy.  If you really must re-use your course instead of creating  a new one for this year, send me an email and I can mark last years students as inactive.  Otherwise the grading interface will get cluttered with both current and past students.  But seriously, the whole idea here was that you can so easily create a new course each time you teach it, and then your past students can always get back to their book and assignments.

How do I update my course to get the latest bug fixes?
------------------------------------------------------

Here is the link to `rebuild your course <http://interactivepython.org/runestone/admin/rebuildcourse>`_.   We recommend that you do this every so often.  The instructors page will show you the current version of our software used to build the thinkcspy and pythonds books.  It will also show you the version for your own course.   If you course is out of date you will also get a flash message in the upper right corner of your browser window.


I was just experimenting and I want to delete my course
-------------------------------------------------------

Once you are done experimenting please delete your course from the instructors interface.  If this does not happen I may have to invent a way to go back and remove courses that were clearly created as an experiment but never really used by students.

What if I want to add a new section or chapter?
-----------------------------------------------

That would be awesome.  This whole book is open source.  You can grab a copy of the source on `github <http://github.com/bnmnetp/runestone>`_.  The source for thinkcspy and pythonds is in the source folder and there is a subfolder for each chapter.  If you want to make a whole new chapter then create a folder and follow the conventions of one of the other chapters.  There is full documentation for the markup language at `docs.runestoneinteractive.org <http://docs.runestoneinteractive.org>`_.  When you are finished make a pull request and we'll review your material and incorporate them into the book.

What if I want to add my own exercises?
---------------------------------------

You can add your own custom exercises by editing the assignments.rst file.  This file is meant for the descriptive or question text for a programming exercise.  Adding an exercise to this file does not automatically add it to the grading interface for your course, you still need to do that from the instructors interface.  See this `blog post <http://reputablejournal.com/Organizing-your-Runestone-Course.html>`_ for more information.

New exercises are always welcome and we would love to expand the number of exercises.  The simplest way is to go to the `github issues <http://github.com/bnmnetp/runestone/issues>`_ page and file a new issue.  In the description simply include the text for the exercise and which chapter you think it should go in.  We'll take it from there.  After we've added the exercise you can rebuild your book and it will be there.

What version of Python does your book use?
------------------------------------------

Ok, this is a question that has the potential to start nasty religious wars.  The technical answer is that this book uses a version of Python called `Skulpt <http://skulpt.org>`_.  It is entirely written in Javascript so that it runs right in the browser.  We think this is very cool.  Now some people get all crazy about whether they should teach Python 3 or Python 2.  The truth is that for CS1 and CS2 it really does not matter.  Skulpt can do print with or without parenthesis, and / can do true division or integer division and lets face it for CS1 that is really all that matters.   Sure, there are differences, but are you really going to start out by teaching your students about `dict_keys` and how they are different from a `list`.  If so, I think you are cruel and you should teach your students APL.  If you want to slant your teaching toward Python 3, you can do that with this book.  If you want to lean towards 2, you can do that too.  When you build your course there is a configuration parameter that lets you choose Python3, this forces you to use parenthesis when you print, and it makes python / default to true division, and // to integer division.


I think there is a bug in your book what should I do?
-----------------------------------------------------

Please let us know!  You can file bug reports on our `github issues page <http://github.com/bnmnetp/runestone/issues>`_.  Thanks!  If you don't have a github account then you can tweet me at iRunestone   or visit our `google.groups discussion <https://groups.google.com/forum/#!forum/runestoneinteractive>`_


I have a question that is not covered here!
-------------------------------------------

.. admonition::  Contact

   1.  Tweet me @iRunestone
   2.  Post the question on our google group
   3.  Send me a private email.  runestoneinteractive@gmail.com
