
# READ ME

# Question 1: Enron data analysis


```python
Enron Corporation was an American energy company whose share was around $90 in December 2001 and it had a drastic 
downfall to almost $0 in January 2002 when they declared bankruptcy.  The major reasons of the downfall was its complex 
business model and mis-interpretation of earnings and account limitations.  The current data provided for analysis is the 
set of email of the employees of the Enron Corporation.

```


```python
##Process for analysis:
1) Have given a relative path so that you could put your absolute path based on where your folders are residing
    relative_path='/Users/Sneha/Downloads/maildir' 
    
2) Using a definition: def check_file_or_dir to check if its a file or folder 
    This function performs a check whether the given path is a folder or a file. If the path is a file/email then it is read to perform analysis, else the function loops through the folders recursively to find files. 
    Once a file is read the following three analysis are performed


```

# Analysis 1:


```python

1.) To find the number of mails which have been sent and recieved during the month of Dec 2001.

#Overview:
-For this count_mails has been globally declared so that total mails in that particular month can be counted.
-Using email parser we can parse through the emails and using header.parser we can find the head as Date and 
 value as Dec 2011
    
###Steps:
> The csv file is read from the relative path and when the first directory is entered the last name of all the employees is obtained by splitting the folder name. These names are used to uniquely identify the from and to mails.

> The function is called with case1 which implies for analysis 1. In this analysis the data is passed to the object of email-parser class where the headers and the body of the email is separated.

> In the "Date" header, the Dec 2001 is found and counted. Using this analysis we can determine if the downfall was due to the communication in the email chain of the employees.
```

# Analysis 2:


```python
2.) To find the number of mails sent and recieved by the people in enron dataset

Overview:
-Two lists are there to append the sent and recieved mails 
-Based on this we write the data to the csv file where the last name of the person, his sent and recieved mails will be the columns

###Steps:
> The csv file is read from the relative path and as in the earlier case the case2 is called in the function.

> The heaaders are checked for "From" and "To" and the names are compared  against the last names that were obtained earlier by splitting the folder name.

> 2 Dictionaries are maintained in which the key value is the last name and the value is the number of emails sent or received from the employee.

> This analysis will help us to conclude the employees who were involved in most exchange of emails and we can infer the employee who would be the probable suspect for the downfall of the company.

> The output is written to a csv file with name -"output_enron_file.csv" which contains the last name, numbers of mails sent and received as the columns.
```

# Analysis 3:


```python
3.)To find the URl links in the body of the letter

Overview:
-Regex function gives the URL in the email body
-This will be put into a list and the redudant URLs are removed using set function

###Steps:
> The csv file is read from the relative path and the case3 is called in the function.

> Regular expression module is used to find the strings that start with "http" or "https".

> All the links are stored in a list and later appended to another list which has all the URL's from every email.

> All the URLs will be written to a text file which makes us get the distinct URLs easily.

> These links help us to analyze the web data that has been accessed which gives us an idea of the possible reasons of the downfall.

> The output is written to the file called as "/Users/Sneha/URL.txt".
```

# Question 2: NYT API


```python
The New York Times is a large source of news and Information.  The NYT developer network has made available huge amount of data which can be used for data analysis.  Additionally the API tools online help us verify the data that has been 
obtained and stored. The data is divided into multiple API's which help in analyzing data pertained to certain section of 
the news.  One striking feature of NYT API's is that it provides data from its articles since 1851. Here data has been 
collected from Archieve	and Most Popular API methods. 
```


```python
##Process for collecting and storing data:

1) The major step in this question is to collect and store the appropriate data necessary for the analysis from the API's.
2) Keys are obtained for the different API's.
3) Using the keys write a program to obtain data. As the data set is huge limit the data using any specific keys such as sports section or classifeds section and so on.
4) Store the data in the local disk in .json files.
5) Loop through the files to perform necessary analysis.

```

# Analysis 1:


```python
1.)Overview:
-Using Archive API articles in January month from the year 2005-2016
-Finding the tompost 50 high frequency words for every year

Steps:
> The sports data for every year is stored in folders according to the year and in each folder data is stored in 12 different
text files corresponding to 12 months in a year.

> Punctuations and Numbers are removed from the data.

> Find out the 50 topmost words in each year with the help of Frequency Dist module.

> This analysis aids in understanding the change of usage of words over a period of 10 years.
```

# Analysis 2:


```python
2.)Overview:
-Proving Zipf's law for data in 2016

Steps:
> Zipf's law states that given some corpus of natural language utterances, the frequency of any word is inversely proportional 
to its rank in the frequency table.

> The aim of this analysis is to prove Zipf's law in data from 2016 year.

> The frequency distribution of words is calculated using the Frequency Dist function and the data is sorted based on the value.

> Graph is plotted using matplotlib module and we conclude that Zipf's law is proved for the News data in year 2016.

```

# Analysis 3:


```python
3.)Overview:
-Finding the topmost 5 countries which are in the news in travel and world sections.

Steps:
> The data is collected from the Most Popular API for various sections such as ARTS, BOOKS, HEALTH etc.

> Separate folders are created for each section and data is stored within a text file.

> We perform analysis on the Travel and World data set to find the most happening cities in the world.

> For reference a list of city names in obtained from web and stored in a file -> 'countries.txt'

> Counting every city name in the file and store it in a dcitionary where the key value is city and the value is the count.

> The dictionary is sorted in descending order and the topmost 5 country names in news is found out.

```
