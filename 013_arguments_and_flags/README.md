# Arguments and Flags

### REMEMBER THE __MAIN__!

Oddly, this is not a section about geopolitics.

While we know how to set up a program now, and we know how to run it, all that means is that we know how to make our script do exactly the same thing, every time.

But we know that most useful programs are interactive in some way: you apply them to some piece of data, and they do something useful with that information.

How does the data get into the program?

I'M SO GLAD YOU ASKED.

## The `sys` module

We've used this module briefly before, to check out the search path Python uses to find modules (including `sys`)! In general, `sys` is the module we will use to interact with the Python interpreter itself. Another module, `os`, allows us to interact with the host computer system, which we'll do a bit later.

Remember that the Python interpreter is, itself, an executable. When we use 

```
$ python myscript.py
```

we are actually giving the `python` executable the name of our script, as an argument, and asking it to run the code it finds there.

Look at the sample script `args_example.py`. We use a property of sys, `argv`, which is a vector (a `list`) of arguments supplied to the Python interpreter when it was started. Let's run it at the command line (not the REPL):

```
$ python args_example.py
```

You can see the list of arguments just has one member: the name of the script we asked it to run.

What do you expect to see if you look at `sys.argv` from inside the REPL? Go try it. Were you right?

## __main__?

You'll see one other thing in here: an if statement. Remember that when we run a script using Python, the first script we enter gets the module name __main__ created for it. What we're doing here is a point of good style, which means it's a useful habit that we do for a good reason.

Remember that when we load a module, the first thing it does is run all the code in the module definition. Also consider that every script is a module. What if we wanted to use this script as a module in someone else's script?

This `if` statement is the usual way of protecting code that you only want to run if this module is the entrypoint for the script. The `__name__` keyword is available from inside all modules, and tells us what the interpreter currently considers to be the name for this module. If we had imported this from somewhere else, the module name would be `args_example`, because it came from the `args_example.py` file. But since we entered this script directly from the interpreter, that name has been replaced in favor of `'__main__'`, so we know we want to run this protected part of the script.

## Back to you, sys

Our `sys.argv` attribute gives us all the arguments supplied to the script. So let's give it one.

```
python args_example.py 1 big potato
```

Check that out! All the arguments got passed through into the list. That means we can change the behavior of the rest of the script depending on what our user handed in.

Try running the example script the other way:

```
./args_example.py 1 big potato
```

What's different? What's the same?

### String Thing

One thing to take notice of is that we receive all the command line arguments as strings. If you're expecting to use one of these arguments as some other type, you'll need to cast it yourself.

## What About The Flags?

If you've used command line programs much, you may have noticed that sometimes we pass flag arguments, sometimes called switches. Things like 

```
$ grep -Rl potato .
$ ls -al
$ python --version
```

This is such a common pattern that some nice person went and wrote a library about it. Several nice people, actually. The one I use the most is [argparse](https://docs.python.org/3.7/library/argparse.html), the one that comes built in to Python. There's a sample script, `argparse_example.py`, that will give you an example of how to use it. Try running

```
./argparse_example.py -h
```

to see a help message generated from the argument parser itself! Then pass in some arguments and tell us if your little buddies are good boys.

Using the documentation and the sample script, try messing around and changing the flag and positional arguments to influence the behavior of the script.

Notice that `args` is a `Namespace` object, which has an attribute for every item inside it. This is not the same as a Python namespace, which we use to resolve symbols in the script.
