#!/usr/bin/env python3

class Triathlete(object):

  def __init__(self, name, tid):
    self.name = name
    self.tid = tid
    self.sport_records = {}

  def add_time(self, sport, time):
    self.sport_records[sport] = time

  def get_time(self, sport):
    if sport in self.sport_records:
      return self.sport_records[sport]

  def race_time(self):
    total = 0
    for records in self.sport_records:
      total = total + self.sport_records[records]
    return total

  def __str__(self):
    return 'Name: {}\nID: {}\nRace time: {}'.format(self.name, self.tid, self.race_time())

def main():

    t1 = Triathlete('Ian Brown', 21)

    t1.add_time('swim', 100)
    t1.add_time('cycle', 120)
    t1.add_time('run', 150)

    print('Cycle: {}'.format(t1.get_time('cycle')))
    print(t1)


if __name__ == '__main__':
    main()
