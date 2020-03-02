s = open("output2.txt","r")
r = open("output3.txt", "w")
thisKey = ""
thisValue = 0.0
for line in s:
  data = line.strip().split(',')
  usertype, tripduration = data
  if usertype != thisKey:
    if thisKey:
      # output the last key value pair result
      r.write(thisKey + '\t' + str(thisValue)+'\n')
      # start over when changing keys
    thisKey = usertype 
    thisValue = 0.0
# apply the aggregation function
  thisValue += float(tripduration)
# output the final entry when done
r.write(thisKey + '\t' + str(thisValue)+'\n')
s.close()
r.close()