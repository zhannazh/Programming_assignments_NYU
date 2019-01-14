This is a faithful port of the “Adventure” game to Python 3 from the
original 1977 FORTRAN code by Crowther and Woods (it is driven by the
same ``advent.dat`` file!) that lets you explore Colossal Cave, where
others have found fortunes in treasure and gold, though it is rumored
that some who enter are never seen again.  Use your operating
system command line to run the package::

    $ python adventure.py
    WELCOME TO ADVENTURE!!  WOULD YOU LIKE INSTRUCTIONS?

    > no
    YOU ARE STANDING AT THE END OF A ROAD BEFORE A SMALL BRICK BUILDING.
    AROUND YOU IS A FOREST.  A SMALL STREAM FLOWS OUT OF THE BUILDING AND
    DOWN A GULLY.

    > east
    YOU ARE INSIDE A BUILDING, A WELL HOUSE FOR A LARGE SPRING.
    THERE ARE SOME KEYS ON THE GROUND HERE.
    THERE IS A SHINY BRASS LAMP NEARBY.
    THERE IS FOOD HERE.
    THERE IS A BOTTLE OF WATER HERE.

    > get lamp
    OK

    > leave
    YOU'RE AT END OF ROAD AGAIN.

    > south
    YOU ARE IN A VALLEY IN THE FOREST BESIDE A STREAM TUMBLING ALONG A
    ROCKY BED.

The original Adventure paid attention to only the first five letters of
each command, so a long command like ``inventory`` could simply be typed
as ``inven``.  This package defines a symbol for both versions of every
long word, so you can type the long or short version as you please.

You can save your game at any time by calling the ``save`` command
with a filename, and then can resume it later::

    > save advent.save
    GAME SAVED
    > quit
    DO YOU REALLY WANT TO QUIT NOW?
    > y
    OK

    $ python -m adventure mygame
    GAME RESTORED
    > look
    SORRY, BUT I AM NOT ALLOWED TO GIVE MORE DETAIL.  I WILL REPEAT THE
    LONG DESCRIPTION OF YOUR LOCATION.
    YOU ARE IN A VALLEY IN THE FOREST BESIDE A STREAM TUMBLING ALONG A
    ROCKY BED.

You can find two complete, working walkthroughs of the game in its
``tests`` directory, which you can run using the ``discover`` module::

    $ python -m unittest discover

I wrote most of this package over Christmas vacation 2010, to learn more
about the workings of the game that so enthralled me as a child; the
project also gave me practice writing Python 3.  I still forget the
parentheses when writing ``print()`` if I am not paying attention.

For extra authenticity, the output of the Adventure game in this mode is
typed to your screen at 1200 baud.  You will note that although this
prints the text faster than you can read it anyway, your experience of
the game will improve considerably, especially when a move results in a
surprise.

Why is the game better at 1200 baud?  When a paragraph of text is
allowed to appear on the screen all at once, your eyes scan the entire
paragraph for important information, often ruining any surprises before
you can then settle down and read it from the beginning.  But at 1200
baud, you wind up reading the text in order as it appears, which unfolds
the narrative sequentially as the author of Adventure intended.

Changelog
=========

| 1.3 — 2012 April 27 — installs on Windows; fixed undefined commands
| 1.2 — 2012 April 5 — restoring saves from command line; 5-letter commands
| 1.1 — 2011 March 12 — traditional mode; more flexible Python syntax
| 1.0 — 2011 February 15 — 100% test coverage, feature-complete
| 0.3 — 2011 January 31 — first public release
