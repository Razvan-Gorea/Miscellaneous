class Student:
#Self.name is an attribute of student.
#Whatever name is passed in is stored in self.name
#Values are assigned to each attributed of the object.
#The student's name is going to equal to the name we passed into the student object.
  def __init__(self, name, major, gpa, is_on_probation):
    self.name = name
    self.major = major
    self.gpa = gpa
    self.is_on_probation = is_on_probation
