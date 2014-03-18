Activecode
----------

Activecode has Many options:

::


    .. activecode:: codeexample1
       :nocanvas:  -- do not create a canvas element (optional)
       :nopre:     -- do not create a pre element (optional)
       :above:     -- position the canvas above the code (optional)
       :autorun:   -- run the example as soon as the page is loaded (optional)
       :caption:   -- add a caption below (optional)
       :include:   -- include code from another activecode use div_id as the parameter (optional)
       :hidecode:  -- Initally hide the editing window (optional)
       :language:  -- Is python by default, but could also be javascript or html
       :tour_1:
       :tour_2:
       :tour_3:
       :tour_4:
       :tour_5:
       
       print("My first program adds two numbers, 2 and 3:")
       print(2 + 3)


.. activecode:: codeexample1
   :above:
   :caption:   This is a caption

   print("My first program adds two numbers, 2 and 3:")
   print(2 + 3)


If you want to invisibly incorporate unittests into the code.

::

    .. activecode:: units1

       def add(a,b):
          return 4

       ====
       import unittestgui

       class myTests(unittestgui.unittest):

           def testOne(self):
               self.assertEqual(add(2,2),4,"A feedback string when the test fails")
               self.assertAlmostEqual(add(2.0,3.0),5.0,"Your function failed on inputs of 2.0 and 3.0")

       myTests().main()

.. activecode:: units1

   def add(a,b):
      return 4

   ====
   import unittestgui

   class myTests(unittestgui.unittest):

       def testOne(self):
           self.assertEqual(add(2,2),4,"A feedback string when the test fails")
           self.assertAlmostEqual(add(2.0,3.0),5.0,"Your function failed on inputs of 2.0 and 3.0")

   myTests().main()

Everything after the ``===`` will be invisible to the student.  If you leave out the ``====`` then the student will see all of the unit tests in the editing window.


CodeLens
--------

::

    .. codelens:: codelens_question
        :breakline: line number, (optional) if present this will pause the trace and ask a question
        :question: question text 
        :feedback: feedback text
        :correct: globals.tot    This can refer to any key in the stack trace locals.xxx or even line

        tot = 0
        prod = 1
        for i in range(10):
           tot = tot + i
           prod = prod * i


.. codelens:: codelens_question
    :question: What is the value of tot after the line with the red arrow executes?
    :breakline: 4
    :feedback: Use the global variables box to look at the current values of tot and i.
    :correct: globals.tot

    tot = 0
    prod = 1
    for i in range(10):
       tot = tot + i
       prod = prod * i

Video
-----

HTML 5
~~~~~~

::

    .. video:: videoinfo
        :controls:   -- show the controls if present
        :thumb: _static/activecodethumb.png   -- thumbnail image

        http://media.interactivepython.org/thinkcsVideos/activecodelens.mov
        http://media.interactivepython.org/thinkcsVideos/activecodelens.webm

YouTube
~~~~~~~

::

    .. youtube:: anwy2MPT5RE
        :height: 315
        :width: 560
        :align: left


Vimeo
~~~~~

::

        .. vimeo:: anwy2MPT5RE
            :height: 315
            :width: 560
            :align: left




Self-Check Questions
--------------------

Multiple Choice
~~~~~~~~~~~~~~~

Multiple choice questions with feedback for each incorrect response.

::

    .. mchoicemf:: question1_1
       :answer_a: Python
       :answer_b: Java
       :answer_c: C
       :answer_d: ML
       :correct: a
       :feedback_a: Yes, Python is a great language to learn, whether you are a beginner or an experienced programmer.
       :feedback_b: Java is a good object oriented language but it has some details that make it hard for the beginner.
       :feedback_c: C is an imperative programming language that has been around for a long time, but it is not the one that we use.
       :feedback_d: No, ML is a functional programming language.  You can use Python to write functional programs as well.

       What programming language does this site help you to learn?


.. mchoicemf:: question1_1
   :answer_a: Python
   :answer_b: Java
   :answer_c: C
   :answer_d: ML
   :correct: a
   :feedback_a: Yes, Python is a great language to learn, whether you are a beginner or an experienced programmer.
   :feedback_b: Java is a good object oriented language but it has some details that make it hard for the beginner.
   :feedback_c: C is an imperative programming language that has been around for a long time, but it is not the one that we use.
   :feedback_d: No, ML is a functional programming language.  You can use Python to write functional programs as well.

   What programming language does this site help you to learn?


