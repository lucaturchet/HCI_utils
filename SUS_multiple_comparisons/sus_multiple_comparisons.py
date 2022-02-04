'''
System Usability Scale calculator
Author: Luca Turchet @ University of Trento
Date: 17/12/2021

This program computes the mean and 95% confidence interval of the System Usability Scale,
as well as plots the mean and standard error/standard deviation of the responses to each question.


Usage: python sus_multiple_comparisons.py 
You need to amend the variable "infile" to asign the path to your filename.csv containg the data

Note: you can choose to plot the standard deviation or the error bars in the plot, amend the code at your convenience

'''

import csv
import sys
import numpy as np
import scipy.stats as st
import matplotlib.pyplot as plt
from textwrap import wrap


infile = 'sus_input_data_multiple_comparisons.csv'


#Here set the actual names of the conditions according to the csv file
condition1 = "FA"
condition2 = "FVR"

sus_condition1 = [] #Array of SUS results for each participant in condition 1
Q1_condition1 = []
Q2_condition1 = []
Q3_condition1 = []
Q4_condition1 = []
Q5_condition1 = []
Q6_condition1 = []
Q7_condition1 = []
Q8_condition1 = []
Q9_condition1 = []
Q10_condition1 = []

sus_condition2 = [] #Array of SUS results for each participant in condition 1
Q1_condition2 = []
Q2_condition2 = []
Q3_condition2 = []
Q4_condition2 = []
Q5_condition2 = []
Q6_condition2 = []
Q7_condition2 = []
Q8_condition2 = []
Q9_condition2 = []
Q10_condition2 = []


with open(infile, mode='r') as csv_file:
    csv_reader = csv.DictReader(csv_file, delimiter = ',')

    for row in csv_reader:

        q1 = int(row['Q1'])
        q2 = int(row['Q2'])
        q3 = int(row['Q3'])
        q4 = int(row['Q4'])
        q5 = int(row['Q5'])
        q6 = int(row['Q6'])
        q7 = int(row['Q7'])
        q8 = int(row['Q8'])
        q9 = int(row['Q9'])
        q10 = int(row['Q10'])
        

        if row['condition'] == condition1:

            Q1_condition1.append(q1)
            Q2_condition1.append(q2)
            Q3_condition1.append(q3)
            Q4_condition1.append(q4)
            Q5_condition1.append(q5)
            Q6_condition1.append(q6)
            Q7_condition1.append(q7)
            Q8_condition1.append(q8)
            Q9_condition1.append(q9)
            Q10_condition1.append(q10)

            odd = (q1 + q3 + q5 + q7 + q9) - 5
            even = 25 - (q2 + q4 + q6 + q8 + q10)
            total = (odd + even) * 2.5
            sus_condition1.append(total)
        

        if row['condition'] == condition2:

            Q1_condition2.append(q1)
            Q2_condition2.append(q2)
            Q3_condition2.append(q3)
            Q4_condition2.append(q4)
            Q5_condition2.append(q5)
            Q6_condition2.append(q6)
            Q7_condition2.append(q7)
            Q8_condition2.append(q8)
            Q9_condition2.append(q9)
            Q10_condition2.append(q10)

            odd = (q1 + q3 + q5 + q7 + q9) - 5
            even = 25 - (q2 + q4 + q6 + q8 + q10)
            total = (odd + even) * 2.5
            sus_condition2.append(total)






print("\n----------------------------------------------------------")
print(f"\nSUS {condition1} mean: {np.mean(sus_condition1)}")
#print(f"Median: {np.median(sus_condition1)}")
#print(f"Std: {np.std(sus_condition1)}")
print(f"\n95% Confidence interval: {st.t.interval(0.95, len(sus_condition1)-1, loc=np.mean(sus_condition1), scale=st.sem(sus_condition1))}")
print("\n----------------------------------------------------------")



print("\n----------------------------------------------------------")
print(f"\nSUS {condition2} mean: {np.mean(sus_condition2)}")
#print(f"Median: {np.median(sus_condition2)}")
#print(f"Std: {np.std(sus_condition2)}")
print(f"\n95% Confidence interval: {st.t.interval(0.95, len(sus_condition2)-1, loc=np.mean(sus_condition2), scale=st.sem(sus_condition2))}")
print("\n----------------------------------------------------------")




