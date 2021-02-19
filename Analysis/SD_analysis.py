import csv
import pandas as pd 
import numpy as np 
import scipy.stats as st

# Import datafiles (Enter data file ID here)
filelist = [1, 2]
#df = pd.read_csv(r"C:\Users\wangs\OneDrive - The University of Western Ontario\Desktop\Project BL\Word MST\Analysis\8_wmst.csv")
def get_accuracy(df):
    # Load data as lists
    corr = [] # Whether the answer was correct (1) or not (0)
    wordtype = [] # Whether the word was old, lure, or new
    resp = [] # Participant's responses (0, 1)
    r = df['key_resp.corr']
    for i in r:
        if pd.isnull(i) == False:
            corr.append(i)
    t = df['Type']
    for i in t:
        if pd.isnull(i) == False:
            wordtype.append(i)
    wordtype = wordtype[5:] # Remove the first 5 because they are for the practice trials
    x = df['key_resp.keys']
    for i in x:
        if pd.isnull(i) == False:
            resp.append(i)

    # What did they respond to Old items?
    old_old = 0 # Old as OLD
    new_old = 0 # Old as NEW
    for i in range(len(wordtype)):
        if wordtype[i] == "OLD":
            old_old += corr[i]
            if corr[i] == 0:
                new_old += 1
    old_old = old_old/40
    z_old_old = st.norm.ppf(old_old)
    new_old = new_old/40
    z_new_old = st.norm.ppf(new_old)

    # What did they respond to New items?
    new_new = 0 # New as NEW
    old_new = 0 # New as OLD
    for i in range(len(wordtype)):
        if wordtype[i] == "NEW":
            new_new += corr[i]
            if corr[i] == 0:
                old_new += 1
    new_new = new_new/64
    z_new_new = st.norm.ppf(new_new)
    old_new = old_new/64
    z_old_new = st.norm.ppf(old_new)

    # What did they respond to Lure (new) items?
    new_sim = 0 # Lure as NEW
    old_sim = 0 # Lure as OLD
    for i in range(len(wordtype)):
        if wordtype[i] == "SIMILAR":
            if corr[i] == 1: # If they responded NEW to lures
                new_sim += 1
            else: # If they responded OLD to lures
                old_sim += 1
    new_sim = new_sim/24
    z_new_sim = st.norm.ppf(new_sim)
    old_sim = old_sim/24
    z_old_sim = st.norm.ppf(old_sim)

    with open ('Sound_MST_analysis.csv', 'a', newline="") as file:
            writer = csv.writer(file)
            writer.writerow(['"Old"|Old', '"Old"|New', '"New"|Lure', '"Old"|Lure', '"New"|New', '"Old"|Old'])
            writer.writerow([old_old, old_new, new_sim, old_sim, new_new, new_old])
            #writer.writerow([z_old_old, z_old_new, z_new_sim, z_old_sim, z_new_new, z_new_old])


for i in filelist:
    filename = str(i)+"_MST128.csv"
    df = pd.read_csv(filename)
    get_accuracy(df)

    