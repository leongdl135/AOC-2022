f = open("input.txt", "r")
score = 0

for line in f:
  line = line.strip()
  temp = line.split(" ")
  if temp[0] == "A":
    if temp[1] == "X":
      score+=3
    elif temp[1] == "Y":
      score+=4
    else:
      score+=8
  elif temp[0] == "B":
    if temp[1] == "X":
      score+=1
    elif temp[1] == "Y":
      score+=5
    else:
      score+=9
  elif temp[0] == "C":
    if temp[1] == "X":
      score+=2
    elif temp[1] == "Y":
      score+=6
    else:
      score+=7

print(score)