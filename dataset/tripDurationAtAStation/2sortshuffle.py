unsorted = open("mapperOutput.txt", "r")
sorted = open("shuffleoutput.txt", "w")

dataList = unsorted.readlines()
dataList.sort()

for line in dataList:
    # print (line)
    sorted.write(line)

unsorted.close()
sorted.close()