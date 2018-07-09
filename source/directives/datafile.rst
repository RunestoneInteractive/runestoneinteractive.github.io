Datafile
========

The ``datafile`` directive works with :doc:`activecode` to emulate reading data from a file.

Synopsis
--------
The general format of the ``datafile`` directive is:

.. code-block:: rst

   .. datafile:: filename
      :options:

      + --- Content area ---+
      | 
      | zero or more lines of data
      | 
      + --------------------+

The id of the directive serves as the filename.
The filename can be referenced in an activecode code block as if it was a physical file
on the filesystem.

Required Arguments
------------------

The required argument is the 'filename' (actually a unique_id that simulates a physical file).
It is the filename you must inform users of 
so that they can perform file reading operations in activecode windows. 

This must be unique within the document as it does become the id of the element.
It does not have the same global uniqueness constraint that unique id's require.


Optional Arguments
------------------

cols 
    ``Integer``.
    Set the width of the textarea.
    If not set, then Runestone will size the area to the contents, or provide a default.

edit 
    ``Boolean``.
    Toggle whether a ``datafile`` is editable. If not set, then false.

    Editable text areas can also be resized by the user.
   
hide 
    ``Boolean``.
    Toggle whether a ``datafile`` is visible. If not set, then true.

    Why hide this element?  
    
    * If you have an exceptionally long file that you want to use in an example 
      where it is not important that the student see all the data. 
    * In an example when you want students to solve a problem dependent on file 
      reading operations in which they should not be able to determine the answer by looking at the file. 
      
    Hidden datafiles can still be referenced in code.

rows 
    ``Integer``.
    Set the height of the textarea.
    If not set, then Runestone will size the area to the contents, or provide a default.

Languages supported
-------------------

Python only at this time.

Sphinx configuration options
----------------------------

No directive specific configuration options exist.

Internationalization
....................

tbd

Known limitations and bugs
--------------------------

An empty ``datafile`` with no default content cannot determine a default size for itself.
If a blank data file is specified (no default content), 
then the rows and cols parameters must be set.


Examples
--------

A ``datafile`` with no optional parameters set.

.. tabbed:: example0

   .. tab:: Data Source

      .. literalinclude:: df_examples/datafile_ex0.txt
         :language: rst

   .. tab:: Try It

      Note that a this empty datafile is not editable!

      .. include:: df_examples/datafile_ex0.txt

A ``datafile`` with some default content

.. tabbed:: example1

   .. tab:: Data Source

      .. literalinclude:: df_examples/datafile_ex1_data.txt
         :language: rst

   .. tab:: Try It

      .. include:: df_examples/datafile_ex1_data.txt

A ``datafile`` with some default content

.. tabbed:: example2

   .. tab:: Data Source

      .. literalinclude:: df_examples/datafile_ex2_data.txt
         :language: rst

   .. tab:: Try It

      .. include:: df_examples/datafile_ex2_data.txt

A ``datafile`` with some default content

.. tabbed:: example3

   .. tab:: Data Source

      .. literalinclude:: df_examples/datafile_ex3_data.txt
         :language: rst

   .. tab:: Try It

      .. include:: df_examples/datafile_ex3_data.txt


The following example shows a complete use of the ``datafile`` directive
that defines a non-trivial input file and use in a small python program.

.. tabbed:: example_activecode

   .. tab:: Data

      .. literalinclude:: df_examples/datafile_ex_qb_data.txt
         :language: rst

   .. tab:: Render It

      .. include:: df_examples/datafile_ex_qb_data.txt

   .. tab:: Source code

      .. literalinclude:: df_examples/datafile_ex_qb_code.txt
         :language: rst

   .. tab:: Try It

      .. include:: df_examples/datafile_ex_qb_code.txt


Adding a ``datafile`` directive doesn't break non-python code,
but it doesn't use it (yet) either.

.. tabbed:: example_ac_cpp

   .. tab:: Data

      .. literalinclude:: df_examples/datafile_ex_cpp_poem.txt
         :language: rst

   .. tab:: Render It

      .. include:: df_examples/datafile_ex_cpp_poem.txt

   .. tab:: Source code

      .. literalinclude:: df_examples/datafile_ex_cpp_code.txt
         :language: rst

   .. tab:: Try It

      .. include:: df_examples/datafile_ex_cpp_code.txt


