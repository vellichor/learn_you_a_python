#!/usr/bin/env python3

if __name__='__main__':
  filename = 'myfile.txt'
  f = open(filename, 'r')
  for line in f:
    print line
  f.close()

