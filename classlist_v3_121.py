#!/usr/bin/env python3

class Student(object):

  def __init__(self, name, cao):
    self.name = name
    self.cao = cao
    self.d = {}

  def add_grade(self, subject, grade):
    self.d[subject] = grade

  def get_grade(self, subject):
    if subject in self.d:
      return self.d[subject]
    return "N/A"

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

  def most_popular_subject(self):
    subjects = []
    #Accessing the student objects which are in the values of the self.classlist dictionary
    for object in self.classlist.values():
        #Adding the subject of each student into the subjects list
      for subject in object.d.keys():
        subjects.append(subject)
    #Using a set to find the most common subject based on appeared frequency
    return max(set(subjects), key=subjects.count)

  def __str__(self):
    student_objects = ['{}'.format(student) for student in sorted(self.classlist.values(), key=sort_on)]
    return '\n'.join(student_objects)

def main():

    cl = Classlist()
    s1 = Student('Boris Spassky', 21345654)
    s2 = Student('Bobby Fischer', 21907321)
    s3 = Student('Mikhail Tal', 21884786)

    s1.add_grade('english', 'H1')
    s1.add_grade('irish', 'O4')

    s2.add_grade('english', 'H2')
    s2.add_grade('french', 'O5')
    s2.add_grade('spanish', 'O1')

    s3.add_grade('english', 'O3')
    s3.add_grade('irish', 'O3')

    cl.add(s1)
    cl.add(s2)
    cl.add(s3)

    print(cl.most_popular_subject())


if __name__ == '__main__':
    main()
