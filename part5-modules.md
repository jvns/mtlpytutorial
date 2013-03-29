Modules
=======

* Who here likes doing more work than they have to?
* Yeah, not me. Programmers are really big on *reusing* code
* now you've already seen the most basic element of code reuse:
  the function
* functions let you store some code and use it again later, possibly 
  many times
* the functions we've seen so far all live in the same
  file as the code calling them -- it's all one script
* but typically, programmers write many scripts -- each one to do
  one particular task
* so how do you reuse code between different scripts?
* well, that's what modules are for

* even better than reusing your own code, Python ships with hundreds
  of useful modules in its standard library
* and there are tens of thousands more out there on the Internet that
  you can use
* so even if you never write a single module of your own, you need to
  know about modules

* let's take a look at one handy module in Python's standard library:
  it's called random, and it's all about generating random numbers
* the first thing you need to learn is how to *import* a module
    
    ```python
    import random
    ```

* huh. that didn't do anything. oh wait, actually it did:

    ```python
    random
    ```

  See what happened? import defines a new name, just like assigning a
  variable or defining a function. A name just references something
  you can print -- in this case a module.

* another thing you can do with a module is get help on it:

    ```python
    help(random)
    ```

  Scroll down to the very bottom to find the good stuff -- under
  "functions".

  That only works in an interactive Python session, by the way.

* The most commonly used functions in the random module are random,
  randint, choice, and shuffle. The other stuff is just there for
  hardcore math geeks and scientists who care deeply about random
  numbers. Honestly, I don't even know what a beta distribution is!

* here's a tiny example of using the random module

    ```python
    print random.randint(1, 10)
    print random.randint(1, 10)
    print random.randint(1, 10)
    ```

* Oh yeah, you can get help on an individual function as well as a
  whole module:

    ```python
    help(random.randint)
    ```

* That's nice. It turns out that generating random integers is
  important, but it's usually not what you really want to do. Usually
  you have a list of items and you want to do something random to
  them. Like, say you've got this rack of letters in a Scrabble game:

    ```python
    letters = ['E', 'P', 'R', 'U', 'L', 'A', 'E']
    ```

  and you want to see some different orderings of this rack:

    ```python
    random.shuffle(letters) ; print letters
    random.shuffle(letters) ; print letters
    random.shuffle(letters) ; print letters
    ```

  or, you want to pick one letter at random:

    ```python
    random.choice(letters)
    ```

* So let's put this stuff together and make the tiniest, simplest
  computer game ever. Here's the idea: you need to practice memorizing
  capital cities for your grade 3 geography course. And don't tell me
  you've already passed grade 3; a little review never killed anyone.

* here's a live demo of the game:

    ```
    python capitals.py
    ```

* So: how does this work? Let's open up the script and take a look.
  You should already have downloaded the script last night, so
  fire up your text editor and open capitals.py.

    ```
    gedit capitals.py
    ```

* First is the data: obviously the program has to know what the right
  answers are, and we use a dictionary for that. The keys are the
  provinces and territories, and the values are the capital cities.

* Next up: we import the random module. Not much point to a game with
  no randomness, is there?

* Finally, the main loop. Let's go over it one line at a time
  - capitals_dict.keys() returns a list of the keys of the dictionary,
    i.e. names of province and territories; we're going to pick five
    random elements from that list
  - to do that, we start a loop, but this one is a little different
    from other loops we've seen, since it uses the range() function
    rather than a list
  - let's pop over to an interactive prompt to demonstrate:

        ```
        range(5)
        ```    
  - So range() really just gives a list of numbers to loop over
    over ... so at its heart, this loop really is the same as the
    other loops we've seen!
  - except that we don't actually care about the contents of the list;
    all we care about is the fact that we run the loop 5 times
  - now we're inside the loop, and we pick one province or territory
    at random
  - then we look up the right answer: the value corresponding to this key
  - next up, here's another new trick: getting input from the user
    with raw_input()
  - this is actually very rare in real-life code, but it's the simplest
    way to interact with the user at the console
  - so now we have the user's answer, and we have the correct answer:
    all that's left is to compare them and tell the user how they did
  - and that's what this "if" statement does
