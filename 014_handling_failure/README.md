# Handling Failure

If you've gotten to this point in the tutorial, you yourself are probably getting pretty good at dealing with what happens when things go wrong. From installing Python in the first place to dealing with what happens if you miss a `)` or a `:`, you are getting used to looking at the error messages you get when something isn't set up right or you make a mistake.

In particular, you've seen your old friends

```
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'a' is not defined
```

and 

```
  File "<stdin>", line 4
    :
    ^
SyntaxError: invalid syntax
```

probably quite a number of times by now. So what _is_ a SyntaxError or NameError?

If you said "well, probably an object!" then you are definitely getting the hang of this Python thing. Indeed, these errors are types of _Exception_ objects, created by Python code when it gets some input that it can't handle. So far, we have generated our fair share of `Exception` objects, and each time, it's caused your program to exit and print that exception to the screen. But WHAT IF I TOLD YOU that you can actually handle exceptions WITHIN your program, allowing it to keep running even if the user (who might even be you) does something crazy?

## Exceptions and the Try Block

You know that if we reference an unbound variable, we get an exception.

```
>>> a
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'a' is not defined
```

What we're going to learn now is a new kind of flow control: the `try` block. Plop this into a text file and run it with Python:

```
try:
  print(a)
except:
  print("a wasn't defined!")
print("Look, ma, still running!")
```

Yep, you read that output right. Your script didn't crash, even though `a` was referenced without being defined. This is because of the special execution environment set up by the `try` block. Inside of a `try` block, when an exception is _raised_ (that's what we call it -- you may also hear people say the exception was _thrown_) execution of that block stops, but the interpreter then looks for an `except` block at the same level as the `try` block -- that is, immediately following the `try`'s indented body, and at the same indent level as the `try` statement itself. (Think of the `else` or `elif` blocks associated with a particular `if`.) If it finds one, it runs the code it finds there, which allows you a chance to tell the user what went wrong and figure out what to do instead. (Hint: this is a great place to use that `logging.warning` method we tried out back in section 011!)

### What if we only care about SOME exceptions?

We can make our try blocks be selective: we can trap different kinds of errors with different `except` blocks. We do this like so:

```
try:
  print(a)
  int("badger")
except NameError:
  print("Oops, a wasn't defined!")
except ValueError as v:
  print("Boo, you gave us a bad value for an operation: {}".format(v))
print("Stiiiiiill running after all that mess!")
```

Run that in a script and see what happens. Notice that you only got one of the errors! The `try` block still stops executing when the first exception is raised -- it doesn't try to run the rest of the `try` block, because it already knows something has gone wrong, and we need to deal with that and not try to run any code that may have depended on it. Instead, it runs the matching `except` block, if there is one, and then continues. In this case, we raised a NameError first, so that's the `except` block that the interpreter will execute.

Now, try swapping the two lines inside the `try` block, and run it again.

Whoa, what's up? We got the printout of the exception, AND the script kept running to the last line!

In the ValueError `except` block, we have a little extra bit of code: `as v`. When the interpreter catches an exception that matches this `except` block, it goes the extra mile and binds the exception it caught to a variable, which lives in the scope of the `except` block.

### Uncaught Exceptions

Let's see what happens if you throw an exception that _doesn't_ match any of your `except` blocks. Add this to the beginning of your try block:

```
my_list = [1, 2, 3]
my_list[11]
```

Run that sucker, and OH DEAR. We didn't get our last line of output -- the whole script exited, with a new kind of error.

Yup, even though we had plans for the other kinds of errors we might want to catch, we didn't write anything for the `IndexError`, so when the `try` block raised an exception, no `except` block caught it. That means it got raised to the next level of the script, which was the top level (global scope.) Nothing caught it there, either, so the whole script stopped execution and bailed out.

Try moving the `print(a)` line to the top of the `try` block. Yup, now the whole script runs again, because the `try` block stopped executing when it raised that `NameError`, and there was an `except` block to catch it. Since the `try` block only raises one exception before exiting, only one `except` block runs, and any uncaught exceptions that could have run later are never generated at all.

