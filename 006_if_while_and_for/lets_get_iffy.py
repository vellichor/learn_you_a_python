#!/usr/bin/env python3

def bigger_than_5(x):
  if x > 5:
    print(str(x) + " is bigger than 5!")
  elif x == 5:
    print("x is actually 5")
  else:
    print(str(x) + " is less than 5 =(")
  print("Checked out the number " + str(x))

bigger_than_5(6)
bigger_than_5(2)
bigger_than_5(5)

