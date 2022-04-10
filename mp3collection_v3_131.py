#!/usr/bin/env python3

class MP3Track(object):
  def __init__(self, title, duration, artists):
    self.title = title
    self.duration = duration
    self.artists = artists

  def __str__(self):
    return 'Title: {}\nBy: {}\nDuration: {}'.format(self.title, ", ".join(self.artists).strip(), self.duration)

class MP3Collection(object):
  def __init__(self):
    self.collection = {}
    self.second_collection = {}
    self.third_collection = {}

  def add(self, other):
    self.collection[self] = other.title
    self.second_collection[self] = other.duration
    self.third_collection[self] = other.artists

  def __add__(self, other):
    new_duration = self.second_collection[self] + other.second_collection[other]
    new_title = self.collection[self] + ' ' + other.collection[other]
    new_artists = []
    for x in self.collection.values():
      if x not in other.collection.values():
        new_artists.append(x)
    self.add(MP3Track(new_title, new_duration, new_artists))
    return MP3Collection()

    print(self.collection, other.collection)
    print(self.second_collection, other.second_collection)
    print(self.third_collection, other.third, collection)
