# Scope

Not just for fresher breath! I promised back in section 008 that we would talk about scope, and that it had something to do with where we can or can't call the functions we have written.

Since we've already written and run quite a bit of Python, it should come as no surprise that we've actually been using scope all along. Take a look back in `function_sample.py`, which we used back in section 003 and which I've copied here, so we can play around with it. Look at all the times we use the variable `x`.

Up on line 3, we declare that `x` is the name for the argument that we receive when someone calls `add_5()`. Inside of `add_5()`, we then use `x` to do the work of the function and get an answer to return.

But in line 8, here's `x` again! This time, it refers to the argument of `add()`. Now, you might have assumed that when we define it again, it overwrites the definition we had before. And if these definitions were occurring in the same _scope_, you'd be right! But maybe, when you were working with this script before, you may have tried to add some statements that used `x` without indenting it -- that is, _not_ inside the body of either functions. If so, you'll have noticed something interesting: you got that error I warned you to get nice and familiar with!

```
NameError: name 'x' is not defined
```

## What gives?

Well, each of these functions defines its own _scope_. That is, when we are inside this function, we can define some variables, and those names exist as long as we're inside that function. Once our execution flow steps outside the function, though, those variables go _out of scope_: we no longer have access to the things we knew inside that function. We call the set of names that are defined in each scope its `namespace`.

At any given point in your execution flow, the interpreter is aware of some symbols, and not aware of others. Moreover, each symbol that the interpreter is aware of in this moment maps to exactly one value. (How else could it get anything done?) The symbols that are currently known to the interpreter, and their values, are determined by the layers of _scope_ you are in.

### Scopes Can Be Layered!

At all times, anywhere within Python, there is a `built-in` scope. This consists of the basic set of Python symbols, like names of built-in functions and classes. You can think of this as the bottom layer of the scope stack: it's always there, and provides the basics of the Python language.

Next, there is a `global` scope. This scope starts out empty, but your script can define names in this scope. A different script will have a different `global` scope. When we define functions in the top level of the script (that is, not inside any class definition or function call) or at the `>>>` prompt in the REPL, we're defining them in this script's `global` scope.

Each time we call a function, we create a new scope: the scope of this function call. It layers on top of the existing stack of scope, and starts out fresh every time; the first thing to be added are our argument bindings, and it then collects all names that are defined as our function call executes.

When we operate inside a class definition, we layer on another new scope, which collects all the names we define during the class definition (names of functions, variables, or even inner classes, as long as they're defined inside this class block!) This scope stays at the top until the class definition finishes executing, and then the set of names in the scope is frozen into a set of class _attributes_: names that have a meaning inside of this class. When we refer to `str.format()`, we are referring to such an attribute: our current scope understands what `str` is, and understands that to find out what `format` means, it needs to look in the attribute list of `str`.

### Namespaces

The set of names defined in a certain scope is called a _namespace_. When the interpreter is executing your code and encounters a symbol it needs to look up, it checks each of these namespaces in order, from the top layer of scope, to the one underneath, to the one underneath, all the way down to the global scope. As soon as it finds a matching name, it decides that's what you meant and moves on. If it doesn't find any match, it returns a NameError, like the one we've seen so many times.


### Scopes Have State

We can change the namespace in a particular scope, and in fact, we've been doing it all along! Every time we make an assignment, we create a new entry in the namespace of the scope that is at the top of the stack. By using the keyword `del`, we can remove an entry from that namespace as well:

```
>>> x = 5
>>> del x
```

We call this top scope the _local_ scope; what scope is "local" at the moment will change as your script executes, because it's just the name for whatever is on top. That means that if you make an assignment, you can accidentally (but temporarily) change the meaning of that symbol, and it will stay changed until you unassign it or exit this local scope! This is called _shadowing_: your new local assignment shadows the one from the outer scope.

## Assigning Outside The Local Scope

Some really arcane magic is here, in `too_much_fun.py`. I'll explain this behavior now, but please be warned that under normal circumstances you will almost never do this. Assigning outside the current local scope means making changes that will affect the behavior of parts of your code that seem unrelated. Later on we'll mention some useful tools that take advantage of this kind of assignment for some very specific reasons.

### Global Assignment

From anywhere in your code, you can assign to the global namespace. These changes stay in the global namespace after you leave your local scope, and are seen by everything that executes after your code has run. This means that by running one function, you can affect the behavior of all the functions that run later on.

### Nonlocal Assignment

This one is even weirder! In nonlocal assignment, instead of assigning to the local scope, the interpreter looks up the symbol in the usual way: from the local scope, it works its way down to the global and then the built-in scope. Wherever it finds a match, it makes your assignment in THAT namespace!

Since scopes can and do appear and disappear as execution flows through your script, taking their namespace with them, your assignment will last until the next time the namespace you assigned to goes out of scope. When it comes back into scope, though, it will be recreated fresh, and your assignment will have disappeared. As you can imagine, this can make an enormous and confusing mess.
