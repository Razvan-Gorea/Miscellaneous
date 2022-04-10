#!/usr/bin/env python3

class Triathlete(object):

  def __init__(self, name, tid):
    self.name = name
    self.tid = tid
    self.times = {}

  def __str__(self):
    r = []
    r.append('Name: {:s}'.format(self.name))
    r.append('ID: {:d}'.format(self.tid))
    r.append('Race time: {:d}'.format(self.total_time()))
    # Take all strings in r and glue them together
    # Strings glues together with a newline character
    return '\n'.join(r)

  def total_time(self):
    # A dictionary mapping from disciplines to times
    if not self.times:
      return 0
    return sum(self.times.values())

  def add_time(self, d, t):
    # Example:
    # d 'cycle'
    # t 100
    # self.times['cycle'] = 100
    self.times[d] = t

  def get_time(self, d):
    if d in self.times:
      return self.times[d]
    else:
      return None

    # support == in terms of overall race time
    # because we have these methods, python
    # can sort our triathletes for us <>
    # it can sort them because it can compare them
    # if it can sort them then it can calculate a minimum and a maximum
  def __eq__(self, other):
    return self.total_time() == other.total_time()

  def __gt__(self, other):
    return self.total_time() > other.total_time()

class Triathlon(object):

  def __init__(self):
    # use d to map from tids to Triathlete objects
    self.d = {}

  def add(self, t):
    # add triathlete t to triathlon self
    self.d[t.tid] = t

  def remove(self, tid):
    del(self.d[tid])

  def lookup(self, tid):
    # A mapping from tid to a triathlete
    if tid in self.d:
      return self.d[tid]
    return None

  def __str__(self):
    # Print the details of each triathlete
    # First convert each triathlete to its string representation
    # Triathletes are in self.d.values()
    slist = ['{}'.format(t) for t in sorted(self.d.values(), key=sort_on)]
    return '\n'.join(slist)

  def best(self):
    # return the triathlete with the worst race time
    return min(self.d.values())

  def worst(self):
    # return the triathlete with the best race time
    return max(self.d.values())
