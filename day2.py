f = open("input.txt", "r")
score = 0

for line in f:
  line = line.strip()
  temp = line.split(" ")
  if temp[0] == "A":
    if temp[1] == "X":
      score+=4
    elif temp[1] == "Y":
      score+=8
    else:
      score+=3
  elif temp[0] == "B":
    if temp[1] == "X":
      score+=1
    elif temp[1] == "Y":
      score+=5
    else:
      score+=9
  elif temp[0] == "C":
    if temp[1] == "X":
      score+=7
    elif temp[1] == "Y":
      score+=2
    else:
      score+=6

print(score)