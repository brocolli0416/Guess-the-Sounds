import csv
import numpy as np 
import pandas as pd 
### For calculating the types of response given to each sound file
### The number of "OLD" response to the Lure items is used to measure similarity 
### (The more OLD response given, the greater the similarity)

filelist = [9, 10, 11]


def get_similarity(df, cat):
    cor_orig = df['Correct2']
    st_orig = df['SoundFile']
    rp_orig = df['MSTResp.keys']
    correct = []
    soundtype = []
    response = []

    for i in range(5, len(cor_orig)):
        if cor_orig[i] == cat:
            soundtype.append(st_orig[i])
            response.append(rp_orig[i])

    stacked = np.column_stack((soundtype, response))
    stacked = sorted(stacked, key=lambda x : x[0])
    new_resp = []
    new_sound = []
    for i in stacked:
        new_resp.append(i[1])
        new_sound.append(i[0])
    with open('Similarity_analysis.csv', 'a', newline="") as file:
        writer = csv.writer(file)
        writer.writerow(new_sound)
        writer.writerow(new_resp)

for f in filelist:
    filename = str(f)+'_MST128_3AFCh.csv'
    df = pd.read_csv(filename)
    get_similarity(df, 2) # Enter the number for the type of sound you want to analyze. (OLD = 1, LURE = 2, FOIL = 3)


