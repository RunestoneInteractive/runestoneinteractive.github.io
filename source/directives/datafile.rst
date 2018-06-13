Datafile
========

The datafile directive works with activecode when you want to have the user read some data from a file.  Because we want the file to come from the browser, not some far away server, or from the user's local hard drive, we can fake files' existence in two different ways.

1.  We can put the data into ``pre`` element.  The id on the element serves as the filename.

2.  We can put the data into a ``textarea`` element.  Again the id on the element serves as the file name.  However, with a text area, the file data can be modified.

Both of these options can be achieved with the ``datafile`` directive.

**Examples in reStructured Text**

::

    .. datafile:: mydata.txt
       :edit:
       :rows: 20
       :cols: 60

       here is the first line in the data file
       also, this is the second line in the data file
       and this is the third line

::

    .. datafile:: mydata2.txt
       :rows: 20
       :cols: 60

       here is the first line in the data file
       also, this is the second line in the data file
       and this is the third line


This example will produce a text area that is 20 rows long and 60 columns wide.  The ``:edit:`` flag tells the directive to produce a textarea rather than a pre element.

**Examples**

.. datafile:: mydata.txt
   :edit:
   :rows: 20
   :cols: 60

   here is the first line in the data file
   also, this is the second line in the data file
   and this is the third line

.. datafile:: mydata2.txt
   :rows: 20
   :cols: 60

   here is the first line in the data file
   also, this is the second line in the data file
   and this is the third line



**Arguments**

The required argument is the 'filename' (this is not reliant on any actual filename, but is the filename you must inform users of so that they can perform file reading operations in activecode windows). In the examples it is ``mydata.txt`` and ``mydata2.txt``. This must be unique within the document as it does become the id of the element.

**Optional Arguments**

``:hide:``  -- This makes the file invisible.  This might be good if you have an exceptionally long file that you want to use in an example where it is not important that the student see all the data, or in an example when you want students to solve a problem dependent on file reading operations in which they should not be able to determine the answer by looking at the file. It will simply be included in the page so that the file can be used in programs (activecode blocks, etc).

``:edit:``  -- This flag makes the file into an editable file in a textarea. This is great if you want your students to be able run their program on different data from a file.  All they have to do is edit the textarea and rerun the program. TODO are edits saveable by users??

``rows``  -- This is for sizing the textarea.  The value has no effect on a pre element.  If the rows value is not provided, the directive will do its best to guess the number of rows within a reasonable number.

``cols``  -- Again this is for sizing the text area, and again, if not provided, the directive will come up with a reasonable value.



