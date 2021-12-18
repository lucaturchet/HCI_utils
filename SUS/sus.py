'''
System Usability Scale calculator
Author: Luca Turchet @ University of Trento
Date: 17/12/2021

This program computes the mean and 95% confidence interval of the System Usability Scale,
as well as plots the mean and standard error/standard deviation of the responses to each question.
The SUS for each participants is also written in a .csv output file 

Usage: python sus.py 
You need to amend the variable "infile" to asign the path to your filename.csv containg the data

Note: you can choose to plot the standard deviation or the error bars in the plot, amend the code at your convenience

'''

import csv
import sys
import numpy as np
import scipy.stats as st
import matplotlib.pyplot as plt
from textwrap import wrap


infile = 'sus-input-data.csv'
outfile = 'sus-results.csv'


sus = [] #Array of SUS results for each participant 
Q1 = []
Q2 = []
Q3 = []
Q4 = []
Q5 = []
Q6 = []
Q7 = []
Q8 = []
Q9 = []
Q10 = []


with open(infile, mode='r') as csv_file:
    csv_reader = csv.DictReader(csv_file, delimiter = '\t')

    for row in csv_reader:

        Q1.append(int(row['Q1']))
        Q2.append(int(row['Q2']))
        Q3.append(int(row['Q3']))
        Q4.append(int(row['Q4']))
        Q5.append(int(row['Q5']))
        Q6.append(int(row['Q6']))
        Q7.append(int(row['Q7']))
        Q8.append(int(row['Q8']))
        Q9.append(int(row['Q9']))
        Q10.append(int(row['Q10']))

        odd = (int(row['Q1']) + int(row['Q3']) + int(row['Q5']) + int(row['Q7']) + int(row['Q9'])) - 5
        even = 25 - (int(row['Q2']) + int(row['Q4']) + int(row['Q6']) + int(row['Q8']) + int(row['Q10']))
        total = (odd + even) * 2.5
        sus.append(total)
        

print("\n----------------------------------------------------------")
print(f"\nSUS mean: {np.mean(sus)}")
#print(f"Median: {np.median(sus)}")
#print(f"Std: {np.std(sus)}")
print(f"\n95% Confidence interval: {st.t.interval(0.95, len(sus)-1, loc=np.mean(sus), scale=st.sem(sus))}")
print("\n----------------------------------------------------------")



#Write SUS results for each participant in a csv file
with open(outfile, mode='w') as csv_writer_file:
    csv_writer = csv.writer(csv_writer_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

    csv_writer.writerow(['Total'])

    for i in sus:
        csv_writer.writerow([i])





#Breakdown plot
fig_sus_results_breakdown, ax = plt.subplots(figsize=(11, 5))

results = [np.mean(Q1), np.mean(Q2), np.mean(Q3), np.mean(Q4), np.mean(Q5), np.mean(Q6), np.mean(Q7), np.mean(Q8), np.mean(Q9), np.mean(Q10)] 
ind = np.arange(len(results))
#err = [np.std(Q1), np.std(Q2), np.std(Q3), np.std(Q4), np.std(Q5), np.std(Q6), np.std(Q7), np.std(Q8), np.std(Q9), np.std(Q10)] #standard deviation
err = [st.sem(Q1), st.sem(Q2), st.sem(Q3), st.sem(Q4), st.sem(Q5), st.sem(Q6), st.sem(Q7), st.sem(Q8), st.sem(Q9), st.sem(Q10)] #standard error


cmap = plt.get_cmap('viridis', 10)
ax.bar(ind, results, width=0.7, yerr=err,  color=cmap.colors, ecolor='black', capsize=9)

sus_xlabels = ['like to use system frequently', 'system unnecessarily complex', 'system easy to use', 'need technical support', 'functions well integrated', 'too much inconsistency', 'learn to use very quickly', 'inconvenient to use', 'confident using the system', 'need to learn a lot before use']
sus_xlabels = [ '\n'.join(wrap(l, 14)) for l in sus_xlabels ]
#sus_xlabels = [ label.replace(' ', '\n') for label in sus_xlabels]
ax.set_xticks([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) 
ax.set_xticklabels(sus_xlabels, fontsize=12, rotation=45)
ax.set_ylim([1, 5])
ax.set_yticks([1, 2, 3, 4, 5]) 
sus_ylabels = ['Strongly disagree', '2', 'Neutral', '4', 'Strongly agree']
sus_ylabels = [ '\n'.join(wrap(l, 10)) for l in sus_ylabels ]
ax.set_yticklabels(sus_ylabels)
#ax.set_yticklabels(['0', 'Strongly disagree', '2', 'Neutral', '4', 'Strongly agree'])
ax.set_title("SUS questions", fontsize=15, fontweight="bold")
plt.tight_layout()
fig_sus_results_breakdown.savefig("sus_results_breakdown.png", dpi=300, bbox_inches='tight')
plt.show()

