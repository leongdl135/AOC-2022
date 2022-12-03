import math


f = open("day3\input.txt", "r")

total = 0

for i in range(100):
  one = f.readline()
  two = f.readline()
  three = f.readline()
  for i in one:
    if i in two and i in three:
      if i.islower():
        total += ord(i) - 96
      else:
        total += ord(i) - 38
      break


print(total)