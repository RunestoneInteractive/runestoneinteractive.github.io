Parsons Problems
================

The Parsons Problem directive, ``.. parsonsprob::``, allows for insertion of a 2D Parsons problem. In a Parsons problem, users are provided with the lines / blocks of code (in the left source area) needed to solve a problem and are asked to reorder them to create a solution (in the right answer area). The 2D version further asks users to specify how much to indent the code. This is semantically meaningful in Python and good code practice in other programming languages. In the problem below, the third line needs to be indented to be correct.

::

    .. parsonsprob:: parsons_problem_1

       Construct a block of code that correctly implements the accumulator pattern.
       -----
       x = 0
       for i in range(10)
          x = x + 1

.. parsonsprob:: parsons_problem_1

   Construct a block of code that correctly implements the accumulator pattern.
   -----
   x = 0
   for i in range(10)
	  x = x + 1

**Required Arguments**

The identifier after the ``::`` must be unique. No spaces.

**Optional Arguments**

``:adaptive:`` - If specified, then this option will offer help after a few failed attempts.  After more failures, it will incrementally simplify the problem.

``:language:`` - You can specify the language for the code. *python* is the default value, but other programming languages are possible: *java*, *javascript*, *html*, *c*, or *ruby*. In addition to these programming languages, you can also specify *natural* for plain text. The default language can be set in the book ``pavement.py`` file.

``:noindent:`` - If you do not want to use the 2D capability, this argument will indent blocks as you specify them (see below). This makes the problem significantly easier to solve.

``:maxdist:`` - If you specify distractors in the code, then this will specify the maximum number of distractors presented to the user.

``:order:`` - If you don't want the code to be randomly shuffled, you can specify the order of the blocks in a comma-separated list (e.g., 0,5,3,2,4,1).

**Content**

Place the question text after the arguments. Use ``-----`` to separate the question text from the code. The code should be specified in the correct order and indented properly. You can also group lines using ``=====`` as in the problem below. The code blocks will be shuffled randomly in the source area; press the *Reset* button on a problem to see this shuffling in action. To make the problem more difficult, you can enter distractors that are not part of the solution. These lines or blocks are marked by placing ``#distractor`` after the line. You can pair one or more distractors with a correct code block by marking it with ``#paired``. When shuffled, these will be kept together with the correct code block (see below).

::

    .. parsonsprob:: parsons_problem_2
       :noindent:

       Construct a function that returns the max value from a list.
       -----
       def findmax(alist):
       =====
    	  if len(alist) == 0:
    		 return None
       =====
    	  curmax = alist[0]
    	  for item in alist:
       =====
    		 if item > curmax:
       =====
             if item > curmax: #paired
       =====
    			curmax = item
       =====
    	  return curmax
       =====
          return CurMax #distractor


.. parsonsprob:: parsons_problem_2
   :noindent:

   Construct a function that returns the max value from a list.
   -----
   def findmax(alist):
   =====
      if len(alist) == 0:
         return None
   =====
      curmax = alist[0]
      for item in alist:
   =====
         if item &gt; curmax:
   =====
         if item &lt; curmax: #paired
   =====
            curmax = item
   =====
      return curmax
   =====
      return CurMax #distractor


