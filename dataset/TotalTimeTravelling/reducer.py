s = open("output2.txt","r")
r = open("output3.txt", "w")
thisKey = ""
thisValue = 0.0
for line in s:
  data = line.strip().split(',')
  from_station_name, tripduration = data
  if from_station_name != thisKey:
    if thisKey:
      # output the last key value pair result
      r.write(thisKey + '\t' + str(thisValue)+'\n')
      # start over when changing keys
    thisKey = from_station_name 
    thisValue = 0.0
# apply the aggregation function
  thisValue += float(tripduration)
# output the final entry when done
r.write(thisKey + '\t' + str(thisValue)+'\n')
s.close()
r.close()