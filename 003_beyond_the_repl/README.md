# Beyond the REPL

Using the REPL is a great way to try out statements and see if they do what you want them to do. But to do interesting things in a script, you're going to want to execute multiple statements, and maybe even define some of your own functions!

That's why this directory, finally, contains more than just a `README.md`. If you're still in the REPL, get out of it by entering `exit()`, or open yourself up a fresh terminal so that we can leave the REPL open to try things out.

In your terminal, make sure you're in the same directory as this `README.md`. Then,

```
pomelo:002_beyond_the_repl chi$ python sample.py 
```

## What Did I Just Do?

You know that when you run `python` without anything after it, you get a REPL. But if you run `python` with the name of a file after it, Python will try to interpret the named file for you!

Open up `sample.py` and `standalone_sample.py`. You'll see that they're mostly the same inside. Indeed:

```
pomelo:002_beyond_the_repl chi$ python standalone_sample.py 
```

and you'll get the same thing. However, there's at least one special thing about the `standalone_sample.py` file. One is easier to see, and one is harder.

### Invoking Python

There is a small magical incantation up at the top of the standalone script.

```
#!/usr/bin/env python
```

This difference is easier to spot, because it's right there in the file.

### Marking The File Executable

If you're using Windows, this difference doesn't even exist, so you certainly won't have been able to find it. However, on Mac OSX or any *nix, files you want to execute have to be "marked" in the filesystem as executable first. When constructing this tutorial, I ran

```
pomelo:002_beyond_the_repl chi$ chmod +x standalone_sample.py 
```

### Running an Executable Script

Because `standalone_sample.py` has the incantation (we call this a *hashbang statement*, and it tells the operating system what interpreter to use to read the rest of the contents) and because it is marked executable, we can run this in a quicker way:

```
pomelo:002_beyond_the_repl chi$ ./standalone_sample.py 
```

The `./` tells our shell we want to execute a file that's present right here in the local directory.

## Playtime!

Make a copy of `standalone_sample.py`:

```
pomelo:002_beyond_the_repl chi$ cp standalone_sample.py my_script.py
```

Open up `my_script.py` and try changing some things around (I bet your name's not Potato!) You can see that the script has more than one statement in it, and that they all ran in order when you executed the script. You can also see the built-in `print()` function, and you can see that the `+` operator works to stick two strings together. What else can you make your script do?