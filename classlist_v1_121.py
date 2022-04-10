#!/usr/bin/env python3

class Student(object):

    def __init__(self, name, cao):
        self.name = name
        self.cao = cao

    def __str__(self):
        return 'Name: {}\nCAO: {}'.format(self.name, self.cao)

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