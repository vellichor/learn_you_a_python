#!/usr/bin/env python3

# Here, we're in the global scope! We'll define some stuff.

snacks = ["chips", "carrot sticks", "chocolate"]

def add(x, y):
  # here, we're in the scope of add().
  # we can still look at things in the global scope from here!
  print ("In the scope of add(), we have snacks! {}".format(snacks))
  return x + y

# Now we've exited the scope of add(), and this line would cause a NameError:
# print("The value of x is {}".format(x))
print("We have snacks in global scope: {}".format(snacks))

# We'll define another function that calls our first function
def add_5(x):
  # x means something different in this scope than it does in add().
  return add(5, x)

# what does the scope stack look like as we make this function call?
x = add_5(7)

# now, x is defined in the global scope, too!
print("The global value of x is {}".format(x))

# let's define something with str type.
my_string = "badgers, again??"
print("The type of my_string is {}".format(type(my_string)))
print("The value of str is {}".format(str))
print("Is my_string of type str? {}".format(type(my_string) == str))

# now, let's do something really weird.
print("Redefining str in the global scope")
str = "oh no, it's a snake!"

# yeah, we did that! Now str resolves in the global scope
# That means we don't get the built-in anymore!
print("The type of my_string is {}".format(type(my_string)))
print("The value of str is {}".format(str))
print("Is my_string of type str? {}".format(type(my_string) == str))

# we can use the del keyword to delete something from the local scope
# (currently, the global scope is local too, because it's at the top of the stack.)
print("Removing str from the global scope")
del str

# now, we should get back to normal: str has been removed from the global scope,
# so we can see the built-in again.
print("The type of my_string is {}".format(type(my_string)))
print("The value of str is {}".format(str))
print("Is my_string of type str? {}".format(type(my_string) == str))
