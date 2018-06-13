Blockly
=======

Support for blockly is very experimental at this stage.
More information about blockly can be found `here <https://developers.google.com/blockly/>`__.

Synopsis
--------

.. code-block:: none

   .. blockly:: unique_id

      + --- Content area ---
      |
      | A list of blockly toolbox items to include
      |
      | followed by an optional XML block containing 
      | default blockly content to preload
      |
      + --------------------

Required Arguments
------------------

unique id
    A unique identifier after a space and the ``::`` in the blockly directive.
    Valid identifiers must not contain spaces.
    You should also avoid the characters `` ` ``, ``,``, ``:``, and ``*``.

content area
    Toolbox items are defined in the content area.
    Each toolbox category starts with ``* category name`` and ends with ``====``.

    The toolbox items in each category must be XML type names.
    See the `Blockly devlopers guide <https://developers.google.com/blockly/guides/configure/web/toolbox>`__
    for more info.

Known limitations
-----------------

Experimental.
Might break or change in a future release.

Examples
--------

.. code-block:: rst 

   .. blockly:: blockly1

      * controls
      controls_if
      controls_repeat_ext
      controls_whileUntil
      controls_for
      ====
      * logic
      logic_compare
      logic_operation
      logic_boolean
      ====
      * math
      math_number
      math_arithmetic
      ====
      * text
      text
      text_print
      ====
      variables

      preload::
      <xml>
         <block type="variables_set" id="1" inline="true" x="25" y="9">
            <field name="VAR">X</field>
            <value name="VALUE">
               <block type="math_number" id="2">
                  <field name="NUM">10</field>
               </block>
            </value>
         </block>
      </xml>