''' 
#Write SUS results for each participant in a csv file
with open(outfile, mode='w') as csv_writer_file:
    csv_writer = csv.writer(csv_writer_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

    csv_writer.writerow(['Total'])

    for i in sus:
        csv_writer.writerow([i])
'''




#Breakdown plot
fig_sus_results_breakdown, ax = plt.subplots(figsize=(13, 5))

results_condition1 = [np.mean(Q1_condition1), np.mean(Q2_condition1), np.mean(Q3_condition1), np.mean(Q4_condition1), np.mean(Q5_condition1), np.mean(Q6_condition1), np.mean(Q7_condition1), np.mean(Q8_condition1), np.mean(Q9_condition1), np.mean(Q10_condition1)] 
#err = [np.std(Q1), np.std(Q2), np.std(Q3), np.std(Q4), np.std(Q5), np.std(Q6), np.std(Q7), np.std(Q8), np.std(Q9), np.std(Q10)] #standard deviation
err_condition1 = [st.sem(Q1_condition1), st.sem(Q2_condition1), st.sem(Q3_condition1), st.sem(Q4_condition1), st.sem(Q5_condition1), st.sem(Q6_condition1), st.sem(Q7_condition1), st.sem(Q8_condition1), st.sem(Q9_condition1), st.sem(Q10_condition1)] #standard error


results_condition2 = [np.mean(Q1_condition2), np.mean(Q2_condition2), np.mean(Q3_condition2), np.mean(Q4_condition2), np.mean(Q5_condition2), np.mean(Q6_condition2), np.mean(Q7_condition2), np.mean(Q8_condition2), np.mean(Q9_condition2), np.mean(Q10_condition2)] 
#err = [np.std(Q1), np.std(Q2), np.std(Q3), np.std(Q4), np.std(Q5), np.std(Q6), np.std(Q7), np.std(Q8), np.std(Q9), np.std(Q10)] #standard deviation
err_condition2 = [st.sem(Q1_condition2), st.sem(Q2_condition2), st.sem(Q3_condition2), st.sem(Q4_condition2), st.sem(Q5_condition2), st.sem(Q6_condition2), st.sem(Q7_condition2), st.sem(Q8_condition2), st.sem(Q9_condition2), st.sem(Q10_condition2)] #standard error

ind = np.arange(len(results_condition1))
width = 0.3

ax.bar(ind - width/2, results_condition1, width, yerr=err_condition1,  color='#CD853F', ecolor='black', capsize=9, label=condition1)
ax.bar(ind + width/2, results_condition2, width, yerr=err_condition2,  color='silver', ecolor='black', capsize=9, label=condition2)

sus_xlabels = ['Like to use system frequently', 'System unnecessarily complex', 'System easy to use', 'Need technical support', 'Functions well integrated', 'Too much inconsistency', 'Learn to use very quickly', 'Inconvenient to use', 'Confident using the system', 'Need to learn a lot before use']
sus_xlabels = [ '\n'.join(wrap(l, 14)) for l in sus_xlabels ]
#sus_xlabels = [ label.replace(' ', '\n') for label in sus_xlabels]


ax.set_xticks(ind, sus_xlabels)
ax.legend()

#ax.set_xticks([0, 1, 2, 3, 4, 5, 6, 7, 8, 9]) 
#ax.set_xticklabels(sus_xlabels, fontsize=12, rotation=45)


ax.set_ylim([1, 5])
ax.set_yticks([1, 2, 3, 4, 5]) 
sus_ylabels = ['Strongly disagree', '', 'Neutral', '', 'Strongly agree']
sus_ylabels = [ '\n'.join(wrap(l, 10)) for l in sus_ylabels ]
ax.set_yticklabels(sus_ylabels)



ax.set_title("SUS questions", fontsize=15, fontweight="bold")
plt.tight_layout()
fig_sus_results_breakdown.savefig("sus_results_breakdown.png", dpi=300, bbox_inches='tight')
plt.show()

