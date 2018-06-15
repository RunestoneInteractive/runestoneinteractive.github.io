Video
=====

**Purpose**

As you may imagine, the job of the video directive is to embed a video in a page.

**Example in reStructured Text**

::

    .. video:: interactive_python_vid_1
       :controls:
       :thumb: ../_static/videothumb.png

       http://media.interactivepython.org/pythondsVideos/list_unique.mov
       http://media.interactivepython.org/pythondsVideos/list_unique.webm
YouTube
-------

.. youtube:: anwy2MPT5RE
    :height: 315
    :width: 560
    :align: left

.. reveal:: anwy2MPT5RE
   :showtitle: Show Source
   :hidetitle: Hide Source
   :modaltitle: Source for the example above

   .. code-block:: rst

      .. youtube:: anwy2MPT5RE
          :height: 315
          :width: 560
          :align: left

**Example**

.. video:: interactive_python_vid_1
   :controls:
   :thumb: ../_static/videothumb.png

   http://media.interactivepython.org/pythondsVideos/list_unique.mov
   http://media.interactivepython.org/pythondsVideos/list_unique.webm

**Required Arguments**

A unique identifier for the video. No spaces. This goes to the right of the ``.. video::`` term. In the example, the unique identifier chosen is ``interactive_python_vid_1``.

**Optional Arguments**

There are two optional arguments to the video directive.

``:controls:`` -  The controls argument is a flag that, if present, allows the library that runs these directives to generate the usual set of video controls: *play, pause, rewind, fast forward*. If ``:controls:`` is not present, the video will automatically play when the page is loaded.

``:thumb:`` - The thumb argument references an image that will serve as the thumbnail for this video. It requires an additional parameter: the path to the image that should serve as the thumbnail (in the example, that path is ``../_static/videothumb.png`` (relative paths to the location of the ``.rst`` file you are currently working in are fine). If the ``:thumb`` argument is used, then a thumbnail image will take the place of the video on the page until the reader clicks on the thumbnail. Clicking on the thumbnail will cause the full video to appear at full size on the page.  If the ``:thumb:`` directive is not present, then the video will appear on the page in its full size.


**Content**

The content lines of the video directive are the lines that follow the arguments, preceded by a blank line. You can specify as many video sources as you need.  (Usually I specify two videos, one in ``.mov`` format and the other in ``webm`` format.  This seems to cover all browsers.)

**Logs & Grading**

Video directives are not tied to the grading interface. Interactions logged in the database: each time a video is played, it is logged (so if you have logged-in users, you can have a log of who has played it; regardless, you can have a log of how many times it has been played).

**Uses**

Teachers have used the video directive to include demonstrative video to accompany conceptual explanations, or to bring in video explanations from other openly licensed sources (e.g. Khan Academy, interactivepython.org).


