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
1. For each user type whats the maximum trip duration -  Karthik
2. For each bike id, find the average of trip duration - Raghavendar
3. For a given from Station I will find the total trip  duration  rented at that station - Ganesh
## Big Data Solutions

 - Ganesh Siripuram

Mapper Input:


| 17536702 | 1/1/2018 0:12 | 1/1/2018 0:17 | 3304 | 323 | 69 | Damen Ave & Pierce Ave | 159 | Claremont Ave & Hirsch St | Subscriber | Male | 1988 |
|----------|---------------|---------------|------|-----|----|------------------------|-----|---------------------------|------------|------|------|

 Mapper Output:

| Start station | Trip duration |
|----------|----------|
|  Damen Ave & Pierce Ave    | 323     |

 Reducer Output:

| Start station | Total Trip Duration |
|----------|----------|
| Damen Ave & Pierce Ave | 323 |

chart: Bar Braph.
  

![bar chart](https://github.com/MRaghavendar/Divvy-s-Bikes/blob/master/images/avgrent.jpg)


Raghavendar Reddy Maddelavedu

Mapper Input:

| 17536702 | 1/1/2018 0:12 | 1/1/2018 0:17 | 3304 | 323 | 69 | Damen Ave & Pierce Ave | 159 | Claremont Ave & Hirsch St | Subscriber | Male | 1988 |
|----------|---------------|---------------|------|-----|----|------------------------|-----|---------------------------|------------|------|------|

Mapper Output:

| Bike I'd | Trip duration |
|----------|----------|
| 3304   | 323     |

Reducer Output:

| Bike I'd | Avg Trip Duration |
|----------|----------|
| 3304   | 389.0      |

chart: Bar Braph.

Karthik Reddy Muthyala

Problem statement:
Mapper Input:
| 7/1/2018 0:06 | 93 | 386 | 153 | Southport Ave & Wellington Ave | 250 | Ashland Ave & Wellington Ave | Subscriber | Male | 1986 |   |   |
|---------------|----|-----|-----|--------------------------------|-----|------------------------------|------------|------|------|---|---|

Mapper Output:
|Usertype    | Trip Duration |
|------------|---------------|
| Subscriber | 386           |


Reducer Output:
|Usertype    | Trip Duration |
|------------|---------------|
| Subscriber | 386           |

<<<<<<< HEAD
Chart: Pie Chart.

![Pie chart](https://github.com/MRaghavendar/Divvy-s-Bikes/blob/master/images/tripimage.jpg)

=======
Chart: Bar Chart.
>>>>>>> ed0a453307fd2c52367f8002047bd9643d44063d



## Big Data Solutions
