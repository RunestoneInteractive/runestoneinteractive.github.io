YouTube and Vimeo
=================
The ``youtube`` directive embeds content from http://www.youtube.com directly in a page.

The ``vimeo`` directive embeds content from http://www.vimeo.com directly in a page.

Synopsis
--------
The general format of the ``youtube`` directive is:

.. code-block:: rst

   .. youtube:: youtube video id
      :options:

The general format of the ``vimeo`` directive is:

.. code-block:: rst

   .. vimeo:: vimeo video id
      :options:

Both the ``vimeo`` and ``youtube`` directives take the same options (with one exception).

Required Arguments
------------------

id
    This must be the ID defined for this video by YouTube or Vimeo, respectively.

content area
    Neither the ``vimeo`` or ``youtube`` directive use a content area.

Optional Arguments
------------------

align
    ``Enumeration``. Define video horizontal alignment.
    
    One of ``left``, ``right``, or ``center`` is allowed. The default is ``left``.

divid
    ``String``. Define a runestone id for this video. YouTube only.

    The default divid is the YouTube video id.
    
    This is provides backward compatibility when converting HTML5 hosted videos 
    to the YouTube platform.
    Or use this if you want to use a different descriptor to reference rather than the YouTube video id.

height
    ``Integer``. Define video height in pixels.  
    Default height is 281 pixels.

http
    ``Enumeration``. Define default transport.

    One of ``http`` or ``https`` is allowed. The default is ``http``.


width
    ``Integer``. Define video width in pixels.
    Default width is 500 pixels.


Languages supported
-------------------

tbd.

Sphinx configuration options
----------------------------

No directive specific configuration options exist.

Internationalization
....................

tbd.

Known limitations
-----------------

The ID can only include the video ID.
Adding a time as in ``&t=3m35s`` or ``&start=90s`` breaks the video.

Can't loop video or link to youtuberepeater.com.

No way to enable closed captioning on by default.


Examples
--------

.. tabbed:: example1

   .. tab:: Source

      .. literalinclude:: video_examples/youtube-ex1.txt
         :language: rst

   .. tab:: Try It

      .. include:: video_examples/youtube-ex1.txt


