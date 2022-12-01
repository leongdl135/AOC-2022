f = open("input.txt", 'r')

score = 0
arr = []

for line in f:
  if line == "\n":
    arr.append(score)
    score = 0
  else:
    score += int(line)

arr.sort(reverse=True)

print(arr[0]+arr[1]+arr[2])
