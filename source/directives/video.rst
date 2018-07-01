Video
=====
The ``video`` directive embeds video in multiple formats on a page.

Synopsis
--------
The general format of the ``video`` directive is:

.. code-block:: rst

   .. ``video``:: unique_id
      :options:

      + --- Content area ---
      |
      | one or more references to video files or URL's
      |
      + --------------------

For an alternative to embed directly to youtube, use the :doc:`youtube` directive.

Required Arguments
------------------

unique id
    A unique identifier after a space and the ``::`` in the ``video`` directive.
    Valid identifiers must not contain spaces.
    You should also avoid the characters `` ` ``, ``,``, ``:``, and ``*``.

content area
    The ``video`` directive must contain at least one line of content.

    The content can be either a file reference to a video, 
    or a url to a video resource, one line per video.

    You can specify as many video sources as you need.  
    One in ``.mov`` format and another in ``.webm`` format is generally enough to cover most browsers.
    The first format that works is the one that is played.


Optional Arguments
------------------

controls
    ``Boolean``. If present, include the usual set of video controls: 
    
    - *Play*, *Pause*, *Rewind*, and *Fast Forward*. 
       
    If not present, the video will automatically play when the page is loaded.

loop
    ``Boolean``. If present, the video will loop continuously.  Default is ``false``.
    
preload
    ``Boolean``. If present, load the video in the background when the page loads.
    Default is ``false``. The video will begin to download when 'play' is pressed.
    
thumb
    ``String``. Define a thumbnail for the video.

    The string parameter defines the path to the image that should serve as the thumbnail::

        ../_static/videothumb.png 
        
    Relative paths are relative to the current file location.

    If ``:thumb:`` is used, then the thumbnail image is displayed until the reader clicks on the thumbnail. 
    Clicking on the thumbnail will cause the full video to appear at full size on the page.  
    
    If the ``:thumb:`` directive is not present, then the video will appear on the page in its full size.


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

tbd.

Examples
--------

.. tabbed:: example1

   .. tab:: Source

      .. literalinclude:: video_examples/video-ex1.txt
         :language: rst

   .. tab:: Show It

      .. include:: video_examples/video-ex1.txt

Logs and Grading
----------------

Video directives are not tied to the grading interface. 
Interactions **are** logged in the database: each time a video is played, it is logged.

- If you have logged-in users, you can have a log of who has played it. 
- If login is not required, a log of how many times it has been played is retained.


