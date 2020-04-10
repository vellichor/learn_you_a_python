# Intro to Debugging

In the last section, we wrote and called a couple of functions. The output may or may not have been what you expected.

In particular, our last function called had no side effects, and we did not print the return value to the screen. That means that if you run this script, it's hard to tell that the function even ran! Our two numbers got added together, but we threw the result away.

I've included a copy of that script here, with three statements added. This time, we'll print some output to the screen so we can trace the execution of our script and understand what's happening.

If you run this script, you'll see that we print output before each function call, and again after they have all finished. This way, we can see that execution must have passed through our second function call, so we know the call was made.

Where would you add a debug statement to make sure the function was actually run?

Our print statements will run and generate output every time we run this script. In a later section, we'll explore how to use the `logging` package to turn certain groups of debug statements on and off.

Using debug statements is a good way to visualize the _execution flow_ of a script. In other words, the interpreter reads each statement in order, but what is the actual order in which things are executed? 

* In this current example, when we reach the function call on line 12, execution actually steps back up to line 3, to run the code we previously defined in the `add_5` function.

* When the `add_5` function called on line 12 is finished running, execution returns to the place where it was called, and continues on to line 13.

* Our next function call similarly steps out of line, executes the block we defined earlier, and then _returns_ (see why we call it that now?) to the place where it was called.

* Actually, if we could add some print statements into Python itself, we could see that the `print()` calls themselves actually send execution outside of our script! When we call `print()`, the script evaluates `print`s arguments, and then code executes inside the interpreter itself where `print` is defined! When the `print` call is done, execution returns to our script.

Learning to trace execution through a program and keep track of the state of the program after each step, including the values of different variables you have defined, is a fundamental programming skill! But it's hard to get it all down right away, so using debug statements to remind yourself of the states your program is passing through is a very useful tool, especially while you're learning.

