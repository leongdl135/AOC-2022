f = open("input.txt", 'r')

score = 0
max = 0

for line in f:
  if line == "\n":
    if score > max:
      max = score
    score = 0
  else:
    score += int(line)

print(max)
