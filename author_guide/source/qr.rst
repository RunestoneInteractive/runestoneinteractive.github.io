Quick Reference
===============

Runestone comes built in with its own little help system.  You can get a list of all of the runestone commands, or get the syntax for any command easily.

::

    $ runestone help
    Available Commands:
    build  [--all]      * build the current project
    deploy               * deploy the current proejct using rsync
    serve [--port]   * start a simple webserver for the current project
    help list             * list all runestone directives
    or type help <directive> for doc on a runestone directive

    $ runestone help list
    Runestone Directives List
       activecode
       blank
       clickablearea
       codelens
       datafile
       disqus
       dragndrop
       fillintheblank
       mchoice
       parsonsprob
       poll
       qnum
       reveal
       shortanswer
       tab
       tabbed
       timed
       usageassignment
       video
       vimeo
       youtube

     $ runestone help mchoice

    .. mchoice:: uniqueid
       :multiple_answers: boolean  [optional]
       :random: boolean [optional]
       :answer_a: possible answer  -- what follows _ is label
       :answer_b: possible answer
       ...
       :answer_e: possible answer
       :correct: letter of correct answer or list of correct answer letters (in case of multiple answers)
       :feedback_a: displayed if a is picked
       :feedback_b: displayed if b is picked
       :feedback_c: displayed if c is picked
       :feedback_d: displayed if d is picked
       :feedback_e: displayed if e is picked

       Question text   ...
