# Python Anatomy

This one is long, because we're going to establish a lot of vocabulary for talking about the parts of a piece of Python code. Knowing the names of things will help later lessons go faster, because it'll be easy to identify what we're talking about as we walk through more and more complicated scripts.

## Objects

The basic unit of stuff in the Python environment is an object. When we made our badger string last time, we created a string `object`. There are a couple basic types, or `classes`, including the `string` and a few different numeric classes, like `int` and `float`. We'll get into more differences later, but an `int` has no fractional part (no decimal point or any stuff after it) and the others do.

To see the type of object you have, use `type()`:

```
>>> type("Badger")
<class 'str'>
>>> type(5)
<class 'int'>
>>> type(3.14)
<class 'float'>
```

Knowing what type an object is is important, because the type of an object determines what kind of operations can be applied to it. So, what kind of operations can we apply to these objects?

## Statements, Expressions and Operators

Just like a spoken language, a scripting language is composed of expressions and statements. Each of these is, roughly speaking, one unit of code that makes the interpreter do something using the computer. Each of our `type()` lines above was an expression, and so was our badgery `string` creation: when we evaluate them, they have a value that the REPL can return. A statement, on the other hand, generally makes some kind of change to its local environment -- it may also have a value when evaluated, and if so, it can also be used as an expression.

So what kind of more interesting expressions and statements are there?

### Math

The standard math operators exist in Python. Try the following expressions:

```
>>> 5 + 2
```

```
>>> 6.0 * 2
```

```
>>> 5 / 2
```

We can also compare values:

```
>>> 5 < 3
```

```
>>> 3 < 5
```

What happens if we do

```
>>> 3 = 5
```

Congratulations! You've got an error message. "Can't assign to literal." `assign`?

### Assignment

So far, if you want to compare 5 to a bunch of things, you have to type 5 every time. That's easy enough. But what if you wanted to compare our very long string to things? Do you want to type "Badger badger badger" a bunch of times? You do not! Let's try an experiment:

```
>>> b = "Badger badger badger"
```

This time we didn't get our string back. But now...

```
>>> b
```

We've assigned a value to `b`, so the REPL will give us back that value if we ask for `b`.

`=` is Python's *assignment operator*. Our assignment statement has two operands: the thing on the left and the thing on the right. The left hand side (LHS) of an assignment is a `variable name` and the RHS is an expression giving the value we want that name to represent. The assignment operation sticks them together: from now on, unless we change it, every time we type `b`, the interpreter knows we mean a `string` with the contents "Badger badger badger".

This statement has made a change to its environment: before we made the statement, `b` was not defined, and after we made it `b` was defined and had a value.

So let's get back to our mathematical comparison problem (and this time we'll throw in some assignment, for fun):

```
>>> a = 3
>>> a == 5
```

`==`, two equals signs in a row, is the `equality operator`. Since `=` is already taken, for assignment, we need to use `==` to compare two values for equality. Try entering just `a` again, at the prompt. Did you get what you expect?

Remember our error message: `can't assign to literal`? We know what assignment is, but what's a literal? Simply: a literal is an exact value that you've typed in, like `5` or `"potato"`. A thing that is not a `literal` is a `symbol`: a thing that stands for another thing. To be legal in Python, and not confuse the interpreter, a `symbol` needs to be an unquoted sequence of letters, numbers, or `_`. A good symbol, or variable name, should

* be short enough to make your statements readable
* be descriptive enough to easily remember what it is

Some good variable names: `my_num`, `first_name`, `address`.
Some not very good variable names: `tuna_fish_sandwich_with_mayonnaise`, `number_we_need_to_keep_during_this_function`, `value`, `x`.

An assigned variable is just a name for the value you assigned to it, so it has the same type:

```
>>> type(a)
```

In checking the type of your variable, you've just used a `built-in function`! `type` is one of the basic functions that lets Python, well, function. Built-in functions can be called from anywhere in a Python script without doing anything extra.

## Function Function, What's Your Function?

A `function` is another class of `object`. A function is a way to attach a name to a block of statements, and then apply that block of statements to some values. The block of statements is called the *body* of the function, and the values you give it are the *arguments*. `type()` is a function named `type` that takes one `argument`. We supply the argument to the function by putting it between the parentheses. When we apply a function to some value or values, we say that we've *called* it. Calling a function is, in turn, another kind of statement!

This section is short, but you'll use functions all the time. ALL the time.