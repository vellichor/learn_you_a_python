# Functions

I've saved functions for now because they're really much easier to deal with in the context of a script. Python is a language that uses whitespace as a syntax element, which means that the number of spaces or tabs before a statement on a line begins is actually part of the language!

From now on, you're going to have to pay a lot of attention to the whitespace characters in your scripts. If your text editor has a setting to make non-printing characters visible, I recommend that you turn it on now.

## The First Function

In the sample script for this section, `function_sample.py`, I've defined a simple function that adds 5 to a number. Let's look through the anatomy of the function, and the script it lives in.

### The First Line

#### The def Keyword

Our function definition on line 3 starts with `def`. `def` is a Python keyword that tells the interpreter that for the symbol that comes next, instead of assigning a value from another expression, we plan to define a function. A function has arguments that it will operate on, a body composed of statements it will execute, and a return value. Some of these can be left out, and as we describe each one, we'll talk about what happens if it's not there.

#### The Function Name

The next piece after the `def` keyword is the function's name. This is the symbol that we'll use to refer to this function when we want to call it later. It has to be a valid Python symbol, so it can't have funny characters or start with a number. Our function is called `add_5`.

#### The Arguments

Next in line after the name of the function is a pair of parentheses `(` `)` between which we'll put a list of arguments. In this case, there is only one argument: the number we will add 5 to. We provide a symbol here that we'll use to refer to the value we are given -- within the body of this function, `x` means the first argument the function is called with.

#### The Colon

The `:` symbol is another special syntax symbol in Python. Appearing at the end of a line, it means that what follows will be a block of statements meant to be invoked after this one.

### The Second Line

We've defined the function's name and arguments, and told the compiler that the body will come next. The second line of the function begins that function body.

Remember, the body of the statement is a block of statements that will be executed in order when the function is called. You'll notice that this statement is indented (I used two spaces.) This means I have *nested* this block of statements inside the function definition. We'll talk about more complex nested structures later on.

In this line, we print the argument we were given to the screen. This is sometimes referred to as a "side effect" of the function -- it is a statement that alters the environment of the function, but it is not the value we want to get back.

### The Third Line

This line is still part of the function body, so it's indented the same amount as the one before it. All members of a block of statements are indented the same amount, and any block nested within that block will be indented one step farther. 

This line of the function body does the work of adding 5 to whatever value x we will be given. We assign the result of the _expression_ `x+5` to `y`.

### The Fourth Line

Here, we give our function its meaning in life. The `return` statement tells us what value to use when the function call is treated as an _expression_. Another way to say this is that the function call _evaluates_ to its return value.

## The Second Function

Now that we've seen the anatomy of the first function, I'll leave it to you to figure out what this next one is doing, and identify each of its parts. Two things to notice:

### The Argument List

This function takes two arguments, not just one. We separate the arguments in the list with `,`

### Returns an expression

We skip assigning the result of this function to an intermediate variable. Instead, we return the expression directly. When this function is called, the expression will be evaluated and its value will be returned. We could have done this in the last function, too, but expanding it made the explanation easier.

## Function Calls

Line 11 calls the first function we wrote. It encloses the function call in a `print()` statement, which means that the function call will be evaluated as an expression and its value will print to the screen.

Line 13 calls the second function.

If you haven't already, go ahead and run the script now. What prints to the screen? Is it what you expected?