s = open("output1.txt","r")
r = open("output2", "w")

thisKey = ""
thisValue = 0.0
for line in s:
  data = line.strip().split(',')
  bikeid, tripduration = data
  if bikeid != thisKey:
    if thisKey:
      r.write(thisKey + '\t' + str(thisValue)+'\n')
    thisKey = bikeid 
    thisValue = 0.0
  thisValue += float(tripduration)
r.write(thisKey + '\t' + str(thisValue)+'\n')
s.close()
r.close()