
# READ ME


# INFO 7374 – DATA ANALYSIS USING PYTHON SEC 01 – SPRING 2017


# INTRODUCTION: DATA FROM BUREAU OF TRANSPORTATION STATISTICS


```python
The data set been collected from bureau of transportation statistics, which is a leading source of timely accurate and reliable information on the U.S. transportation systems used for moving people and goods, and on their impacts on the economy, society and the environment. 
            The Bureau’s National Transportation Library is the permanent, publicly accessible home for research publications from throughout the transportation community, the gateway to all DOT data, and the help line for the Congress, researchers, and the public for information about transportation.
STORING THE DATA:
•The data was obtained year wise which contained details about every incoming and outgoing flight in all the airports of USA.
•The csv file for every year contained around 70 million to 1 billion records on an average.
•Subset of data from each file was collected by performing random samples using the following command.

   Subsample -n [no of samples required] [name of original file] > [output file] 

•All the csv files were combined in to one csv file to perform the analysis.
•The above random sampling aided in easy analysis as it drastically reduced the size of the dataset from order of Gb’s to order of Mb’s.
•Along with this we used two more datasets one of which contained the financial structure of the Carriers and the other file containing the details of the airport, such as the city name, latitude, longitude etc.…
```

# ANALYSIS PERFORMED:

# Analysis 1:

-This analysis was performed to determine the number of flights delayed for every year.
-To accomplish this task we had to split the departure time and the scheduled departure time into hours and minutes and find the difference among these two.


Steps Performed:
*The data is read from csv file to Pandas data frame.
*The departure time is split into hours and minutes based on string split.
*The delay is calculated based on the hour difference between scheduled and actual departure.
*Groupby is performed on year and the number of flights delayed.
*Data is sorted to find in which year the maximum number of flights were delayed.


Challenges faced:
-Splitting the time into hours and minutes.

<img width="449" alt="4" src="https://cloud.githubusercontent.com/assets/25678970/25310301/85d8ad5c-27af-11e7-8055-fb61467ba65d.png">

![plot_analysis_1](https://cloud.githubusercontent.com/assets/25678970/25310271/f0190ea6-27ae-11e7-88ae-d60535237cb8.png)

# Analysis 2:

-This analysis was performed to determine the apt month for travel between a pair of origin and destination.
-This will give us a probability of cancellation of flight for that specific month for the pair of origin and destination.

Steps Performed:
*The data is read from csv file to Pandas data frame.
*The sum of all the delays such as the career delay, weather delay, NAS Delay, security delay and late aircraft delay.
*The data is sorted in descending order in groups for every pair of origin and destination.

Challenges faced:
-Sorting the data group wise for each pair.

img width="712" alt="1" src="https://cloud.githubusercontent.com/assets/25678970/25310115/bba35450-27aa-11e7-9880-f962592a78b5.png">


![plot_analysis_2](https://cloud.githubusercontent.com/assets/25678970/25310124/f50254a8-27aa-11e7-8ca5-2ccd34bed3c2.png)


# Analysis 3:

-This analysis was performed to determine the top 5 busiest airports.
-This will give us a clear idea about the busiest airport during the time span of 1987-2008.

Steps Performed:
*The data is read from csv file to Pandas data frame.
*Groupby is performed on origin and destination separately and the counts have been noted.
*Both the counts are added and the current data frame is merged with the data frame which contains the airport details.

Challenges faced:
-Performing the join based on the key column.

<img width="710" alt="2" src="https://cloud.githubusercontent.com/assets/25678970/25310136/50283eba-27ab-11e7-84d4-d0cf31914c24.png">

![plot_analysis_3](https://cloud.githubusercontent.com/assets/25678970/25310140/5cfdea7c-27ab-11e7-91d5-5b78b5b9aef9.png)


# Analysis 4:

-This analysis was performed to analyze the quarterly profits of the carrier for every year.
-This will help us to understand the relation between profits gained and services provided to the customer.

Steps Performed:
*The data is read from csv file to Pandas data frame.
*All the NaN values in assets, liabilities and credits columns are filled with 0,0.
*The groupby is performed on origin, destination and carrier.
*I added all the columns related to assets and liabilities and performed percentage profit calculations.

<img width="742" alt="3" src="https://cloud.githubusercontent.com/assets/25678970/25310159/36d8843c-27ac-11e7-9817-d5940b63fa64.png">

![plot_analysis_4](https://cloud.githubusercontent.com/assets/25678970/25310152/f3cb2ce4-27ab-11e7-8494-86c9825b9317.png)

# Analysis 5:

-This analysis was performed to determine the best carrier based on cancellation criteria.
-the dataset has information about the reason of cancellation and particularly in this case we have considered the cancellation due to the carrier.

Steps Performed:
*The data is read from csv file to Pandas data frame.
*Groupby is performed on unique carrier and the count is calculated for the same.
*Another groupby is performed based on unique carrier and cancelled columns and the count is calculated again.
*Percentage of cancellation is calculated by the formula.

      ([number of flights cancelled] / [total number of flights]) * 100
 

    
![plot_analysis_5](https://cloud.githubusercontent.com/assets/25678970/25310236/fd1a9c4c-27ad-11e7-8ec7-ace1bea9ba28.png)


```python

```
