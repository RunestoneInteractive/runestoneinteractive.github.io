Multiple Choice
===============

The multiple choice directive, ``..mchoice::``, allows for insertion of multiple choice questions, either with a single correct option or a checkbox question with multiple correct answers (there must be at least one correct answer for a multiple choice question).

(Previously, these directive options were in two different directives:  ``mchoicemf`` and ``mchoicema``. For now, these work, but they are deprecated -- you should use ``mchoice`` if you are writing new questions.)


**Examples in reStructured Text**

Multiple Choice with One Correct Answer

::

    .. mchoice:: question1_1
       :answer_a: Python
       :answer_b: Java
       :answer_c: C
       :answer_d: ML
       :correct: a
       :feedback_a: Yes, Python is a great language to learn, whether you are a beginner or an experienced programmer. You can write many different styles of programs using the Python language.
       :feedback_b: Java is a good object oriented language but it has some details that make it hard for the beginner.
       :feedback_c: C is an imperative programming language that has been around for a long time, but it is not the one that we use.
       :feedback_d: No, ML is a functional programming language.  (You can use Python to write functional programs as well!)

       What programming language does this site help you to learn?

Multiple Choice with Multiple Answer(s)

::

    .. mchoice:: question1_2
       :multiple_answers:
       :answer_a: xyZ
       :answer_b: new_var_3
       :answer_c: 3things
       :answer_d: hello-there
       :correct: a,b
       :feedback_a: Any combination of letters is a valid variable name in Python.
       :feedback_b: Underscores are acceptable to include in Python variable names, as long as they are not the first character in the variable name.
       :feedback_c: Variable names can't begin with digits in Python.
       :feedback_d: Hyphens and dashes are not acceptable characters to include in variable names in Python.

       Which of these are valid variable names in Python? (Choose all that are correct)

**Examples**

.. mchoice:: question1_1
    :answer_a: Python
    :answer_b: Java
    :answer_c: C
    :answer_d: ML
    :correct: a
    :feedback_a: Yes, Python is a great language to learn, whether you are a beginner or an experienced programmer. You can write many different styles of programs using the Python language.
    :feedback_b: Java is a good object oriented language but it has some details that make it hard for the beginner.
    :feedback_c: C is an imperative programming language that has been around for a long time, but it is not the one that we use.
    :feedback_d: No, ML is a functional programming language.  (You can use Python to write functional programs as well!)

    What programming language does this site help you to learn?

.. mchoice:: question1_2
    :multiple_answers:
    :answer_a: xyZ
    :answer_b: new_var_3
    :answer_c: 3things
    :answer_d: hello-there
    :correct: a,b
    :feedback_a: Any combination of letters is a valid variable name in Python.
    :feedback_b: Underscores are acceptable to include in Python variable names, as long as they are not the first character in the variable name.
    :feedback_c: Variable names can't begin with digits in Python.
    :feedback_d: Hyphens and dashes are not acceptable characters to include in variable names in Python.

    Which of these are valid variable names in Python? (Choose all that are correct)

**Required Arguments**

Unique identifier for the question, e.g. ``question1_2``. You also must have at least ``answer_a``, and the ``correct`` argument.

The value for the ``correct`` argument must correspond to an answer you've included, e.g. if you have included ``:answer_a:`` and ``:answer_b:`` only, you cannot use ``:correct: c``.

For *Multiple Choice Multiple Answer*, you may have more than one correct answer, comma-separated, as seen in the raw RST examples above. For *Multiple Choice Single Answer*, you must have only one correct answer.

**Optional Arguments**

``:multiple_answer:`` - This argument determines whether the question may have multiple correct answers with checkboxes, as above (including this option means you get the multiple answers format).

*Multiple Choice Single Answer*

``:answer_a:``, ``:answer_b:``, ``:answer_c:``, ``:answer_d:``, ``:answer_e:``  You can provide up to five different possible correct answers, like so. (See **required arguments** above.)

``:feedback_a:``, ``:feedback_b:``, ``:feedback_c:``, ``:feedback_d:``, ``:feedback_e:``  Each answer can have its own feedback. If there is feedback for one answer, there should be feedback for each answer. We recommend that thoughtful feedback be included for every multiple choice question.


*Multiple Choice Multiple Answer*

``:answer_a:``, ``:answer_b:``, ``:answer_c:``, ``:answer_d:``, ``:answer_e:``  You can provide up to five different possible correct answers. (See **required arguments** above.)

``:feedback_a:``, ``:feedback_b:``, ``:feedback_c:``, ``:feedback_d:``, ``:feedback_e:``  Each answer can have its own feedback. If there is feedback for one answer, there should be feedback for each answer. We recommend that thoughtful feedback be included for every multiple choice question, and that question writers consider how feedback may be useful for questions which have multiple correct answers!


