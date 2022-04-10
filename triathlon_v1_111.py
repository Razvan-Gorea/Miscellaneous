#!/usr/bin/env python3

class Triathlete(object):

  def __init__(self, name, tid):
    self.name = name
    self.tid = tid

  def __str__(self):
    return 'Name: {}\nID: {}'.format(self.name, self.tid)

class Triathlon(object):

  def __init__(self):
    self.agenda = {}

  def add(self, triathlete):
    self.agenda[triathlete.tid] = triathlete

  def remove(self, id):
    if id in self.agenda:
      del(self.agenda[id])

  def lookup(self, id):
    if id in self.agenda:
      return self.agenda[id]
    return None
