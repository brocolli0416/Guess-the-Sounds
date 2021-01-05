import pandas as pd 
import numpy as np
import csv
df = pd.read_csv(r"C:\Users\wangs\OneDrive - The University of Western Ontario\Desktop\Project BL\Guess The Sound\Analysis\mayte_GuessTheSound_2021-01-04_21h16.16.532.csv")
output = pd.read_csv(r"C:\Users\wangs\OneDrive - The University of Western Ontario\Desktop\Project BL\Alien language pilot\Analysis\Sound_data.csv")
types = output.columns.tolist()
names = []
new = []
soundname = list(df['SoundFiles'])
#print(soundname)
response = list(df['ResponseBox.text'])
for i in types:
    if i in soundname:
        for x in range(len(soundname)):
            if soundname[x] == i:
                names.append(response[x])
    else:
        names.append("NA")
for i in soundname:
    if i not in types:
        new.append(i)

    
        
with open ('Sound_data.csv', 'a') as file:
        writer = csv.writer(file)
        writer.writerow(names)
        writer.writerow(new)