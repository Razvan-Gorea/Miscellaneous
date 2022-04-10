#!/usr/bin/env python3

import sys

comparison_word = sys.stdin.readline()
comparison_word = comparison_word.strip()
#Splitted excludes the dashes
splitted = comparison_word.split('-')

words = [line.strip() for line in sys.stdin]

length_filter = []
for word in words:
  if len(word) == len(comparison_word):
    length_filter.append(word)
#Compares if the letters of the comparison word are present in each of the other words
#If a word passes the flag check then it matches with the comparison word
filtered = []
for words in length_filter:
  flag = True
  for chars in splitted:
    if chars not in words:
      flag = False
  if flag is True:
    filtered.append(words)

#Print something only if 'filtered' isn't empty
if len(filtered) != 0:
  print(', '.join(filtered))
else:
  pass
