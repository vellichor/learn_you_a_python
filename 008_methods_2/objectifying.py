#!/usr/bin/env python3

class Animal(object):

  def __init__(self, color):
    self.color = color
    self.type = "animal"

  def eat(self, food):
    print("The {} {} ate the {}".format(self.color, self.type, food))


class Possum(Animal):

  def __init__(self, color):
    super().__init__(color)
    self.type = "possum"

  def hide(self):
    print("Possums away!!")

critter = Animal("brown")
critter.eat("kibble")

my_critter = Possum("grey")
my_critter.eat("trash")
my_critter.hide()
