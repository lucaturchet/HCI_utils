'''
Self-Assessment Manikin questionnaire calculator
Author: Luca Turchet @ University of Trento
Date: 18/12/2021

This program computes the mean and 95% confidence interval of the System Usability Scale,
as well as plots the mean and standard error/standard deviation of the responses to each question.
The SUS for each participants is also written in a .csv output file 

Usage: python sus.py 
You need to amend the variable "infile" to asign the path to your filename.csv containg the data

Note1: the example is for just two conditions, amend at your convenience
Note2: you can choose to plot the standard deviation or the error bars in the plot, amend the code at your convenience

'''

import csv
import numpy as np
import scipy.stats as st
import matplotlib.pyplot as plt
#from textwrap import wrap

#Here amend the file name
infile = "sam_9point_input_data.csv"


#Here set the actual names of the conditions according to the csv file
condition1 = "FA"
condition2 = "FVR"

valence_dictionary = {"V/a": 1, "V/b": 2, "V/c": 3, "V/d": 4, "V/e": 5, "V/f": 6, "V/g": 7, "V/h": 8, "V/i": 9}
arousal_dictionary = {"A/a": 1, "A/b": 2, "A/c": 3, "A/d": 4, "A/e": 5, "A/f": 6, "A/g": 7, "A/h": 8, "A/i": 9}
dominance_dictionary = {"D/a": 1, "D/b": 2, "D/c": 3, "D/d": 4, "D/e": 5, "D/f": 6, "D/g": 7, "D/h": 8, "D/i": 9}

valence_condition1 = []
arousal_condition1 = []
dominance_condition1 = []

valence_condition2= []
arousal_condition2 = []
dominance_condition2 = []

with open(infile, mode='r') as csv_file:
    csv_reader = csv.DictReader(csv_file, delimiter = ',')

    for row in csv_reader:

        v = valence_dictionary[row['valence']]
        a = arousal_dictionary[row['arousal']]
        d = dominance_dictionary[row['dominance']]


        if row['condition'] == condition1:

            valence_condition1.append(v)
            arousal_condition1.append(a)
            dominance_condition1.append(d)
       

        if row['condition'] == condition2:

            valence_condition2.append(v)
            arousal_condition2.append(a)
            dominance_condition2.append(d)




###########################################################################################################
# Subplot of the three individual measures ##################################################################

fig_all, (ax_v, ax_a, ax_d)= plt.subplots(1, 3, figsize=(11, 5))
fig_xlabels =[condition1, condition2]
fig_ind = np.arange(len(fig_xlabels))


# Valence ###########################################################################################

fig_v_results = [np.mean(valence_condition1), np.mean(valence_condition2)]
#fig_md_err = [np.std(valence_condition1), np.std(valence_condition2)] #standard deviation
fig_v_err = [st.sem(valence_condition1), st.sem(valence_condition2)] #standard error
ax_v.bar(fig_ind, fig_v_results, width=0.7, yerr=fig_v_err,  color=['#CD853F','silver'], ecolor='black', capsize=9)
ax_v.set_xticks([0, 1]) 
ax_v.set_xticklabels(fig_xlabels, fontsize=14)
ax_v.set_yticks([1, 2, 3, 4, 5, 6, 7, 8, 9]) 
ax_v.set_ylim([1, 9])
ax_v.set_title("Valence", fontsize=15, fontweight="bold")
#ax_v.set_ylabel("Score", fontsize=14)


# Arousal ###########################################################################################

fig_a_results = [np.mean(arousal_condition1), np.mean(arousal_condition2)]
#fig_md_err = [np.std(arousal_condition1), np.std(arousal_condition2)] #standard deviation
fig_a_err = [st.sem(arousal_condition1), st.sem(arousal_condition2)] #standard error
ax_a.bar(fig_ind, fig_a_results, width=0.7, yerr=fig_a_err,  color=['#CD853F','silver'], ecolor='black', capsize=9)
ax_a.set_xticks([0, 1]) 
ax_a.set_xticklabels(fig_xlabels, fontsize=14)
ax_a.set_yticks([1, 2, 3, 4, 5, 6, 7, 8, 9]) 
ax_a.set_ylim([1, 9])
ax_a.set_title("Arousal", fontsize=15, fontweight="bold")
#ax_a.set_ylabel("Score", fontsize=14)



# Dominance ###########################################################################################

fig_d_results = [np.mean(dominance_condition1), np.mean(dominance_condition2)]
#fig_md_err = [np.std(dominance_condition1), np.std(dominance_condition2)] #standard deviation
fig_d_err = [st.sem(dominance_condition1), st.sem(dominance_condition2)] #standard error
ax_d.bar(fig_ind, fig_d_results, width=0.7, yerr=fig_d_err,  color=['#CD853F','silver'], ecolor='black', capsize=9)
ax_d.set_xticks([0, 1]) 
ax_d.set_xticklabels(fig_xlabels, fontsize=14)
ax_d.set_yticks([1, 2, 3, 4, 5, 6, 7, 8, 9]) 
ax_d.set_ylim([1, 9])
ax_d.set_title("Dominance", fontsize=15, fontweight="bold")
#ax_d.set_ylabel("Score", fontsize=14)


######################
plt.tight_layout()
fig_all.savefig("fig_all.png", dpi=300, bbox_inches='tight')
plt.show()

