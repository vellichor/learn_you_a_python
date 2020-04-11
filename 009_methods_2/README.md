# Methods To The Madness, Part 2

OK, you asked for it. (Maybe you didn't.) We're going to bind our own methods! For that, we have to define a new class to bind them to!

We'll use `objectifying.py`. There's a lot in here. Two new classes of Animal of our very own, a way to initialize them, and a method called `eat()` which allows our Animals to eat stuff. Line by line:

## The Class definition

Class definitions start with the `class` keyword. Anatomically, they look a lot like a `def` function definition: there's the `class` keyword, then a symbol (this time, it starts with a capital letter! This is a Python convention, which is to say it's a habit programmers are in and it makes it easier for all the other programmers if you have this habit too.) The symbol this time defines the name of the class we're making.

Next there are parentheses again. This time, it's not an argument. This time, it's a "superclass". That is, what other class that already exists is a more general version of this?

If there's no obvious answer to this, use "object". This is the most generic type of Python object and is a safe place for you to base your class on.

Finally there's the `:` indicating that there's going to be an indented body coming up.

## The `__init__()` Method

If we want to make a new Animal, we need to be able to set up the basic properties that it has. Our Animal has a color. We define a method inside a class just as we would define a function outside of the class context, using the `def` keyword, and the basic anatomy is the same. The difference is that invisible argument we mentioned in the last section. There really IS an invisible argument to all bound methods, and that argument is _the bound object itself_! By convention, we call it `self`.

The `__init__()` method is a special name for the method that will be invoked when we call our class. (Yep, a class is a callable too! Calling it invokes the `__init__()` method and then returns the initialized object.)

Inside the `__init__()` method, we set the properties our animal will have. Each property is bound to the object in the same way that the method is, so we refer to it the same way: joining the bound property to the bound object with a `.` like `self.color`. We set the type of this animal to the literal "animal."

Down on line 22, you can see that we can create an Animal now, passing in the color. The invisible `self` argument is supplied by the interpreter when it runs your code.

## The `eat()` Method

Critters gotta eat! Give your critter some food, and we will print that it ate the food. Again, notice that we have the `self` argument at the head of the argument list, and we use that to find out what color and type our animal is.

## Another Class Definition!

There are lots of types of animals that eat, and one is the noble Possum! We are going to define the Possum with the `superclass` of Animal. Another way to say this is that Possum _inherits_ from Animal. What that means is that all Possums have the methods and properties designed for Animals, as well as any that we add in the Possum definition. Our possums can eat!

Since the superclass sets its type to "animal", we need to first make sure the superclass's `__init__()` method runs, then reset the type of our Animal to "possum". `super()` is how to reference the superclass from within this class's `__init__()` method.

## One More Method

Possums are good at hiding.

## Creating Our Objects

Now that we've defined for the interpreter what an Animal and a Possum are, we can create some. I'm going to introduce the term `instance` at this point, which is how we refer to a particular item we've created in our script: `critter` is an _instance_ of `Animal`. This piece of vocabulary will come in handy when we're talking about a number of different instances in the same script that all have the same type, as well as for differentiating between the two ways we can call these functions we define in the class.

### Instance Methods

After creating our instance of `Animal` on line 22, we call the method we defined, binding it to the instance. Since it's bound to the instance, we have our invisible `self` argument supplied for us, and we only need to supply the food we want our `critter` to eat.

### Class Methods

For our Possum, we show both ways of calling the `eat()` method. First, we bind it to the instance again. But the second time, we instead bind it to the `class` that defines it! This time, the `self` argument is not supplied by the interpreter, because from the `class` scope, we don't know which _instance_ of `Possum` to use. That means we supply both arguments explicitly in the call.
 