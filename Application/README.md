# Text Reader for Domain Group 

with this application you can read any text_file.txt, and receive a report. also you can create a file to limit the application to read some special words. 


## Files
 
limited_words.txt:   
in this file you should add all the words that you want to skip from reading.   
report.txt:
when you run your application you can find all allowed words and the count of them in this file. 

## How to run
for running the application
1- go to the root of the folder, where main.py and other files are there. 
then you should run 
```bash
python main.py
```
2- you need to insert the path of the text file to application. 
3- in front of the this question you should insert the minimum number of count that you want to see in the report for each word: 
```bash
Insert The minimum count number:
```
if everything goes right, you will see this message: 

```bash
INFO:root:report.txt file has been created.
```
