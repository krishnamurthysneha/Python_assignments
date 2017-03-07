
# ReadMe

# Question 1: Enron data


```python
>Have given a relative path so that you could put your absolute path based on where your folders are residing
    relative_path='/Users/Sneha/Downloads/maildir' 
    
>Using a definition: def check_file_or_dir to check if its a file or folder 
    If its a folder we will loop through to check if we encouter a folder again if not then its a file,
    then the file is read
after the file is read, three analysis are performed
Analysis
1.) To find the number of mails which have been sent and recieved during the month of Dec 2001.
-For this count_mails has been globally declared so that total mails in that particular month can be counted.
-Using email parser we can parse through the emails and using header.parser we can find the head as Date and value as Dec 2011
2.) To find the number of mails sent and recieved by the people in enron dataset
-Two lists are there to append the sent and recieved mails
-Based on this we write the data to the csv file where the last name of the person, his sent and recieved mails will be the columns
-"output_enron_file.csv"
3.)To find the URl links in the body of the letter
-Regex function gives the URL in the email body
-This will be put into a list and the redudant URLs are removed using set function
-All the URLs will be written to a text file which makes us get the used distinct URLs easily
-"/Users/Sneha/URL.txt"

```

# Question 2: NYT API


```python
> NYT is the New York times API that provides data from its articles since 1851. Here data has been collected from Archieve
and Most Popular API methods. 
Analysis 1:
> Using Archive API articles in January month from the year 2005-2016
>Finding the tompost 50 high frequency words for every year
Analysis 2:
>Proving Zipf's law for data in 2016
Analysis 3:
>Finding the topmost 5 countries which are in the news in travel and world sections.
```
