#!/usr/bin/env python3

try:
  print(a)
except Exception as e:
  print("General Exception {}".format(e))
except NameError as n:
  print("NameError {}".format(n))

