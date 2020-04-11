# More Types

We've seen the built-in types `str`, `int`, `float`, and `list`. What else does Python's basic type set have to offer us?

## True, False, and None

These are values you'll see and use extremely frequently. True and False are of type `bool` and are the only two possible values of this type. None is of the special type `NoneType` and is the only one of its kind.

None is a useful value to set when you want to set up a variable to use later, but don't yet know what its value should be yet. True and False are the values of our conditional expressions in our `while` and `if` statements, where we rely on them to control execution flow.

## Sequences

Sequences are iterable objects. You'll notice that in the last section, I referred to `range` as an object, not a function, even though we called it. That's because what we called was a function built into range that allows us to create different kinds of `range` object. We'll learn more about why that works in sections 008 and 009. We can create most objects this way, but for other objects, we have usually provided a literal instead. `range` has no literal, so you need to create it this way.

Other iterable objects are `list`, which you've seen, and `tuple`, which you haven't. A `tuple` is like a fixed-length list: you can't add anything to it. You construct a literal tuple by enclosing some values in parentheses: 

```
>>> my_tuple = (0, 1, 2)
>>> type(my_tuple)
```

If this looks familiar, that's because you've used them before: when we define functions, we write the argument list as a tuple.

## Mappings

The only type of mapping built into Python is `dict`. We haven't seen one yet, but deep down in the Python internals, we are using them all the time. A literal dict is defined using curly braces `{}`:

```
>>> my_dict = {"a": 1, "b": 2}
>>> type(my_dict)
```

Mappings are like translation or lookup tables: we use them when we want to look up one piece of information by giving another. That's why their name is short for _dictionary_. You can probably think of other places in Python where we want to use one thing to look up another -- your suspicions may be validated in section 010. We call the thing we use for lookups the `key`, and the thing we looked up the `value`: in this case "a" and "b" are keys and 1 and 2 are values.

To look up something in a `dict`, we use `[]` again, just like we did in retrieving members of a `list`. Instead of a number, we give the key we want to look up:

```
>>> my_dict["a"]
```

## More Types Than You Can Shake A Stick At

For a really exhaustively complete list of types that Python supports, go on in [here]()[https://docs.python.org/3.7/library/stdtypes.html].

## Build Your Own Example

There's no sample code for this section, since we did it all in the REPL, but feel free to take a crack at writing a script from scratch to try out a couple of these new types.