This is generally true of a `try` block: only one exception block will run. If there is more than one `except` block that could match your error, only the first one will run.

### Wait, More Than One Match?

Let's talk about class inheritance again. Remember when we made our `Animal` class in section 009, and then subclassed it with `Possum`? That was a way of saying that `Possum` is a kind of `Animal`, and can do all the basic things any `Animal` can.

There is a tricky implication of that: all `Possum`s are `Animal`s! This is an example of a _class hierarchy_. (No, no, not that kind. Put away your pitchforks for a second. We can get them back out later.)

Every Python3 class is part of the same class hierarchy, with `object` at the very top. (Like many class hierarchies, being at the top means that `object` has the fewest actual capabilities.) Each layer of inheritance adds some attributes and capabilities, but keeps the ones it inherited from above. But since `object` is pretty useless, we will often talk about the _root_ of a particular class hierarchy, or its _base class_, as being the ancestor of this class that inherits from `object`, and that all other kinds of this object inherit their actual abilities from.

The base class of exceptions is the `Exception`. You can test this right now. Get back in that REPL and try

```
>>> n = NameError()
>>> v = ValueError()
>>> e = Exception()
>>> isinstance(n, Exception)
>>> isinstance(v, Exception)
>>> isinstance(v, ValueError)
>>> isinstance(e, NameError)
```

We made ourselves some instances of different exception types, and then checked them out to see if they were instances of certain _types_ (classes). This is different from checking the `type()` of something -- that will tell you what exact type the object was created as. The builtin `isinstance()` instead tells you whether this instance _inherits from_ the given type, which is to say, whether it can do all the things that type can do.
```

### What Do I Care For Class Hierarchies?

Well, we now know that every exception is an instance of `Exception`. Turns out, that's actually what the interpreter does when it checks to see if your `except` block matches: it's not checking for an exact match on `type()`, it's looking to see if your exception _is an instance of_ the listed exception type.

So what do you think would happen if your `except` block said

```
except Exception as e:
```

### Well That's Useful!

So why don't we do it all the time? We could just catch all exceptions every time, and our script would never crash!

There are two things that make that less useful:

1. Depending on the exception that you caught, the response that lets the rest of your script run could be very different

2. Remember when I said that `try` sets up a special execution environment?

Yeah, that second one is pretty important. When we raise an exception, we generate a lot of information that then becomes available to you, the developer, to try to figure out what went wrong. In addition to knowing what error was raised, you get what's called a _traceback_: you can see this when your script or REPL command fails, though in most cases we've seen so far, there's only one call in it.

However, if you're calling a function that calls another function that calls another function, many layers deep, and something way down the stack raises an exception, each new `raise` adds a layer to the traceback, which accumulates every time the exception fails to be caught at one level and raises to the next. These objects can get pretty heavy and complex! If part of the normal flow of your program involves creating big tracebacks all the time, you are going to get a significant performance penalty.

A much much better strategy is this: go ahead and use a very general `except` block if you really have no idea what's going on, but then use that as a tool to debug your code, and find out what makes it crash. Because make no mistake: when we `raise` an exception, it's a crash! `try-except` blocks are just a tool to prevent it from taking down the whole program.

### Why Now?

Why am I only bringing this up now? Well, up until now, we weren't accepting any inputs from outside our programs -- what happened when you ran your program was completely up to you. However, now we know how to control a program from outside. That means that no matter how carefully you write it, someone else can come and hand you something you never expected (like trying to make an integer out of a badger! Sheesh. Who would do that?) and it might make everything go haywire.

Exception handling is a great tool to deal with that edge case where someone has handed you something cuckoo. But we can still avoid a lot of it by doing some basic checking of the input we're given (checking types and making sure they can be converted to the right thing, etc.) This is called _sanitizing_ the input, and it's a major element of good style.

## Playtime

Try modifying the sample scripts in this section and the last section and see what you can do to cause exceptions and catch them. Try things like

* catching multiple types of exceptions
* passing in an argument of the wrong type, and making sure your program doesn't crash
* nesting one `try` block inside another (you can totally do that!)
