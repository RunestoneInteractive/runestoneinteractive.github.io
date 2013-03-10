Extension Authors
-----------------

In this section I will take you through an example of writing a new directive for the runestone interactive system.  In this case we will look at adding a ``datafile`` directive.  

The ``datafile`` directive is going to be used in conjunction with the skulpt file operations.  For skulpt to read a file we must provide some data that data can either be data that is part of a ``<pre>`` element or if we want the data to be editable we can embed the data in a ``<textarea>`` element.   In the case of the ``<pre>`` element the data might be visible or it might be hidden.  Our directive will look something like this:

Indentation is important.  Following the directive line, you can have as many optional parameters as you want.  Followed by a blank line, followed by the main body of your directive.

::

    .. datafile::  myid
       :edit:
       :rows: 20
       :cols: 65
       
       line 1  some data
       line 2  some more data
       line 3  this is the end

So the datafile takes one required parameter, a unique id that is used by the Skulpt ``open`` function as the file name.  The ``:edit:`` parameter tells us to make a textarea rather than a pre.  The ``:rows:`` and ``:cols:`` tell us how many rows and columns to add to the textarea.  If these are not present, then our directive should do its best to figure out a reasonable number of rows and columns.

The html output of the directive above should be:

::

    <textarea id="myid" cols="65" rows="20">
    line 1  some data
    line 2  some more data
    line 3  this is the end
    </textarea>

We will also make this extension work if the user wants to generate a non-interactive paper or pdf version of some text using LaTeX.  In this case the output of our directive should simply be:

::

    \begin{verbatim}
    line 1  some data
    line 2  some more data
    line 3  this is the end
    \end{verbatim}
    
Unless the ``:hide:`` flag is present in which case we won't generate anything.


Components of a directive
~~~~~~~~~~~~~~~~~~~~~~~~~

There are several parts to writing an extension.

1.  Initialization:  In this part you need to let sphinx know that there there is a new directive.  The name of the directive is associated with a Python class that derives from the restructuredText ``Directive`` class.

2.  Parse Time:  In this stage of processing sphinx is building the document object model.  A tree of nodes.  At this stage we process all of the arguments and gather the main content into a structure that can be used later when rendering a document in whatever format:  html, latex, epub, etc.

3.  Output:  At this stage we take the data that we have and format it for output by whatever *writer* is being used, again html, latex, etc.


All of the components of a directive can go in a single Python file.  Sphinx sees these extensions as simple python packages, so you can create a folder with an ``__init.py`` file or you can create an ``__init__.py`` file that imports one or more of your own files.

The ``__init__.py`` file should go in the modules folder following the folder heirarchy that is in place.  For example  ``luther/sphinx/datafile/``.


Initialization
~~~~~~~~~~~~~~

For the initialization phase we need to provide a setup function.  The setup function connects the directive name with a class, and tells skulpt about any css or javscript files that will be needed to support any html output.

The initialization code for the datafile directive looks like this:

::

    from docutils import nodes
    from docutils.parsers.rst import directives
    from docutils.parsers.rst import Directive


    def setup(app):
        app.add_directive('datafile',DataFile)
        app.add_javascript('bookfuncs.js')
        app.add_javascript('skulpt/dist/skulpt.js')
        app.add_javascript('skulpt/dist/builtin.js')

        app.add_node(DataFileNode, html=(visit_df_node, depart_df_node))

        app.connect('doctree-resolved',process_datafile_nodes)
        app.connect('env-purge-doc', purge_datafiles)

The key function here is the setup function.   The ``add_directive`` method maps the ``datafile`` directive to the ``DataFile`` class.  Then we add three javascript files we want to include along with a new node type called ``DataFileNode``  This is the node that will get added to the document object model.

The next line connects the ``'doctree-resolved'`` event with a function called ``process_datafile_nodes``.  This function could be used to create an index of our datafiles, or do nothing.  the ``env-purge-doc`` event is simliar but is called after all datafile nodes have been processed.

Parsing
~~~~~~~

During the parse phase there is one class for every directive.  This class must supply a run method that returns a list of nodes.  If you know that your directive is only ever going to create output for a particular rendering, e.g. html you can finish your run method by returning a ``raw`` node that is simply a string.

::

    return [nodes.raw('', mystring ,format='html')]
    
In this case mystring could be as long and complicated an html string as you might like to make.  A minimal hello world type example might be:

::
  
    return [nodes.raw('', '<h1>Hello World</h1>', format='html')]

In other cases you will defer the rendering of the node until later, having built a structure that can support multiple output styles.  In our example you will see that we return:

::

    return [DataFileNode(self.options)]
    
Where the DataFileNode just maintains a dictionary of data items we will use when we want to render any of the possible output formats.

If you return a ``raw`` node then you can ignore the ``app.add_node(DataFileNode, html=(visit_df_node, depart_df_node))`` line in the ``setup`` method.

Here is the DataFile class along with its run method.

