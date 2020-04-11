#!/usr/bin/env python3

import argparse

if __name__=='__main__':
  parser = argparse.ArgumentParser()
  parser.add_argument('name', help="you must supply this person's name") # this is a positional arg: it's whatever we get first.
  parser.add_argument('-a', '--age', help="the age of this person") # this is a flag variable
  parser.add_argument('pets', metavar='pet', nargs='*', help="WHO ARE THEIR BABIESSS")
  parser.add_argument('-g', '--goodboys', help="ARE THEY VERY GOOD BOYS??", action='store_true')

  args = parser.parse_args()

  # now we can use the arguments in args
  print("Hi, {}".format(args.name))
  if args.age is not None:
    print("It must be nice to be {}".format(args.age))
  print("I see you have {} gorgeous little buddies!".format(len(args.pets)))
  if len(args.pets) == 0:
    print("That's too bad! Lots of buddies are waiting to be rescued and loved on... I hope you can find a good friend!")
  else:
    if args.goodboys:
      print("SUCH GOOD BUDDIES!!!")
      for pet in args.pets:
        print("Gooboy, {}!!".format(pet))

