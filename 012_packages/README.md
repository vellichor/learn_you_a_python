# Modules and Packages

We already know two things about the module search order: one is that there are some built-in packages that the interpreter knows about and can check, and the other is that the very first thing the interpreter does is look in the current working directory for a match.

But what else is happening? How else can we control which modules the Python interpreter will find?

## Search Order

When looking for a module `possumpouch`, the interpreter searches a set of directories in order. In each one, it looks for

* A Python module in the local directory (a file called `possumpouch.py`)
* A Python package in the local directory (a directory called `possumpouch`, set up in a certain way.)

What directories does it search? For this, head back to the REPL and do this:

```
>>> import sys
>>> sys.path
```

You got back a `list` of `strings`, defining the Python interpreter's search order. First on the list is `''`, an empty string. That's why Python knows to look in the local directory first!

The rest of them are defined by the `sys` module that comes with your install of Python. You might notice that they all start with `/`: they are all explicit paths that specify a path all the way from the root of your filesystem. Some are ZIP files, and some are directories -- there's logic in the interpreter to help it do the right thing with each of these.

## OK, Show Me Your Package!

Easy there. There's one in this directory. You don't even have to ask!

We've defined a module called `tools`, by creating a directory called `tools` which has a special file in it called `__init__.py`. That file in a directory tells the interpreter we want this directory treated as a module -- it holds the contents that would be in the module file if this module were a file and not a directory. (Yeah, I suggest you let that one marinate.) In other words, when the module loader finds this module, it can't run it directly, since it's not a file, so it runs the `__init__.py` file to create the namespace for the module. Right now, that file is empty, but we'll see in a moment some useful things it can do.

Inside the tools directory, there are some modules. They're submodules of the tools module. When the tools module is loaded, the module loader also looks in the module directory for any submodules that are there. If our submodules were directories, they could have submodules of their own, as well!

Right now, we can load these submodules by using the `.` notation in our import statement: `import tools.tools`. You can see that we've done that in `main.py`.

So a package is just this: a set of nested directories with `__init__.py` files in them, and maybe some submodules, which can be files or directories themselves.

Our `main.py` goes on to use some functions from these submodules, and you'll notice that the function names are fully specified, from the top level of the package. How else could we do it?

### Importing the submodule with `from`

We could change the math_tools import to `from tools import math_tools`. That's allowed because the module loader can see that tools is a package, so it knows to look inside for submodules.

What else do we have to change in the script for that to work?

### Changing the `__init__.py`

You know, tools.tools is kind of redundant. It would be nice if the tools package had all the tools.tools members in its own namespace, so we didn't have to type it twice.

You know that the `__init__.py` defines the namespace when a module is a directory. What can you do to put all the functions from `tools.py` into the `tools` namespace?

(Remember that you can import all members of one namespace into another by taking advantage of `*`!)
