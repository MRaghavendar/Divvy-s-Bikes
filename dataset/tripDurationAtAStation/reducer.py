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
      # output the last key value pair result
      r.write(thisKey + '\t' + str(thisValue/count)+'\n')
      # start over when changing keys
    thisKey = bikeid 
    thisValue = 0.0
    # apply the aggregation function
    count=0
  thisValue += float(tripduration)
  # output the final entry when done
  count+=1
r.write(thisKey + '\t' + str(thisValue/count)+'\n')
s.close()
r.close()