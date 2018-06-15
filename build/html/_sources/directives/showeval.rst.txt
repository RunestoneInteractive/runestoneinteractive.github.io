ShowEval Trace Mode
===================
The title directive ...


.. showeval:: showEval_0
   :trace_mode: true

   eggs = ['dogs', 'cats', 'moose']
   ~~~~

   ''.join({{eggs}}{{['dogs', 'cats', 'moose']}}).upper().join(eggs)
   {{''.join(['dogs', 'cats', 'moose'])}}{{'dogscatsmoose'}}.upper().join(eggs)
   {{'dogscatsmoose'.upper()}}{{'DOGSCATSMOOSE'}}.join(eggs)
   'DOGSCATSMOOSE'.join({{eggs}}{{['dogs', 'cats', 'moose']}})
   {{'DOGSCATSMOOSE'.join(['dogs', 'cats', 'moose'])}}{{'dogsDOGSCATSMOOSEcatsDOGSCATSMOOSEmoose'}}



.. showeval:: showEval_1
  :trace_mode: false

  eggs = ['dogs', 'cats', 'moose']
  ~~~~

  ''.join({{eggs}}{{['dogs', 'cats', 'moose']}}).upper().join(eggs)
  {{''.join(['dogs', 'cats', 'moose'])}}{{'dogscatsmoose'}}.upper().join(eggs)
  {{'dogscatsmoose'.upper()}}{{'DOGSCATSMOOSE'}}.join(eggs)
  'DOGSCATSMOOSE'.join({{eggs}}{{['dogs', 'cats', 'moose']}})
  {{'DOGSCATSMOOSE'.join(['dogs', 'cats', 'moose'])}}{{'dogsDOGSCATSMOOSEcatsDOGSCATSMOOSEmoose'}}

Synopsis
--------

.. code-block:: none

   .. title:: unique_id
      :required: parameter value

      + --- Content area ---
      |
      | one or more lines of code in a supported language
      |
      + --------------------

Required Arguments
------------------

unique id
A unique identifier after a space and the ``::`` in the title directive.
Valid identifiers must not contain spaces.
You should also avoid the characters `` ` ``, ``,``, ``:``, and ``*``.

content area
The title directive must contain at least one line of content.

Optional Arguments
------------------

``:nopre:``
    **Boolean**. Prevents a ``<pre></pre>`` element from getting created in the page.

``:caption:``
    **String**. Define a caption for the title directive.

Languages supported
-------------------

tbd

Sphinx configuration options
----------------------------

tbd

Internationalization
....................

Known limitations
-----------------

tbd

Examples
--------

You can embed disqus discussions:

::

    .. title::
        :required: value 1
        :optional:



