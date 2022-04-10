#!/usr/bin/env python3

class Student(object):

  def __init__(self, name, cao):
    self.name = name
    self.cao = cao

  def __str__(self):
    r = []
    r.append('Name: {:s}'.format(self.name))
    r.append('CAO: {:d}'.format(self.cao))
    return '\n'.join(r)

def sort_on(student):
  return student.cao

class Classlist(object):

  def __init__(self):
    self.classlist = {}

  def add(self, student):
    self.classlist[student.cao] = student

  def remove(self, cao_num):
    if cao_num in self.classlist:
      del(self.classlist[cao_num])

  def lookup(self, cao_num):
    if cao_num in self.classlist:
      return self.classlist[cao_num]
    return None

  def __str__(self):
    student_objects = ['{}'.format(student) for student in sorted(self.classlist.values(), key=sort_on)]
    return '\n'.join(student_objects)
