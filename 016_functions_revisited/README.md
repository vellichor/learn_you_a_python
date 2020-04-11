# Functions, Revisited

We've built our share of functions by now, and so far we've used a standard recipe for declaring them:

```
def my_func(some, args):
  print(some)
  print(args)
```

The way we've been specifying our argument list has been very simple, so far: it's just a tuple. We give some names in order, and when we call our function

```
my_func(1, 2)
```

We give our values in the order we specified in the function definition. We call these _positional arguments_. The position where they appear in the tuple of arguments determines how they get assigned.

What happens if we give too many arguments?

```
my_func(1, 2, 3)
```

Whoa Nellie. Tooooo much. But what if I told you... that you could make your function take ANY NUMBER OF POSITIONAL ARGUMENTS???

```
def expandable_func(some, *args):
  print(some)
  print(args)

expandable_func(1, 2)
```

Hmmm.... args looks different than it did before. It seems to be a tuple.

Let's try adding that extra argument back again:

```
expandable_func(1, 2, 3)
```

HEYYYY. You can easily imagine that we could pile as many of those bad boys in there as we want. They'll all just wind up in our tuple called args.

Now, a tuple can be empty. Does that mean....

```
expandable_func(1)
```

WHOA! But what if we leave them all out?

```
expandable_func()
```

Yup. So what we can figure out from this is that

* positional arguments are required, but
* `*` is magic

A single `*` preceding a positional argument means "instead of just taking the next positional value, take ALL the remaining positional values." `args` thus becomes a collection, a tuple, containing all the positional arguments except for the first one.

What would happen if we tried to use it twice?

```
def bogus_func(some, *args, *more):
  print(some)
  print(args)
  print(more)
```

Call that and see what happens. Do you know why?

### The `args` symbol

This is a Python convention: whenever we use a variable-length list of positional arguments, we usually call it `args`. This makes it very easy for other developers to quickly understand what they are looking at.

## Keyword Arguments

Our function arguments have names. It turns out that you can use these names to call the function in a more flexible way. Try this on for size:

```
my_func(args=1, some=2)
```

This is called specifying _keyword_ arguments. Every positional argument is also a _keyword argument_: it can be given by naming it in the function call, and then assigning it a value. An important thing to notice: we referenced `args` in the global scope, even though we only defined it in the scope of `my_func()`! This is a special circumstance where that is allowed -- the interpreter knows what to do, because it knows we have called the function and can determine what namespace to look it up in.

What happens if we do

```
myfunc(args=1, some=2, potato=3)
```

YUP. There's the proof: the interpreter knew that the namespace for these keywords was "keywords accepted by `my_func()`", and so it knew that potato didn't make any sense.

Now, there IS a way to accept arbitrary keyword arguments to your function -- the caller can specify any ones they like. Let's try this out:

```
def flexible_func(some, args, **kwargs):
  print(some)
  print(args)
  print(kwargs)

flexible_func(args=1, some=2, potato=3)
```

Check that out! Now again, the symbol `kwargs` isn't magic -- it just stands for _keyword arguments_ and is a convention observed by Python developers so that it's obvious what's going on when you read the code. The magic happens with those two little `**`. Just as `*` means "assign all the remaining positional arguments here as a tuple", `**` means "assign all the remaining keyword arguments here as a dict." That's all.

## Default Arguments

As we've seen, unless they are wrapped in the _variadic_ notations of `*args` and `**kwargs`, positional/keyword arguments are REQUIRED. What if we wanted to make some of these arguments optional?

For example, I want to increment a number:

```
def incr(x):
  return x + 1

print(incr(4))
```

But what if I want to let it be incremented by any step?

```
def incr(x, step):
  return x + step

print(incr(4, 2))
```

OK, but that's not much different from adding. However, most of the time when I want to increment something, I really just want to increment by 1. How can I make it so things increment by 1 UNLESS I TELL THEM NOT TO?

```
def incr(x, step=1):
  return x + step
```

Yup. It's that simple. Using a notation that looks very much like keyword arguments, you can prepopulate your argument with a value that will be used if your caller leaves it out.

```
print(incr(4))
print(incr(4, 2))
```

Now that you know what wild things we can do with arguments, and how many different ways the same function can be called (we call this _polymorphism_!), let's look at the actual docs for the `range` object we've used in `for` loops: [https://docs.python.org/3.7/library/stdtypes.html#ranges]

Look at the different ways you can call this object.

If you had to implement it yourself, defining an `__init__()` function that could take 1, 2, or 3 arguments, do you think you could do it using variadic arguments? How would you do it?

## Playtime

Go ahead, try it. Open up a new Python script and define a class called MyRange that can be constructed the same way as `range`, and populates itself with the same list of numbers.

Verify that you are right by building `for` loops on `range()` and `MyRange` objects, with the same values, and seeing if they act the same way.