# What is a Python?

A python is any snake of genus Pythonidae, a group of non-venomous constricting snakes living in the tropics of the Eastern hemisphere.

A Python, on the other hand, is any of a versioned series of executables serving as an interpreter and execution environment for the Python scripting language, as well as the language defined by that interpreter.

OK, great. What the heck does that mean?

## Scripts and Executables

Broadly speaking, there are two ways to write and run code. One is by creating an "executable," a list of binary instructions executed directly by a processor or operating system. These lists of binary instructions are not human-friendly, and are difficult to work with unless you are a VERY particular type of nerd, so we typically create an executable by writing a program in a *compiled* language, and then using a *compiler* to translate that human-readable program into a less-human-friendly instruction set for the processor. You can then run the compiled executable as a separate step.

Since we are translating the whole program to a set of binary instructions, the executable can become very small. However, since instruction sets are specific to a particular processor, it's likely that the executable you compiled for one computer system might not work well on others.

The other way is the Python way. Python is a scripting language, which means that when you write a Python program, you are writing a set of instructions for an executable to interpret and run. That executable is called the *interpreter*. Just like a human interpreter, the interpreter knows both the host language of the computer system (the binary instruction set) and the scripting language (Python, in our case) and takes care of translating the one to the other when it runs. The interpreter, as an executable, is compiled for a particular computer system, in the same way that an interpreter who translates English to ASL would not necessarily be useful for translating English to French.

## Why do I care?

As a scripting language, Python needs to be run by an outside system. Functionally, this means we can expect a few things are true about it:

* It provides a REPL: a Read-Evaluate-Print loop. You can try this now by getting to a command prompt and entering `python`. Enter `exit()` at the `>>>` prompt to get back out.
* When you make changes to your script, they take effect the very next time you run it, rather than needing to be compiled first as a separate step.

## Heck Yeah Let's Interpret Some Stuff

OK awesome!! Fire up that REPL again by entering `python` at the command line.

You should see something like

```
$ python
Python 3.7.7 (default, Mar 10 2020, 15:43:27) 
[Clang 10.0.0 (clang-1000.11.45.5)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>>
```

Those `>>>` arrows are your Python prompt, and everything you type there will be Read, Evaluated (interpreted) and the results will be Printed. Let's try:

```
>>> "Badger badger badger"
'Badger badger badger'
```

What happened there? Well, you entered the text "Badger badger badger" in quotes. (We'll call any item of regular old text a `string`, so you created a `string` with the contents "Badger badger badger".) The interpreter *read* your opening quote, said "Aha! A string is coming!" and *evaluated* everything up until the closing quote into a brand new `string`. Then, it *printed* your new string so you could see what you made.

If you were to type it without the quotes, something very different would happen.

```
>>> badger
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'badger' is not defined
```

Because this was not a quoted string, your interpreter went looking around for something it knew about called "badger". Unfortunately, it doesn't know about badgers yet, so it told you so. Remember this error message! You will probably see it a lot. 

Next, we'll look at what else you can do in the REPL.

