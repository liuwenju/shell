#!/usr/bin/env python
# encoding: utf-8

class Person(object):
    def eye(self):
        print "two eyes"
    def breast(self, n):
        print "The breast is : ", n

class Girl(object):
    age = 25
    def color(self):
        print "The girl is white."

class HotGirl(Person, Girl):
    pass

if __name__ == "__main__":
    kong = HotGirl()
    kong.eye()
    kong.breast(90)
    kong.color()
    print kong.age
