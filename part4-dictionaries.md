Dictionaries
============

So far we've seen some basic data types: integers, floating-point
numbers, and strings. And we've played around with lists, which let
you group similar items together. Lists are the classic example of a
*compound* data type, which just means something that contains other
things.

But Python has another really handy data type hidden up its sleeve:
dictionaries. As the name suggests, dictionaries are used to look things up.
Specifically, a dictionary associates *keys* (words) with *values*
(definitions).

making a dictionary
-------------------

Here's an example of using dictionaries to implement ... a dictionary! You
should follow along and make your own dictionary, but put different things in
it!

    meaning = {
      "apple": "round edible fruit",
      "computer": "electronic device that drives people crazy",
      "window": "glass fitted in a wall",
      "python": "large tropical snake",
    }

Now I've got a dictionary where I can look up the meaning of four
different words.

*Exercise*: Make your own dictionary! Put anything you want in it.

accessing elements
------------------

Here's an example of looking up a word:

    meaning["computer"]
    meaning["apple"]

Notice how this looks just like looking values up in a list, except
the key is not an integer. It can be almost any value, although
strings are most common.

adding elements
---------------

You can add new elements to a dictionary:

    meaning["ruby"] = "attractive semi-precious gem"
    meaning["macintosh"] = "a variety of apple"

*Exercise*: Add an element to your dictionary!

how many?
---------

Just like with strings and lists, you can use the len() function to
find out how big a dictionary is:

    len(meaning)

*Exercise*: Add an element to your dictionary!

replacing elements
------------------

You can replace existing values:

    # old meaning
    meaning["python"]
    # change meaning
    meaning["python"] = "a popular programming language"
    # new meaning
    meaning["python"]

another example
---------------

There are lots of other uses for dictionaries. Let's say you're playing
scrabble, and you want to keep track

    scrabble_scores = {
      "Julia": 20,
      "Kate": 80,
      "Marianne": 40,
      "Annaelle": 40,
    }

    scrabble_scores["Julia"]

Notice how the same value can occur multiple times. That's important
to understand: each *key* is unique, but values can repeat.

We can add more entries to the dictionary, if we get a new player:

    scrabble_scores["Juliet"] = 100

Now the dictionary is a bit bigger:

    len(scrabble_scores)

iterating
---------

Like a list, you can iterate over a dictionary. Unlike a list, you
iterate over the *keys* rather than the *values*:

    for player in scrabble_scores:
        print player + " is playing Scrabble"

Of course, your loop is a lot more useful if you lookup what their current
score is

    for player in scrabble_scores:
        score = scrabble_scores[player]
        print player + " has a current score of " + score

*Exercise*: Print out every element in your dictionary

methods
-------

First example: I want to see the keys of a dictionary:

    print scrabble_scores.keys()

I can use the same method on a different object, and I get a different
result:

    print meaning.keys()

Another method, which is complementary to keys(), is values():

    print band.values()
    print meaning.values()

*Exercise*: Get the keys and values from your dictionary

.keys() and .values() are called *methods* They let you get more information
about a dictionary.

Python has a really useful 'help' function, that lets you find out other
things about a dictionary.

    help(meaning)

Ignore all the things that begin with __ for now. 

(find a method that actually makes sense) Can anyone guess what this
might mean? Okay, I want everyone to go through this and find one new
method to use, and use it.

documentation
-------------

A quick note about documentation:

Who thought that help() page was easy to understand? Who found it confusing?
Let people give some feedback.

(go to browser, and google "python dictionaries")

A lot of the resources about programming languages can be really hard to read.
They are written by people who have been programming for a long time, and
they're usually aimed at people who already know how to program. Do not worry
if you Google something and it doesn't make any sense to you; it's probably
not written with you in mind (even if it says it's a tutorial!)
Instead, try searching for "dictionaries tutorial". We have a short list
of tutorials on the wiki.

TODO: make a list of resources for continuing learning Python on the website,
and point people to that.
