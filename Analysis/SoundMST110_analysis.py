import pandas as pd 
import csv

### Load participant file ###
filelist = [15, 16, 17]

###############################
### Calculate accuracy rate ###
###############################
def get_accuracy(df):
    # Get data from file
    corr = [] # Correct (1) or incorrect (0)
    r = df['MSTResp.corr']
    for i in r:
        if pd.isnull(i) == False:
            corr.append(i)
    soundtype = [] # Sound type (old, lure, new)
    t = df['Correct2']
    for i in t:
        if pd.isnull(i) == False:
            soundtype.append(i)
    del soundtype[:5] # Remove the first 11 headphone checks and practice trials
    response = [] # Subject's response (OLD, SIMILAR, NEW)
    k = df['MSTResp.keys']
    for i in k:
        if pd.isnull(i) == False:
            response.append(i)

    # Count the number of each response type to each sound type
    old_o = 0
    sim_o = 0
    new_o = 0
    old_s = 0
    sim_s = 0
    new_s = 0
    old_n = 0
    sim_n = 0
    new_n = 0

    for i in range(len(soundtype)):
        if soundtype[i] == 1: # For Old sounds
            if response[i] == 1:
                old_o += 1
            elif response[i] == 2:
                sim_o += 1
            else:
                new_o += 1
        elif soundtype[i] == 2: # For Lure sounds
            if response[i] == 1:
                old_s += 1
            elif response[i] == 2:
                sim_s += 1
            else:
                new_s += 1
        else: # For New sounds
            if response[i] == 1:
                old_n += 1
            elif response[i] == 2:
                sim_n += 1
            else:
                new_n += 1
    # Calculate the average
    old_o = old_o/40
    sim_o = sim_o/40
    new_o = new_o/40
    old_s = old_s/24
    sim_s = sim_s/24
    new_s = new_s/24
    old_n = old_n/64
    sim_n = sim_n/64
    new_n = new_n/64

#############################
### Calculate LDI and REC ###
#############################
    LDI = sim_s - sim_n
    REC = old_o - old_n

    # Output to csv file
    with open('Sound_MST_analysis.csv', 'a', newline="") as file:
        writer = csv.writer(file)
        #writer.writerow(['"Old"|Old', '"Sim"|Old', '"New"|Old', '"Old"|Sim', '"Sim"|Sim', '"New"|Sim', '"Old"|New', '"Sim"|New', '"New"|New'])
        writer.writerow([old_o, sim_o, new_o, old_s, sim_s, new_s, old_n, sim_n, new_n, LDI, REC])

for i in filelist:
    filename = str(i)+'_MST128_3AFCh.csv'
    df = pd.read_csv(filename)
    get_accuracy(df)


        

