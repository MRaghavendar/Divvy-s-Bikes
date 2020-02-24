s = open("shuffleoutput.txt","r")
r = open("reducerOutput", "w")
count=0
thisKey = ""
thisValue = 0.0
for line in s:
  data = line.strip().split(',')
  bikeid, tripduration = data
  if bikeid != thisKey:
    if thisKey:
      r.write(thisKey + '\t' + str(thisValue/count)+'\n')
    thisKey = bikeid 
    thisValue = 0.0
    count=0
  thisValue += float(tripduration)
  count+=1
r.write(thisKey + '\t' + str(thisValue/count)+'\n')
s.close()
r.close()