.. sourcecode:: python

   class DataFile(Directive):
       required_arguments = 1
       optional_arguments = 2
       has_content = True
       option_spec = {
           'hide':directives.flag,
           'edit':directives.flag,
           'rows':directives.positive_int,
           'cols':directives.positive_int
       }

       def run(self):
           env = self.state.document.settings.env

           if not hasattr(env,'datafilecounter'):
               env.datafilecounter = 0
           env.datafilecounter += 1
        
           if 'cols' not in self.options:
               self.options['cols'] = min(65,max([len(x) for x in self.content]))
           if 'rows'not in self.options:
               self.options['rows'] = 20
        
           self.options['divid'] = self.arguments[0]
           if self.content:
               source = "\n".join(self.content)
           else:
               source = '\n'
           self.options['filecontent'] = source
        
           if 'hide' not in self.options:
               self.options['hide'] = 'block'
           else:
               self.options['hide'] = 'none'
            
           if 'edit' not in self.options:
               self.options['edit'] = False
        
           return [DataFileNode(self.options)]
   
As you can see our class has some shared/static/class level variables that specify whether the directive has content, how many arguments, and what the names and types of the arguments are.

Here are the possible types for the options:

* flag: For options with no option arguments. Checks for an argument (raises ValueError if found), returns None for valid flag options.
* unchanged_required: Returns the text argument, unchanged. Raises ValueError if no argument is found.
* unchanged: Returns the text argument, unchanged. Returns an empty string ("") if no argument is found.
* path: Returns the path argument unwrapped (with newlines removed). Raises ValueError if no argument is found.
* uri: Returns the URI argument with whitespace removed. Raises ValueError if no argument is found.
* nonnegative_int: Checks for a nonnegative integer argument, and raises ValueError if not.
* class_option: Converts the argument into an ID-compatible string and returns it. Raises ValueError if no argument is found.
* unicode_code: Convert a Unicode character code to a Unicode character.
* single_char_or_unicode: A single character is returned as-is. Unicode characters codes are converted as in unicode_code.
* single_char_or_whitespace_or_unicode: As with single_char_or_unicode, but "tab" and "space" are also supported.
* positive_int: Converts the argument into an integer. Raises ValueError for negative, zero, or non-integer values.
* positive_int_list: Converts a space- or comma-separated list of integers into a Python list of integers. Raises ValueError for non-positive-integer values.
* encoding: Verfies the encoding argument by lookup. Raises ValueError for unknown encodings.

There are two important instance variables to think about.

* self.content  Refers to the body content of the directive.  That is the indented text that comes after the options.  This can be anything, and you can make up your own conventions for how to interpret the body of a directive.

* self.options  Is a dictionary that contins key value pairs for all of  the optional parameters.  Of course you are free to modify this dictionary as much as you wish.

The ``self.options`` instance variable is a dictionary that will be used later to fill in a template for our output.  So, most of the processing in the ``run`` method is checking to see if the author provided values for these options and providing some default values for them if they have not.

The last line of ``run`` creates an instance of our DataFileNode.  This object doesn't do much other than act as a container to hold our data until it is time to render the output.  Nevertheless here is the code:

::

   class DataFileNode(nodes.General, nodes.Element):
       def __init__(self,content):
           """
           Arguments:
           - `self`:
           - `content`:
           """
           super(DataFileNode,self).__init__()
           self.df_content = content
   

Output
~~~~~~

In the final stage of processing we render the document in whatever format the author is requesting.  In this stage we take the data stored away in our ``DataFileNode`` and turn it into html or latex or whatever.

Each output format is handled by their own function that is registered back in the setup phase.  recall that we used the following line to connect our html output with a couple of functions:  ``app.add_node(DataFileNode, html=(visit_df_node, depart_df_node))``.

We will use Python triple quoted strings to create a couple of templates to fill in.  In the code below these templates are ``PRE`` and ``TEXTA``

::

    PRE = '''
    <pre id="%(divid)s" style="display: %(hide)s;">
    %(filecontent)s
    </pre>
    '''

    TEXTA = '''
    <textarea id="%(divid)s" rows="%(rows)d" cols="%(cols)d">
    %(filecontent)s
    </textarea>
    '''

    # self for these functions is an instance of the writer class.  For example
    # in html, self is sphinx.writers.html.SmartyPantsHTMLTranslator
    # The node that is passed as a parameter is an instance of our node class.
    def visit_df_node(self,node):
        if node.df_content['edit'] == True:
            res = TEXTA
        else:
            res = PRE
        res = res % node.df_content

        res = res.replace("u'","'")  # hack:  there must be a better way to include the list and avoid unicode strings

        self.body.append(res)

    def depart_ac_node(self,node):
        ''' This is called at the start of processing an activecode node.  If activecode had recursive nodes
            etc and did not want to do all of the processing in visit_ac_node any finishing touches could be
            added here.
        '''
        pass
    
The ``visit_df_node`` function is called when a DataFileNode is found in the document tree.  The visit function is called when the node is first encountered.  The ``depart_df_node`` function is called after all the children have been visited.

Notice that ``visit_df_node`` mainly just looks at its options to see if we need to create a textarea or a pre element and then lets Python's formatted strings take care of the rest.


