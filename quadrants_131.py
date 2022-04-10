#!/usr/bin/env python3

import sys

for line in sys.stdin:
  line = line.strip().split()
  left, right = int(line[0]), int(line[1])
  if left > 0 and right > 0:
    print(1)
  elif left > 0 and right < 0:
    print(2)
  elif left < 0 and right < 0:
    print(3)
  elif left < 0 and right > 0:
    print(4)
  elif left == 0 and right == 0:
    print("Touches all four quadrants")
  else:
    print("Error Occurred")