Multiple choice with multiple answers

::

    .. mchoicema:: question1_2
       :answer_a: red
       :answer_b: yellow
       :answer_c: black
       :answer_d: green
       :correct: a,b,d
       :feedback_a: Red is a definitely on of the colors.
       :feedback_b: Yes, yellow is correct.
       :feedback_c: Remember the acronym...ROY G BIV.  B stands for blue.
       :feedback_d: Yes, green is one of the colors.

       Which colors might be found in a rainbow? (choose all that are correct)

.. mchoicema:: question1_2
   :answer_a: red
   :answer_b: yellow
   :answer_c: black
   :answer_d: green
   :correct: a,b,d
   :feedback_a: Red is a definitely on of the colors.
   :feedback_b: Yes, yellow is correct.
   :feedback_c: Remember the acronym...ROY G BIV.  B stands for blue.
   :feedback_d: Yes, green is one of the colors.

   Which colors might be found in a rainbow? (choose all that are correct)


Fill in the Blank
~~~~~~~~~~~~~~~~~

Fill in the blank with regular expression matching for the answer

::

    .. fillintheblank:: baseconvert1
       :correct: \\b31\\b
       :blankid: baseconvert1_ans1

       What is value of 25 expressed as an octal number (base 8) :textfield:`baseconvert1_ans1::mini`


Parson's
~~~~~~~~

Parson's Problems:

Question text comes first, then ``-----`` separates the question text from the code.  You provide the correct code, and the javascript takes care of mixing it up.
::

    .. parsonsprob:: question1_100_4

       Construct a block of code that correctly implements the accumulator pattern.
       -----
       x = 0
       for i in range(10)
          x = x + 1


You can also group statements using ``=====``  In the example below the for loop and its body will appear as one block to position in the problem.

::

    .. parsonsprob:: question1_100_4

       Construct a block of code that correctly implements the accumulator pattern.
       -----
       x = 0
       =====
       for i in range(10)
          x = x + 1
       =====
       print(x)


.. parsonsprob:: question1_100_4

   Construct a block of code that correctly implements the accumulator pattern.
   -----
   x = 0
   =====
   for i in range(10)
      x = x + 1
   =====
   print(x)


Disqus
~~~~~~


You can embed disqus discussions:

::

    .. disqus::
        :shortname: Your registered  shortname with disqus
        :identifier: discussion1  


Tabs and Tab Groups
~~~~~~~~~~~~~~~~~~~

You can create a section that contains several tabs.  This is useful for exercises, and in other situations where you may want to partially reveal content.

::

    .. tabbed:: exercise1

        .. tab:: Question 1
        
            Write a program that prints "Hello, world".
            
            .. activecode:: helloworld

                print("Hello, world")

        .. tab:: Discussion
        
            .. disqus::
                :shortname: interactivepython
                :identifier: helloworlddiscussion


.. tabbed:: exercise1

    .. tab:: Question 1
    
        Write a program that prints "Hello, world".
        
        .. activecode:: helloworld

            print("Hello, world")

    .. tab:: Discussion
    
        .. disqus::
            :shortname: interactivepython
            :identifier: helloworlddiscussion


Polls
~~~~~

Allow students to vote or rate things on a scale

::

    .. poll:: pollid1
       :scale: 10
       :allowcomment:

        On a scale from 1 to 10, how important do you think it is to have a polling directive in the Runestone Tools?

.. poll:: pollid1
   :scale: 10
   :allowcomment:

    On a scale from 1 to 10, how important do you think it is to have a polling directive in the Runestone Tools?

Reveal
~~~~~~

Very useful for in class presentations, or for in book exercises where you want to keep a solution hidden.

::

    .. reveal:: revealid1
        :showtitle: Reveal Content
        :hidetitle: Hide Content

        This content starts out hidden. It's visibility can be toggled by using the Show/Hide button.

        The reveal block can also contain other directives (ActiveCode, Disqus block, etc):

        .. activecode:: ac11

            print ("Hello, world")



.. reveal:: revealid1
    :showtitle: Reveal Content
    :hidetitle: Hide Content

    This content starts out hidden. It's visibility can be toggled by using the Show/Hide button.

    The reveal block can also contain other directives (ActiveCode, Disqus block, etc):

    .. activecode:: ac11

        print ("Hello, world")

