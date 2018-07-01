Disqus
======

The ``disqus`` directive allows embedding discussions directly inline with content.

The directive inserts a hyperlink to pre-defined threaded Disqus discussion.

Synopsis
--------
The general format of the disqus directive is:

.. code-block:: rst

   .. disqus::
      :shortname: Your registered  shortname with disqus
      :identifier: discussion1

The ``disqus`` directive does not use a content area or a unique id.

Required Arguments
------------------

shortname
    Your registered shortname with disqus.

    The shortname will be used to link directly to your discussion on discuss::

       https://' + disqus_shortname + '.disqus.com

identifier
    A unique identifier for this discussion on disqus.

Optional Arguments
------------------

No optional arguments are defined for this directive.

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

Using Disqus does present some security concerns.

Examples
--------

.. tabbed:: example1

   .. tab:: Source

      .. literalinclude:: di_examples/disqus-ex1.txt
         :language: rst

   .. tab:: Run It

      .. include:: di_examples/disqus-ex1.txt


