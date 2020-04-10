# Methods To The Madness, Part 1

So far we've used built-in functions and built a few of our own. We've also touched on the idea that things in Python are objects, and that they have types, or classes.

Well, an object in real life has some properties -- depending on its type, it might have a weight, or a color, or a smell. It also has some methods you can use it by: you can use a hammer to hit stuff, or use a fork to eat stuff. Objects in Python are the same way! The reason why we define these types is so that we'll have a built-in set of tools for dealing with every object of that type.

In this section, we'll use some methods that are already built in to the classes we're familiar with already. In later sections, we'll see what it takes to build our own methods.

## A Better Way To String

So far we've done string formatting by force: turn anything that isn't a string into a string with `str()`, then stick it together with `+`. Check out `formatting.py` to see a new way to do it, then come on back here for the explanation.

### Method calls

On line 4, you can see that we've defined a string literal, as we usually do, and bound it to a variable, `message`, so that we can reuse it. However, it's got a pair of curly braces `{}` in it. The next thing we do is brand new: we take our variable, follow it with a `.`, and then what looks like a function call. What gives?

Functions, you see, are one kind of callable object Python understands. A function is unbound, meaning it doesn't belong to any particular object. It just floats around in the general context of the script, and you can call it by just using its name wherever* you want.

A method is a callable object that is BOUND. In particular, it's bound to an object of a certain class. All objects that have the same class also have the same methods bound to them. That means EVERY STRING we've ever made had a format() method attached to it. You call it by first naming the object you want to use it with (`message` for us), then joining it with a `.` to the name of the method you want to call. You fill up the `()` with arguments you want to pass in, just like other callables.

Why did we never use it before? That's because of what the `str.format()` method does (we'll refer to it that way, so that it's easy to see it belongs to the `string` class.) This method looks at its bound string to see where there are holes in it to plug arguments into (those look like `{}` inside the string.) Then it plugs in its arguments in order, converting them to strings first (`str()`) if it needs to. In essence, it has one extra invisible argument: ITSELF.

Our earlier strings just didn't have any holes in them, so there wouldn't have been any place to plug stuff in. That's all.

Try formatting some strings in the REPL. See what happens if you supply more arguments than holes, or more holes than arguments! It's a good idea to try things out in the REPL that you already know won't work. That means if you get that error message later on when you run a script, you'll have an idea of what might have gone wrong to cause it.

This is a great time to introduce you to the [Python Library Reference](https://docs.python.org/3.7/library/stdtypes.html#str), which will tell you all about the built-in classes and functions, their methods, and how to use them. Go see what else a `string` can do, and we'll cut this lesson short so you can play around in the REPL and make it say silly stuff.

* You can't always call all functions wherever you want! Later we'll talk about scope.

