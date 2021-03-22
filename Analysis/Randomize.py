import csv
import random
import numpy as np 
import pandas as pd
from itertools import repeat
df = pd.read_csv(r"C:\Users\wangs\OneDrive - The University of Western Ontario\Desktop\Project BL\Guess The Sound\Analysis\To be randomized.csv")
#def sound_randomize(df):
seeds = [0]*140 # Initial placeholders
typ = [0]*128 # Seeds for word types
corr = [0]*128 # Seeds for correct answers
# lure_name = df['lure_name']
# old_name = df['old_name']
both = df['All sounds']
lure_ind_list = []
both_ind_list = []

# lures = list(range(1, 17))
# for i in lures:
#     initial_ind = random.randint(0, 90)
#     ind_list = list(range(initial_ind,initial_ind+45, 15))
#     lure_ind_list.append(ind_list)

for i in range(64):
    initial_ind = random.randint(0, 110)
    ind_list = list(range(initial_ind,initial_ind+40, 20))
    both_ind_list.append(ind_list)

# for i in range(16):
#     item = lure_name[i]
#     for ind in lure_ind_list[i]:
#         while seeds[ind] != 0:
#             ind += 1            
#         seeds[ind] = item

for i in range(64):
    item = both[i]
    for ind in both_ind_list[i]:
        while seeds[ind] != 0:
            ind += 1            
        seeds.insert(ind, item)
        #seeds[ind] = item

with open("randomized sounds.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(seeds)
    print("done")
