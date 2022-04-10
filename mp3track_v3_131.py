#!/usr/bin/env python3

class MP3Track(object):
  def __init__(self, title, duration, artists=[]):
    self.title = title
    self.duration = duration
    self.artists = artists
    self.artists = ", ".join(self.artists)

  def add_artist(self, artist):
    if len(self.artists) > 1:
      self.artists = self.artists + ", " + artist
    else:
      self.artists = self.artists + artist

  def __str__(self):
    return 'Title: {}\nBy: {}\nDuration: {}'.format(self.title, self.artists, self.duration)
