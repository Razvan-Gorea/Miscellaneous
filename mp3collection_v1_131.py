#!/usr/bin/env python3

class MP3Track(object):
  def __init__(self, title, duration):
    self.title = title
    self.duration = duration

  def __str__(self):
    return 'Title: {}\nDuration: {}'.format(self.title, self.duration)

class MP3Collection(object):
  def __init__(self):
    self.d = {}

  def add(self, track):
    self.d[track.title] = track

  def remove(self, title):
    del(self.d[title])

  def lookup(self, title):
    if title in self.d:
      return self.d[title]
    return None
