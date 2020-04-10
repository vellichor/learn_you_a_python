#!/usr/bin/env python

def find_my_stuff(stuff):
  message = "Darling, where are my {}"
  print(message.format(stuff))


find_my_stuff("potatoes")

find_my_stuff(5)

find_my_stuff(["antelopes", "bears", "cobras"])

