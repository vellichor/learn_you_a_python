#!/usr/bin/env python3

# Here comes some evil Python magic!

# Let's define a variable in the global scope.
my_global_str = "Hey now, here we go now"

# Now, let's define a function that can modify that scope.
def make_a_mess(x):
  # first tell the interpreter that we want to look this up in the global scope
  global my_global_str
  # now we can assign to it as if it were ours.
  my_global_str = x

print("Before making a mess...")
print(my_global_str)
make_a_mess("WHAT A DISASTER!!")
print("After making a mess...")
print(my_global_str)

# since we modified the global scope directly, del can't save us!
# our old value is gone forever.

# now, let's make things worse.
def outer_function():
  outer_function_var = 0
  print("This function's variable is {}".format(outer_function_var))
  make_a_bigger_mess()
  make_a_bigger_mess()
  print("This function's variable is {}".format(outer_function_var))
  make_a_bigger_mess()

def other_outer_function():
  outer_function_var = 1
  print("This other function's variable is {}".format(outer_function_var))
  make_a_bigger_mess()
  print("This other function's variable is {}".format(outer_function_var))
  make_a_bigger_mess()
  make_a_bigger_mess()
  print("This other function's variable is {}".format(outer_function_var))

def make_a_bigger_mess():
  nonlocal outer_function_var
  outer_function_var += 1 # every time this runs, we'll bump up the outer variable.

outer_function()

other_outer_function()

# now what happens if we run this by itself? how will it know what to increment?
# try uncommenting it and see!
# make_a_bigger_mess()
