import csv
import json
import pandas as pd

#Intialize the column names in csv
fieldnames=["survived","pclass","name","sex","age","sibsp","parch","ticket","fare","cabin","embarked"]

#open file in read mode
f=open('titanic.csv', 'r')

#read csv file 
csv_reader=csv.DictReader(f, fieldnames)

#create json from csv_reader
data = json.dumps([r for r in csv_reader])
jdata=json.loads(data)[1:]

#convert json data to pandas dataframe
df = pd.DataFrame(jdata)

##match the top 5 records from JSON read and actual titanic dataset
#Read first 5 rows from titanic.csv file
print('------------------------Data from titanic.csv file----------------------------')
count=0
with open("titanic.csv") as f:
    reader = csv.reader(f)
    for row in reader:
        count=count+1
        print(" ".join(row))
        if(count>5):
            break
            
print('\n\n------------------------Data from json----------------------------')
#first 5 dataset read from json
df.head(5)

#Initialize the URL to be read from
url='http://vincentarelbundock.github.io/Rdatasets/datasets.html'

#Read the HTML table to create Pandas dataframe
htm= pd.read_html(url)

rd=htm[1][1:100]
#print(pd.DataFrame.to_json(rd, orient="records"))

# Load the first sheet of the JSON file into a data frame
df = pd.read_json('sample2.json', orient='columns')

# View the first ten rows
df.head(10)