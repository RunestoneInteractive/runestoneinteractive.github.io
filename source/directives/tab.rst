Tab Groups
==========
The ``tabbed`` directive is a container that allows splitting related content
into selectable tabs, viewable one at a time.

Synopsis
--------
The general format of the ``tabbed`` directive is:

.. code-block:: rst

   .. tabbed:: unique_id

      .. tab:: Tab #1

         + --- Content area #1 ---
         |
         | one or more lines of content
         |
         + -----------------------

      .. tab:: Tab #2

         + --- Content area #2 ---

      .. tab:: Tab #N

         + --- Content area #N ---

There is no hard limit on the maximum number of tabs allowed.
On narrow pages, the tabs will adjust to fit the overall tabbed content.
However, too many tabs can impair usability more than they improve it.
Use your judgement to see what works in your environment.


Required Arguments
------------------

unique id
    A unique identifier after a space and the ``::`` in the ``tabbed`` directive.
    Valid identifiers must not contain spaces.
    You should also avoid the characters `` ` ``, ``,``, ``:``, and ``*``.

content area
    The ``tabbed`` directive must contain at least 1 child ``.. tab::`` directive.

    Any other content placed as an immediate child of the ``.. tabbed::`` directive is silently ignored.

    The ``.. tab::`` is only valid inside a ``.. tabbed::`` parent container.

**.. tab::**
    ``String``. Create a new tab and label the tab using the provided string.
    A label is required, and may contain spaces.

    If the tab contains a null content area,
    then the build process throws a warning and the tab will not appear in the rendered HTML.
    
    Any valid Sphinx or Runestone markup can reside within a tab.


Optional Arguments
------------------

No optional arguments are defined for this directive.

Languages supported
-------------------

The ``tabbed`` directive is language agnostic.
Nothing is actually executed or interpreted.

Sphinx configuration options
----------------------------

No directive specific configuration options exist.

Internationalization
....................

tbd.

Known limitations
-----------------

Currently, some Runestone directives do not function correctly in a tabbed container:

- :doc:`codelens`
- :doc:`showeval`

If a ``tabbed`` contain has the same unique id as another in the same document,
then no error or warning is displayed, but the conflicting ``tabbed`` container
will not display its children correctly.

Examples
--------

You can create a container that contains one or more tabs.

.. tabbed:: tabbed-ex1

   .. tab:: Source

      .. literalinclude:: tab_examples/tab-ex1.txt
         :language: rst

   .. tab:: Try It

      .. include:: tab_examples/tab-ex1.txt


Note that nearly every example in this directives manual used tabs to organize the
source code and live examples.

