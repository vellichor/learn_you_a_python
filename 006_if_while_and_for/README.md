# If, While, and For: Control Flow in Python

So far, we've written scripts that execute all of their statements in order. Execution flows from the top of the script to the bottom, executing everything it finds, and occasionally stepping back up into a previously defined function. However, sometimes we want to allow our script or function to behave differently, based on the current state of the program and its variables. We're going to explore a few basic ways to do that now.

## If, Elif, Else

In Python Anatomy, we did some mathematical comparisons. These expressions evaluate to True or False, two important literal values Python understands.

```
>>> 5 < 3
False
>>> 5 > 3
True
```

What `type()` are True and False?

### Getting Iffy

Open up the script `lets_get_iffy.py` from this directory. We end this script with 3 calls in a row to the same function. How does it behave each time?

### Branching Flow

This type of logic is called a branching flow: when we reach the beginning of the `if` block, we know the execution flow may pass into one of the following branches. Branches of an `if` statement may include zero, one, or many `elif` blocks, and zero or one `else` blocks. They always appear in this order. 

Each of these blocks has its own indented body. You can see that these indented bodies are _nested_ inside the function body.

A branching flow works this way:

* If the expression following `if` is True, execution enters the block after the `if` statement, flows through that block, and then skips the rest of the branches.

* If the expression following `if` is False, we go on to the next branching statement, or, if there are no more, we exit the branching flow and go on to the next statement in line.

* If the next branching statement we reach is `elif` and its expression evaluates True, we enter this block, execute it, and then skip the rest of the branches.

* If the next branching statement we reach is `elif` and its expression is False, we skip it and go to the next branching statement.

* If the next branching statement is `else`, there is no expression to evaluate. An `else` block catches all flows that did not enter a previous branch, and never takes an expression of its own. Else always comes last, because if we reach an `else` block, it always executes.

Sometimes execution will not pass into any branch of a branching flow. Can you predict what could cause this?

What would happen if you had the following flow:

```
if True:
  print("A")
elif False:
  print("B")
elif True:
  print("C")
else:
  print("D")
```

Add it to your script and run it to see if you're right!

What about this tricky example:

```
if True:
  print("A")
if False:
  print("B")
elif False:
  print("C")
elif True:
  print("D")
if True:
  print("E")
elif False:
  print("F")
else:
  print("G)
```

One more thing before we leave this script: in the `print` statements, see if you notice what we are doing to print numbers. You can look up why this is done this way on your own, or wait until the end of this section!

## Looping Flows

What if you get tired of writing "badger" all the time? What if, for some reason, you wanted to say "badger" a lot of times, but you really only want to type it once?

Check out `while_away_the_badgers.py` for an example of how we might do this.

* You'll see something new here: the comment! On lines 4 and 7, we see a `#` symbol followed by a note about what the code is doing. The `#` symbol is a note to the Python interpreter to ignore everything that comes after it and go on to the next line. Not only can we use this to make our code more readable to others, it's a good idea to do it for yourself -- if you come back to your code 2 or 3 years later and need to make head or tail of it, the comments really help!

### In A While

`while` is the simplest form of looping operator. `while` evaluates its expression (`times < num_times` in our case) and if it's True, it runs its indented body. Then, it does it again. And again. And again. If the expression ever evaluates to False, however, it immediately exits, does not pass Go, does not execute the statements in the body, and returns execution flow to the next thing in line.

### What's That Funky Operator?

Before we get too far into things, I've snuck a new one by you. Check out line 7: `times += 1`

WHAAAAT? Are we ADDING 1 and ASSIGNING A VALUE at the SAME TIME???

That's exactly what we're doing. After this statement executes, the value of `times` is 1 more than it was before. `-=` works too! You'll see this a lot in while loops, as it's a very intuitive way to do something a certain number of times.

Looping is sometimes also referred to as `iterating`. However, `iterating` usually refers to a specific kind of loop: the `for` loop.

### For Score and 7 Loops Ago

We'll be working with the `for_science.py` script now. Folks there is so much new stuff in here! I'm picking up the pace a little, because we've been working with Python hands on for 5 lessons already, you've worked on 7 different scripts, and some of the basics of looking at a script and reading Python code are probably getting a little easier.

But all that is to say, if you take a little longer with this lesson, no big. I'm throwing a lot at you, and if your brain is full, take a break, and come back to it tomorrow. But when you're ready, we're diving on in!

#### The List Type

A new object??? Up there on line 3 we have some square brackets and it's crazy. We've never seen those before. You can tell that this line is assigning something to the variable `rad_types`. What could you add to the script to find out what kind of object it is?

Spoilers: it's a `list`. Specifically, square brackets are how you tell the interpreter that you want to write a `list literal`. What sits between the brackets are the items you want to have in that list. Things that are true about lists:

* Their items are in a fixed order
* You can get their members back by number (go ahead, plop that list definition into a REPL, and then see what you get if you say `rad_types[1]`!)
* They are ITERABLE

What "iterable" means, for now, is that a `for` loop can use this expression, and execute its body once for each value in the list, in order.

#### The For Loop Itself

This is new too! Let's break it down. You have the `for` keyword, and then the symbol`rad_type`. This is a variable name we're going to use to represent the list member we're working on for this go-around. (Each go-around is called an `iteration`.) Then we have the `in` keyword, which means that the next thing is the expression we will pick values of `rad_type` from. Last, we have the `:` we usually find before an indented block.

#### The `range` object

`range()` uses the arguments you give it to set up a list of numbers, which it will hand back in order. Run this code and see if anything surprises you about the list of numbers you get. Think back to what you got when you asked for `rad_types[1]`. Notice anything?

#### Zero-Indexing

What you're seeing is that in computer science, we often count from 0. Just look at the lesson numbers in this series! The reason for this is iteration itself. Member `[0]` of `rad_types` is the member that is 0 steps away from the front of the `list`. Just remember that, and this habit (we call it _zero-indexing_) will seem way less weird and make a lot more sense.

#### The `len()` Function

Another built-in, this gives you the count of items in an iterable object, OR the number of characters in a `string`. Actually, that's a tricky statement... a `string` IS AN ITERABLE!! What do you get if you start a `for` block with `for x in "potato":`?

#### The `str()` Function

I told you I'd explain this one. This is an example of _casting_: turning one type of object into another. Try this in the REPL:

```
>>> a = 1
>>> b = str(a)
>>> b
>>> type(a)
>>> type(b)
```

It works the other way too:

```
>>> x = "1"
>>> y = int(1)
>>> type(y)
```

What happens if you try

```
>>> int("badger")
```

We'll talk more about casting, and how and when it works, later on.