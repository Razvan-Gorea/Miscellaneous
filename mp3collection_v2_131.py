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

  def add(self, track):
    self.collection[track] = track.artists

  def remove(self, title):
    if title in self.collection:
      del(self.collection[title])

  def lookup(self, title):
    if title in self.collection:
      return MP3Track(title, self.collection[title])
    return None

  def get_mp3s_by_artist(self, artist):
    artist_all_tracks = []
    for tracks in self.collection:
      if artist in self.collection[tracks]:
        artist_all_tracks.append(tracks)
    return artist_all_tracks
