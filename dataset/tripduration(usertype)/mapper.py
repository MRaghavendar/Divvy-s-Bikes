# Reading data from data.txt file and writing into output1.txt file
input_mapper = open("data.txt","r")
output_mapper = open("output1.txt","w")
# iterating and reading each line in the data set
for line in input_mapper:
    # dividing the data using comma seperator
    data = line.strip().split(',')
    # storing the values in variables
    if (len(data) == 12):
        trip_id, start_time, end_time, bikeid, tripduration, from_station_id, from_station_name, to_station_id, to_station_name, usertype, gender, birthyear = data
        # writing the output to the output1.txt file
        output_mapper.write(usertype+","+tripduration+"\n")
input_mapper.close()
output_mapper.close()