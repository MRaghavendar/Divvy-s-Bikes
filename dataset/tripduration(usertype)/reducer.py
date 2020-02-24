s = open("output2.txt","r")
r = open("output3.txt", "w")

thisKey = ""
thisValue = 0.0
for line in s:
  data = line.strip().split(',')
  usertype, tripduration = data
  if usertype != thisKey:
    if thisKey:
      r.write(thisKey + '\t' + str(thisValue)+'\n')
    thisKey = usertype 
    thisValue = 0.0
  thisValue += float(tripduration)
r.write(thisKey + '\t' + str(thisValue)+'\n')
s.close()
r.close()