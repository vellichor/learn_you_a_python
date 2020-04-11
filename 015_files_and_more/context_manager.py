#!/usr/bin/env python3

if __name__=='__main__':
  filename = 'myfile.txt'
  with open(filename, 'r') as f:
    for line in f:
      print line

