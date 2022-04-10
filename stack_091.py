#!/usr/bin/env python3

class Stack(object):

  def __init__(self):
    self.stack = []

  def push(self, e):
    self.stack.append(e)

  def pop(self):
    return self.stack.pop()

  def top(self):
    return self.stack[-1]

  def is_empty(self):
    return len(self.stack) == 0

  def __len__(self):
    return len(self.stack)

#In this program, the stack is a list.
#Push method adds element at the top of a stack.
#Pop method removes and return the element at the top of the stack..
#in this case it removes and returns the last element of the list.
#Top method returns a reference to the element at the top of the stack.
#Is empty method tells us if the stack is empty.
#Last in, first out order (LIFO)
#Theory: elements added to the top of the stack and the element at the top..
#will always be removed first, then the next top element and so on..
#the first ever element of the stack which is at the very bottom of the..
#stack will be removed last.
#Afterwards the stack will be empty.
