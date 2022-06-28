'''
Self-Assessment Manikin questionnaire calculator
Author: Luca Turchet @ University of Trento
Date: 18/12/2021

This program computes the mean and standard error/standard deviation for the 3 scales 
Valence, Arousal, Dominance of the Self-Assessment Manikin questionnaire assessed on 9-point scales, 
as well as plots the mean and standard error/standard deviation of the responses to each question.

Usage: 
python sam_9point.py 
You need to amend the variable "infile" to asign the path to your filename.csv containg the data

Note:
you can choose to plot the standard deviation or the error bars in the plot, amend the code at your convenience

'''

import csv
import numpy as np
import scipy.stats as st
import matplotlib.pyplot as plt
#from textwrap import wrap

#Here amend the file name
infile = "sam_9point_input_data.csv"


valence_dictionary = {"V/a": 1, "V/b": 2, "V/c": 3, "V/d": 4, "V/e": 5, "V/f": 6, "V/g": 7, "V/h": 8, "V/i": 9}
arousal_dictionary = {"A/a": 1, "A/b": 2, "A/c": 3, "A/d": 4, "A/e": 5, "A/f": 6, "A/g": 7, "A/h": 8, "A/i": 9}
dominance_dictionary = {"D/a": 1, "D/b": 2, "D/c": 3, "D/d": 4, "D/e": 5, "D/f": 6, "D/g": 7, "D/h": 8, "D/i": 9}

valence = []
arousal = []
dominance = []


with open(infile, mode='r') as csv_file:
    csv_reader = csv.DictReader(csv_file, delimiter = ',')

    for row in csv_reader:

        v = valence_dictionary[row['valence']]
        a = arousal_dictionary[row['arousal']]
        d = dominance_dictionary[row['dominance']]

        valence.append(v)
        arousal.append(a)
        dominance.append(d)




###########################################################################################################
# Subplot of the three scales ##################################################################

fig_all, ax = plt.subplots(figsize=(6, 4))
fig_xlabels =["Valence", "Arousal", "Dominance"]
fig_ind = np.arange(len(fig_xlabels))

fig_results = [np.mean(valence), np.mean(arousal), np.mean(dominance)]
#fig_err = [np.std(valence), np.std(arousal), np.std(dominance)] #standard deviation
fig_err = [st.sem(valence), st.sem(arousal), st.sem(dominance)]#standard error



ax.bar(fig_ind, fig_results, width=0.6, yerr=fig_err,  color=['#CD853F','silver', 'cornflowerblue'], ecolor='black', capsize=9)


ax.set_xticks([0, 1, 2]) 
ax.set_xticklabels(fig_xlabels, fontsize=14)
ax.set_yticks([1, 2, 3, 4, 5, 6, 7, 8, 9]) 
ax.set_ylim([1, 9])
ax.set_title("Self-Assessment Manikin", fontsize=15, fontweight="bold")
#ax.set_ylabel("Score", fontsize=14)



######################
plt.tight_layout()
fig_all.savefig("fig_SAM_all.png", dpi=300, bbox_inches='tight')
plt.show()

