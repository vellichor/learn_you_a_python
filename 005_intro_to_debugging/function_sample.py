#!/usr/bin/env python

def add_5(x):
  print(x)
  y = x + 5
  return y

def add(x, y):
  return x + y

print("Calling add_5")
print(add_5(7))

print("Calling add")
add(5, 15)

print("Called all the functions")
