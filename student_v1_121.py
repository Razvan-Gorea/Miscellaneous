#!/usr/bin/env python3

class Student(object):

  def __init__(self, name, cao):
    self.name = name
    self.cao = cao

  def __str__(self):
    return 'Name: {}\nCAO: {}'.format(self.name, self.cao)

def main():
    s1 = Student('Boris Spassky', 21345654)
    s2 = Student('Bobby Fischer', 21907321)

    assert(s1.name == 'Boris Spassky')
    assert(s1.cao == 21345654)

    print(s1)
    print(s2)


if __name__ == '__main__':
    main()
