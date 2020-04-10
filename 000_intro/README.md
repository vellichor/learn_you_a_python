# Setting up your environment for Python 3 development

## Some choices to make

I am going to write most of this tutorial based on the assumption that you are hand-editing text files of code, using a programmer-oriented text editor. Telling you what text editor to use is beyong the scope of these instructions, but I typically use Sublime Text, an editor available for all major operating systems.

Some other tools you might consider:

* PyCharm, a Python oriented IDE
* emacs, a very full-featured editor for the terminal which allows some scripting of its own and a wide variety of useful plugins
* vim, a slightly less full featured but much less complicated editor for the terminal

## Conventions For Commands

When there's something to type at the command prompt, I'll show it with a `$` in front of it:

```
$ ls -l
```

When there's something to type at the Python prompt, I'll show it with Python's triple arrow:

```
>>> print("Hello, world!")
```

### Linux

If you are running Linux, it's almost certain that Python is already installed. Here's how to tell if it's there. Get to a terminal and type:

```
which python
```

If you see something like 


```
$ which python
/usr/local/opt/python/libexec/bin/python
```

then Python is already installed. If you don't see that second line show up, you need to install it using your package manager:

* Ubuntu, Debian: `apt-get install python`
* Arch: `pacman -S python`
* Gentoo: `emerge python`
* Alpine: `apk upgrade && apk add python`
* RedHat/CentOS: `yum install python`

Then verify it's installed by using `which python` again. If you still don't see a second line of output, something went wrong and you're about to get two more powerful lessons in programming: "Googling the error message" and "reading stackoverflow.com." Do those things and try to fix your problems -- you'll know you've won when you can `which python` and get a second line of output that ends in `/python`.

Lastly, I've written this guide for Python 3, since Python 2.7 was sunset as of January 1st, 2020. Check your Python version this way:

```
python --version
```

If it gives you a version number that does not start with 3, try

```
python3 --version
```

If that gets you a version number and not an error message, you'll be using `python3` wherever I use `python` in the following sections.

Now install a text editor. Use your Googling skills to find and install the one you want.

Then meet us in `Section 001`.

### Mac OSX

The best way to install the widest variety of software packages on OSX is using Homebrew. Go to [https://brew.sh/] and follow the instructions there (this is the last time I will *ever* tell you to copy and paste random code from somewhere else on the Internet.)

Once Homebrew is installed (it may take a while) you should do a couple of things:

#### Install Python 3

`brew install python` <-- enter that at the command line and wait until it's done

#### Make Homebrew Python the system default

Open up the file called `~/.bash_profile` using your text editor and add the following line somewhere near the top:

```
PATH=/usr/local/opt/python/libexec/bin:$PATH
```

Then save that file, and enter `source ~/.bash_profile` at the command line to add these changes to your current session. You'll need to do this last command again for every terminal that was already open before you made this change; new ones you open will get it on their own.

Now, do

```
which python
```

If you see something like 


```
$ which python
/usr/local/opt/python/libexec/bin/python
```

then Python is installed. If you don't see a second line of output, something went wrong and you're about to get two more powerful lessons in programming: "Googling the error message" and "reading stackoverflow.com." Do those things and try to fix your problems -- you'll know you've won when you can `which python` and get a second line of output that ends in `/python`.

Now install a text editor. Use your Googling skills to find and install the one you want.

Then meet us in `Section 001`.