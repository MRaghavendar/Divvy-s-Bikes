## Divvy-s-Bikes
- We are working on Divvy's Bike with a group of 3 people.
- Group-08
- section-01

## List Of Developers
- Raghavendar Reddy maddelavedu
- karthik Reddy Muthyala
- Ganesh siripuram

## Links
- https://github.com/MRaghavendar/Divvy-s-Bikes
- https://github.com/MRaghavendar/Divvy-s-Bikes/issues

## Introduction
- In this project we are calculating how many are going to rent from which city and place for particular gender and calculating the trip duration according to the birthyear with unique bike id.

## Datasource 
- This dataset is created from 2018, the data is retrieved from Divvy's Bikes website.

- It has 12 columns with structured format data. In this project, we mainly concentrated on reducing maps and gender columns.

Volume: The dataset size has 50MB and it has 387146 records in this dataset.

Variety:  It is in CSV file which will open in excel and it is the structured format.

Velocity: It is updated daily basis and the data is in a static state.

Veracity: In this data, there are some blank columns and this data is fully clean.   

Value: In this dataset, we can calculate the average users of bikes usage and with these, we can analyzing how many bikes can be sell in the next quarter.

## Datasource Link
- [DataSource](https://www.kaggle.com/michaelshoemaker/divvy-bike-chicago-2018#Divvy_Trips_2018_Q2.csv)

## Big Data Problems 
1. On an average, how many people are renting bikes in a particular area  -  Karthik
2. For particular day how much time they are travelling - Raghavendar
3. For a given from Station I will find the total trip  duration   rented at that station - Ganesh
## Big Data Solutions

 - Ganesh Siripuram
     - Mapper input: 20  lines of data that mapper will read:
      - 1 17536702,1/1/2018 0:12,1/1/2018 0:17,3304,323,69,Damen Ave & Pierce Ave,159,Claremont Ave & Hirsch St,Subscriber,Male,1988
      - 2 17536703,1/1/2018 0:41,1/1/2018 0:47,5367,377,253,Winthrop Ave & Lawrence Ave,325,Clark St & Winnemac Ave (Temp),Subscriber,Male,1984
    - 3 17536704,1/1/2018 0:44,1/1/2018 1:33,4599,"2,904.00",98,LaSalle St & Washington St,509,Troy St & North Ave,Subscriber,Male,1989
    - 4 17536705,1/1/2018 0:53,1/1/2018 1:05,2302,747,125,Rush St & Hubbard St,364,Larrabee St & Oak St,Subscriber,Male,1983
    - 5 17536706,1/1/2018 0:53,1/1/2018 0:56,3696,183,129,Blue Island Ave & 18th St,205,Paulina St & 18th St,Subscriber,Male,1989
    - 6 17536707,1/1/2018 0:56,1/1/2018 1:00,6298,266,304,Broadway & Waveland Ave,299,Halsted St & Roscoe St,Subscriber,Female,1994
    - 7 17536708,1/1/2018 0:57,1/1/2018 1:02,1169,314,164,Franklin St & Lake St,174,Canal St & Madison St,Subscriber,Male,1998
    - 8 17536709,1/1/2018 1:00,1/1/2018 1:13,6351,794,182,Wells St & Elm St,142,McClurg Ct & Erie St,Subscriber,Male,1990
    -9 17536710,1/1/2018 1:07,1/1/2018 1:31,1920,"1,481.00",99,Lake Shore Dr & Ohio St,99,Lake Shore Dr & Ohio St,Customer,,
    - 10 17536711,1/1/2018 1:07,1/6/2018 10:04,4783,"464,168.00",99,Lake Shore Dr & Ohio St,99,Lake Shore Dr & Ohio St,Customer,,
    - 11 17536712,1/1/2018 1:08,1/1/2018 1:31,3881,"1,361.00",99,Lake Shore Dr & Ohio St,99,Lake Shore Dr & Ohio St,Customer,,
    - 12 17536713,1/1/2018 1:09,1/1/2018 1:13,3838,212,13,Wilton Ave & Diversey Pkwy,220,Clark St & Drummond Pl,Subscriber,Male,1992
    - 13 17536714,1/1/2018 1:12,1/1/2018 1:19,6160,448,296,Broadway & Belmont Ave,304,Broadway & Waveland Ave,Subscriber,Female,1985
    - 14 17536715,1/1/2018 1:15,1/1/2018 1:21,6330,346,85,Michigan Ave & Oak St,106,State St & Pearson St,Subscriber,Female,1993
    - 15 17536718,1/1/2018 1:25,1/1/2018 1:36,6099,677,462,Winchester (Ravenswood) Ave & Balmoral Ave,238,Wolcott (Ravenswood) Ave & Montrose Ave (*),Subscriber,Male,1979
    - 16 17536719,1/1/2018 1:36,1/1/2018 1:40,966,219,118,Sedgwick St & North Ave,291,Wells St & Evergreen Ave,Subscriber,Male,1993
    - 17 17536720,1/1/2018 1:40,1/1/2018 1:45,520,320,165,Clark St & Grace St,256,Broadway & Sheridan Rd,Subscriber,Male,1994
   - 18 17536721,1/1/2018 1:44,1/1/2018 1:52,6050,498,198,Green St & Madison St,89,Financial Pl & Congress Pkwy (Temp),Subscriber,Male,1981
    - 19 17536722,1/1/2018 1:48,1/1/2018 1:52,586,272,69,Damen Ave & Pierce Ave,213,Leavitt St & North Ave,Subscriber,Female,1986
    - 20 17536724,1/1/2018 1:49,1/1/2018 1:52,5765,172,69,Damen Ave & Pierce Ave,213,Leavitt St & North Ave,Subscriber,Male,1985
    
        - Mapper output/reducer input: example of an intermediate key, value pair output by your mapper:
        - Damen Ave & Pierce Ave,323
        - Winthrop Ave & Lawrence Ave,377
        - Rush St & Hubbard St,747
        - Blue Island Ave & 18th St,183
        - Broadway & Waveland Ave,266
        -  Franklin St & Lake St,314
        - Wells St & Elm St,794
        - Wilton Ave & Diversey Pkwy,212
        - Broadway & Belmont Ave,448
        - Michigan Ave & Oak St,346
        - Winchester (Ravenswood) Ave & Balmoral Ave,677
        - Sedgwick St & North Ave,219
        - Clark St & Grace St,320
        - Green St & Madison St,498
        - Damen Ave & Pierce Ave,272
        - Damen Ave & Pierce Ave,172  


    - Reducer output
    
        - Blue Island Ave & 18th St	183.0
        - Broadway & Belmont Ave	448.0
        - Broadway & Waveland Ave	266.0
        - Clark St & Grace St	320.0
        - Damen Ave & Pierce Ave	767.0
        - Franklin St & Lake St	314.0
        - Green St & Madison St	498.0
        - Michigan Ave & Oak St	346.0
        - Rush St & Hubbard St	747.0
        - Sedgwick St & North Ave	219.0
        - Wells St & Elm St	794.0
        - Wilton Ave & Diversey Pkwy	212.0
        - Winchester (Ravenswood) Ave & Balmoral Ave	677.0
        - Winthrop Ave & Lawrence Ave	377.0
        

![bar chart](https://github.com/MRaghavendar/Divvy-s-Bikes/blob/master/images/avgrent.jpg)


  - Karthik Muthayala
  - Mapper input: 20  lines of data that mapper will read:
      - 1 17536702,1/1/2018 0:12,1/1/2018 0:17,3304,323,69,Damen Ave & Pierce Ave,159,Claremont Ave & Hirsch St,Subscriber,Male,1988
      - 2 17536703,1/1/2018 0:41,1/1/2018 0:47,5367,377,253,Winthrop Ave & Lawrence Ave,325,Clark St & Winnemac Ave (Temp),Subscriber,Male,1984
    - 3 17536704,1/1/2018 0:44,1/1/2018 1:33,4599,"2,904.00",98,LaSalle St & Washington St,509,Troy St & North Ave,Subscriber,Male,1989
    - 4 17536705,1/1/2018 0:53,1/1/2018 1:05,2302,747,125,Rush St & Hubbard St,364,Larrabee St & Oak St,Subscriber,Male,1983
    - 5 17536706,1/1/2018 0:53,1/1/2018 0:56,3696,183,129,Blue Island Ave & 18th St,205,Paulina St & 18th St,Subscriber,Male,1989
    - 6 17536707,1/1/2018 0:56,1/1/2018 1:00,6298,266,304,Broadway & Waveland Ave,299,Halsted St & Roscoe St,Subscriber,Female,1994
    - 7 17536708,1/1/2018 0:57,1/1/2018 1:02,1169,314,164,Franklin St & Lake St,174,Canal St & Madison St,Subscriber,Male,1998
    - 8 17536709,1/1/2018 1:00,1/1/2018 1:13,6351,794,182,Wells St & Elm St,142,McClurg Ct & Erie St,Subscriber,Male,1990
    -9 17536710,1/1/2018 1:07,1/1/2018 1:31,1920,"1,481.00",99,Lake Shore Dr & Ohio St,99,Lake Shore Dr & Ohio St,Customer,,
    - 10 17536711,1/1/2018 1:07,1/6/2018 10:04,4783,"464,168.00",99,Lake Shore Dr & Ohio St,99,Lake Shore Dr & Ohio St,Customer,,
    - 11 17536712,1/1/2018 1:08,1/1/2018 1:31,3881,"1,361.00",99,Lake Shore Dr & Ohio St,99,Lake Shore Dr & Ohio St,Customer,,
    - 12 17536713,1/1/2018 1:09,1/1/2018 1:13,3838,212,13,Wilton Ave & Diversey Pkwy,220,Clark St & Drummond Pl,Subscriber,Male,1992
    - 13 17536714,1/1/2018 1:12,1/1/2018 1:19,6160,448,296,Broadway & Belmont Ave,304,Broadway & Waveland Ave,Subscriber,Female,1985
    - 14 17536715,1/1/2018 1:15,1/1/2018 1:21,6330,346,85,Michigan Ave & Oak St,106,State St & Pearson St,Subscriber,Female,1993
    - 15 17536718,1/1/2018 1:25,1/1/2018 1:36,6099,677,462,Winchester (Ravenswood) Ave & Balmoral Ave,238,Wolcott (Ravenswood) Ave & Montrose Ave (*),Subscriber,Male,1979
    - 16 17536719,1/1/2018 1:36,1/1/2018 1:40,966,219,118,Sedgwick St & North Ave,291,Wells St & Evergreen Ave,Subscriber,Male,1993
    - 17 17536720,1/1/2018 1:40,1/1/2018 1:45,520,320,165,Clark St & Grace St,256,Broadway & Sheridan Rd,Subscriber,Male,1994
   - 18 17536721,1/1/2018 1:44,1/1/2018 1:52,6050,498,198,Green St & Madison St,89,Financial Pl & Congress Pkwy (Temp),Subscriber,Male,1981
    - 19 17536722,1/1/2018 1:48,1/1/2018 1:52,586,272,69,Damen Ave & Pierce Ave,213,Leavitt St & North Ave,Subscriber,Female,1986
    - 20 17536724,1/1/2018 1:49,1/1/2018 1:52,5765,172,69,Damen Ave & Pierce Ave,213,Leavitt St & North Ave,Subscriber,Male,1985
    
    - Mapper output/reducer input: example of an intermediate key, value pair output by your mapper:
        - Damen Ave & Pierce Ave,323
        - Winthrop Ave & Lawrence Ave,377
        - Rush St & Hubbard St,747
        - Blue Island Ave & 18th St,183
        - Broadway & Waveland Ave,266
        -  Franklin St & Lake St,314
        - Wells St & Elm St,794
        - Wilton Ave & Diversey Pkwy,212
        - Broadway & Belmont Ave,448
        - Michigan Ave & Oak St,346
        - Winchester (Ravenswood) Ave & Balmoral Ave,677
        - Sedgwick St & North Ave,219
        - Clark St & Grace St,320
        - Green St & Madison St,498
        - Damen Ave & Pierce Ave,272
        - Damen Ave & Pierce Ave,172  
  
     - Reducer output


	- Blue Island Ave & 18th St	1	183.0	183.0
	- Broadway & Belmont Ave	1	448.0	448.0
	- Broadway & Waveland Ave	1	266.0	266.0
	- Clark St & Grace St	1	320.0	320.0
	- Damen Ave & Pierce Ave	3	767.0	255.666666667
	- Franklin St & Lake St	1	314.0	314.0
	- Green St & Madison St	1	498.0	498.0
	- Michigan Ave & Oak St	1	346.0	346.0
	- Rush St & Hubbard St	1	747.0	747.0
	- Sedgwick St & North Ave	1	219.0	219.0
	- Wells St & Elm St	1	794.0	794.0
	- Wilton Ave & Diversey Pkwy	1	212.0	212.0
	- Winchester (Ravenswood) Ave & Balmoral Ave	1	677.0	677.0
	- Winthrop Ave & Lawrence Ave	1	377.0	677.0

![bar chart](https://github.com/MRaghavendar/Divvy-s-Bikes/blob/master/images/average.jpg)
   



## Big Data Solutions
