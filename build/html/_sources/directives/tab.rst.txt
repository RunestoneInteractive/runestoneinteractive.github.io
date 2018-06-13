Tabs and Tab Groups
===================

You can create a section that contains several tabs.  This is useful for exercises, and in other situations where you may want to partially reveal content.

::

    .. tabbed:: exercise1

        .. tab:: Question 1

            Write a program that prints "Hello, world".

            .. activecode:: helloworld

                print("Hello, world")

        .. tab:: Discussion

            .. disqus::
                :shortname: interactivepython
                :identifier: helloworlddiscussion


.. tabbed:: exercise1

    .. tab:: Question 1

        Write a program that prints "Hello, world".

        .. activecode:: helloworld

            print("Hello, world")

    .. tab:: Discussion

        .. disqus::
            :shortname: interactivepython
            :identifier: helloworlddiscussion



