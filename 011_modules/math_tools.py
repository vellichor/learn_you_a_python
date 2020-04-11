#!/usr/bin/env python3

def add(x, y):
  return x + y

def round(x):
  # short-circuit: don't need to round an int
  if type(x) == int:
    return x
  else:
    # casting to an int truncates the fractional part.
    # if adding 0.5 to this value doesn't change the truncation, round down
    if int(x) == int(x + 0.5):
      return int(x)
    else:
      # round up!
      return int(x) + 1

def sqrt(x):
  # start with 1/2 x
  y = x / 2
  y_sq = y * y
  # if it's too far off, try adjusting it.
  while abs(y_sq - x) > 0.001:
    # if it's too small, increase it by half its value
    if y * y < x:
      y = y * 1.5
    else:
      # it's too big. decrease it by 10%.
      y = y * 0.9
  # if we broke out of the loop, we got close enough.
  return y


