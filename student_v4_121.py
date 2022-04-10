#!/usr/bin/env python3

class Student(object):

  def __init__(self, name, cao):
    self.name = name
    self.cao = cao
    self.d = {}
    self.converter = {"H1": 100, "H2": 88, "H3": 77, "H4": 66, "H5": 56, "H6": 46, "H7": 37, "H8": 0, "O1": 56, "O2": 46, "O3": 37, "O4": 28, "O5": 20, "O6": 12, "O7": 0, "O8": 0}

  def add_grade(self, subject, grade):
    self.d[subject] = grade

  def get_grade(self, subject):
    if subject in self.d:
      return self.d[subject]
    return "N/A"

  def total_points(self):
    converted = [self.converter[grade] for grade in self.d.values()]

    if len(self.d) < 3:
      total = sum(converted)
    else:
      top_three_marks = sorted(converted, reverse=True)[:3]
      total = sum(top_three_marks)
    return total

  def __eq__(self, other):
    return self.total_points() == other.total_points()

  def __lt__(self, other):
    return self.total_points() < other.total_points()

  def __gt__(self, other):
    return self.total_points() > other.total_points()

  def __str__(self):
    return 'Name: {}\nCAO: {}\nPoints: {}'.format(self.name, self.cao, self.total_points())

def main():

    s1 = Student('Boris Spassky', 21345654)
    s2 = Student('Bobby Fischer', 21907321)
    s3 = Student('Mikhail Tal', 21884786)

    s1.add_grade('english', 'H2')
    s1.add_grade('irish', 'H3')
    s1.add_grade('chemistry', 'H5')
    print(s1)

    s2.add_grade('irish', 'H3')
    s2.add_grade('physics', 'H2')
    s2.add_grade('french', 'O1')
    print(s2)

    s3.add_grade('art', 'H1')
    s3.add_grade('music', 'H2')
    s3.add_grade('woodwork', 'H2')
    print(s3)

    assert(s1 == s2)
    assert(s1 < s3)
    assert(s3 > s2)


if __name__ == '__main__':
    main()
