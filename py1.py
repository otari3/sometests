li = [[3,'three'],[7,'seven'],[10,'five'],[14,'forteen']]
linecunter = 1
index = 0
last = li[-1][0]

with open('numer.txt','w') as file:
  while linecunter<=last:
    if linecunter in li[index]:
     file.write(li[index][1]+ '\n')
     index+=1
    else:
     file.write('\n')
    linecunter+=1
