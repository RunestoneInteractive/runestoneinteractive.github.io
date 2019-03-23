Reveal
======
The ``reveal`` hides content until a 'Show' button is pressed.

Synopsis
--------
The general format of the ``reveal`` directive is:

.. code-block:: rst

   .. reveal:: unique_id
      :optional: parameter value

      + --- Content area ---
      |
      | one or more lines of initially hidden content
      | which can include any Runestone or Sphinx supported directives.
      |
      + --------------------

Required Arguments
------------------

unique id
    A unique identifier after a space and the ``::`` in the ``reveal`` directive.
    Valid identifiers must not contain spaces.
    You should also avoid the characters `` ` ``, ``,``, ``:``, and ``*``.

content area
    The ``reveal`` directive must contain at least one line of content.

Optional Arguments
------------------

showtitle
    ``String``. Define a label for the 'show' button. Default is ``Show``.

hidetitle
    ``String``. Define a label for the 'hide' button. Default is ``Hide``.

    This option only applies if the ``modal`` option is **not** used.

modal
    ``Boolean``. If defined, the revealed content is presented in a modal dialog.  Default is ``false``.

    The default behavior reveals content in-line.

modaltitle
    ``String``. Title of modal dialog window. Default is "Message from the author".

    This option only applies if the ``modal`` option is used.

instructoronly
    ``Boolean``. If provided the content and reveal button will only be visible to instructors.  The proposed use of this is to provide an instructor guide embedded in the book.



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

None.

Examples
--------

.. tabbed:: example1

   .. tab:: Source

      .. literalinclude:: re_examples/reveal-ex1.txt
         :language: rst

   .. tab:: Try It

      .. include:: re_examples/reveal-ex1.txt

Both show and hide buttons are easy to customize:

.. tabbed:: example2

   .. tab:: Source

      .. literalinclude:: re_examples/reveal-ex2.txt
         :language: rst

   .. tab:: Try It

      .. include:: re_examples/reveal-ex2.txt



Very useful for in class presentations, or for in book exercises where you want to keep a solution hidden.
Display inline, or in a dialog, as you prefer.


.. tabbed:: example3

   .. tab:: Source

      .. literalinclude:: re_examples/reveal-ex3.txt
         :language: rst

   .. tab:: Try It

      .. include:: re_examples/reveal-ex3.txt



