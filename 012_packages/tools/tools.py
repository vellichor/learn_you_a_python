#!/usr/bin/env python3

def make_potato_uppercase(s):
  lower_s = s.lower()
  potato_s = s
  potato_index = lower_s.find("potato")
  while potato_index > -1:
    potato_s = potato_s[0:potato_index] + "POTATO"
    if potato_index + 6 < len(s):
      potato_s += s[potato_index+6:]
    potato_index = lower_s.find("potato", potato_index+1)
  return potato_s
