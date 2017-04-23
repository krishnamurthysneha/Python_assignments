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
