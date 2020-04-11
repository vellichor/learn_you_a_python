# Modules

It's easy to see that if we write a lot of Python code, we might want to break it up into different files. But we already know that within each Python script, the farthest out scope is the global scope, and we already know that each script has its own global scope. How can two Python scripts reference one another?

Much like everything else lately, modules are something we've been using the whole time. In fact, you've already referred to a module outside your own script!

## The Builtins Module

Yyyyyup. All those built-in functions that make Python go have to be defined somewhere, and where that is is the builtins module. The builtins module is treated specially by the interpreter, and exists in a scope at the very bottom of the stack. If it didn't do this, you couldn't use Python in Python.

But what about modules you define?

## Defining Modules, Part 1

Once again, we've already defined modules. In fact, every single Python script we've written has been its own module. In fact, it's more correct to say that every _module_ has its own global scope. When you run a script from the commandline, all of its contents go into a module created by the interpreter, with the special name `__main__`. It's this module that holds the `dict` where we keep the `global` namespace.

## How To Reference Other Modules

We bring another module into our current module's namespace using the `import` keyword. We can use `import` anywhere in a script, but we usually put it at the top, so that as the interpreter processes our file in order, the things we import are available everywhere inside our module.

Python provides a module called `logging` as part of its basic installation into your system. It's not a built-in, since you can use the Python language without it, so it's not provided in the built-in scope and you have to import it before you can use it.

Let's do that now, in the REPL (yeah, you can import things in the REPL, too! The REPL instantiates its own `__main__` module for you when it starts up.)

```
>>> import logging
>>> print(logging)
```

Look at that! It's created a module for you in your own module's global namespace, and it's bound it to the name `logging` in that namespace, so you can refer to it.

Inside the logging module, global functions are defined to help you send output from inside your application. One of the things you can do is "warn" the user of your module that something bad might happen. So, how can we access logging's global scope from our global scope?

Well, the imported `module` object has attributes, and we can reference an object's attributes using the `.` notation. A module's attributes are all the names defined in its global namespace. That's it! So let's try...

```
>>> logging.warning("Oops!!")
```

Since it's in our module's global scope, any function we define in this scope can use it from inside its scope, too.

### How did it know where to look?

Much like the way our interpreter looks up names by checking the local scope, then the next one down, etc, the interpreter also has a search order for looking up modules in an `import` statement. The first place it always looks is the local directory we're running in.

## Defining Modules, Part 2

In this directory, you'll find two Python modules. One of them is called `math_tools.py`, and it contains some definitions for mathematical operations. It doesn't ever call any of these functions from the global scope, so if we run it, we won't see it do anything interesting. The interpreter will define all the functions, and then just exit.

The other one is called `main.py`, and that's the one we're going to run. Check out the import statement.

Yup! If the module name you are importing is the same as a filename in your working directory (the one you were in when you ran the script), minus the `.py`, the interpreter will load the module. That means it first executes the whole module, to create the module's global namespace, and then it creates a module object for you, with the module's global namespace stuck inside.

Just like with the `logging` module, we brought the `math_tools` module object into our global scope, not the things inside its namespace. That means that when we use the methods from `math_tools`, we have to reference them as attributes of the module object.

## Another Way To Import

As I just broadly hinted, you're not restricted to importing whole modules. You can use another form of import statement:

```
>>> from logging import warning
>>> warning("OH NO")
```

Try that in the REPL, and you'll see that we have added the `warning` function from `logging` directly into our global scope. The `from` keyword searches for the module and creates it, but does not add anything to scope -- the import keyword then adds only the module attributes you've asked for. That means we don't need to reference it as an attribute of the logging module -- in fact, if you hadn't imported the whole logging module into your REPL a minute ago, you would not be able to reference it this way at all! `warning` would be in your global scope, but `logging` would be undefined.

You can import all attributes from a module (everything in its global scope) into your global scope with `from $module import *`

* That's another programming convention! Putting $ in front of a string in some instructions means "instead of $whatever, put the value you want, without the $." You may also see something like `from <module> import *`, which means the same thing: replace the whole thing, `<>` and all.)

Here, let's try changing the import line of `main.py` to `from math_tools import *`. If you run it just like that, is the result what you expected? What else do you have to change so that your script can run?


