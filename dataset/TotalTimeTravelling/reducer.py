s = open("output2.txt","r")
r = open("output3.txt", "w")

thisKey = ""
thisValue = 0.0
for line in s:
  data = line.strip().split(',')
  from_station_name, tripduration = data
  if from_station_name != thisKey:
    if thisKey:
      r.write(thisKey + '\t' + str(thisValue)+'\n')
    thisKey = from_station_name 
    thisValue = 0.0
  thisValue += float(tripduration)
r.write(thisKey + '\t' + str(thisValue)+'\n')
s.close()
r.close()