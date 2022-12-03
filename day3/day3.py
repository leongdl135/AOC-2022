import math


f = open("day3/input.txt", "r")

total = 0

for line in f:
  one = line[:math.floor(len(line)/2)]
  two = line[math.floor(len(line)/2):]
  for i in one:
    if i in two:
      if i.islower():
        total += ord(i) - 96
      else:
        total += ord(i) - 38
      break

print(total)