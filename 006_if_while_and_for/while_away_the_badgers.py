#!/usr/bin/env python

def say_it_n_times(thing_to_say, num_times):
  times = 0 # we have done this 0 times so far
  while (times < num_times):
    print(thing_to_say)
    times += 1 # whoa what's that funky operator! The README explains!
  print("mushroom, mushroom!")


say_it_n_times("badger", 11)

say_it_n_times("snake", 3)
