# Files and More

## `file` objects

Yup, more objects. We can load a file from the filesystem if we know its path, and we can also create files in the filesystem. It all starts with the `open` command, which returns a `file` object for a path.

Fire up your REPL, and we're going to create a file.

```
>>> import os
>>> f = open('myfile.txt', 'w')
```

Wait, we gave two arguments to the `open` function! I see the path, but what's that other one? Let me fire up my explaining engine... [BOOYAH!](https://docs.python.org/3.7/library/functions.html#open)

Oh. Hah. Yeah, that was just another link to the Python documentation. It was quicker than writing out all the available mode codes that can be supplied as our second argument. As you can see, `'w'` is the code for "open a filehandle for writing, truncating (deleting the contents of) any file that was already there."

Now we can write some content, and then close the file:

```
>>> f.write("Wow, I'm writing things directly to the freaking hard drive!\n")
>>> f.write("It's important to put that newline there.")
>>> f.write("That's the backslash and n at the end.)
>>> f.write("Without that, we'll just keep writing one long line with no breaks.\n")
>>> f.close()
```

Check it out: it's a real file. You can open it yourself and see.

Now, more interestingly, you can read files back in. Try the script in this directory called `file_reader.py`. What does it do right now? What else can you make it do?

Using the things you learned in section 013, can you alter this script to read ANY file from the filesystem, without having to update the code for each new file?

### Context Managers

There's another way to read a file, which can save you from some problems later on. Python has a keyword `with`, which you can see the usage of in the `context_manager.py` example. It does the exact same thing as `file_reader.py`, but using `with`. This causes the open filehandle to act as a context manager, which means that special `__enter__()` and `__exit__()` functions are run at the beginning and end of the following indented block. In this case, the `__enter__()` doesn't do anything, but the `__exit__()` function takes care of closing the file. That way you can't forget to close it, even if the branching logic inside the context manager gets complicated! We will always exit this block, which means that we will always close the file.

Using context managers when they are available is usually good style, because it helps to prevent bugs when resources are not closed properly. In our case, if the filehandle is not closed, new contents may not be flushed (written) to disk, and the file will show as "in use" to the filesystem, which can cause problems later.


## The `os` package

I mentioned the `os` library in section 013, and now we're going to learn how to use it. The most frequent applications of the `os` library are inspecting and using files and environment variables. Just as arguments are one way to change the behavior of your program, reading files and environment from the operating system can also influence how execution flows through the logic of your program.

Earlier, you messed around with `file_reader.py`, and probably got it into a state where you could pass it the name of any file on the command line and read the contents. You may have even tried using some exception handling to deal with what happened if the filename you passed in was no good.

But what happened when you passed in the name of a directory instead?

Probably, what you would want this to do is to print out the names of files in that directory, or the contents that are inside. But to use `open()`, we need to already know the name of the file.

Let's review the docs for the `os` package: [https://docs.python.org/3.7/library/os.html#files-and-directories]

Look in this page for a function called `listdir`. Have you read enough Python docs now to be able to learn to use this function by reading the documentation? Don't forget to

* import it into your namespace before using
* reference it in a way that matches the import style you used

Try modifying `file_reader.py` to do something useful with directories. If you get stuck, you can look at some sample code in `os_example.py`.

