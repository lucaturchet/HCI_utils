'''
Analysis and plot of the NASA TLX (raw) questionnaire
Author: Luca Turchet @ University of Trento
Date: 17/12/2021

Usage: python nasa_tlx_raw.py 
You need to amend the variable "infile" to asign the path to your filename.csv containg the data

Note1: the example is for just two conditions, amend at your convenience
Note2: you can choose to plot the standard deviation or the error bars in the plot, amend at your convenience
'''

import csv
import numpy as np
import scipy.stats as st
import matplotlib.pyplot as plt
#from textwrap import wrap

#Here amend the file name
infile = "NASA_TLX_example_data.csv"


#Here set the actual names of the conditions according to the csv file
condition1 = "FA"
condition2 = "FVR"

total_workload_condition1 = [] #Array of condition1 results for each participant 
md_condition1 = []
pd_condition1 = []
td_condition1 = []
pe_condition1 = []
ef_condition1 = []
fr_condition1 = []

total_workload_condition2 = [] #Array of condition2 results for each participant 
md_condition2 = []
pd_condition2 = []
td_condition2 = []
pe_condition2 = []
ef_condition2 = []
fr_condition2 = []


with open(infile, mode='r') as csv_file:
    csv_reader = csv.DictReader(csv_file, delimiter = ',')

    # each row represents a participant
    for row in csv_reader:

        md = int(row['mental_demand'])
        pd = int(row['physical_demand'])
        td = int(row['temporal_demand'])
        pe = int(row['performance'])
        ef = int(row['effort'])
        fr = int(row['frustration'])

        if row['condition'] == condition1:

            md_condition1.append(md)
            pd_condition1.append(pd)
            td_condition1.append(td)
            pe_condition1.append(pe)
            ef_condition1.append(ef)
            fr_condition1.append(fr)

            total_workload_condition1.append(md + pd + td + pe + ef + fr)


        if row['condition'] == condition2:

            md_condition2.append(md)
            pd_condition2.append(pd)
            td_condition2.append(td)
            pe_condition2.append(pe)
            ef_condition2.append(ef)
            fr_condition2.append(fr)

            total_workload_condition2.append(md + pd + td + pe + ef + fr)            



# Total Workload ###########################################################################################

total_workload_condition1_mean = np.mean(total_workload_condition1)
total_workload_condition1_std = np.std(total_workload_condition1)
total_workload_condition1_ster = st.sem(total_workload_condition1)

total_workload_condition2_mean = np.mean(total_workload_condition2)
total_workload_condition2_std = np.std(total_workload_condition2)
total_workload_condition2_ster = st.sem(total_workload_condition2)

print("\n----------------------------------------------------------------------------")
print(f"\ntotal_workload_condition1:\n mean: {total_workload_condition1_mean}, std: {total_workload_condition1_std}, ster : {total_workload_condition1_ster}")
print(f"\ntotal_workload_condition2:\n mean: {total_workload_condition2_mean}, std: {total_workload_condition2_std}, ster : {total_workload_condition2_ster}")
print("\n----------------------------------------------------------------------------")


fig_tw, ax_tw = plt.subplots(figsize=(6, 6))
fig_tw_xlabels =[condition1, condition2]
fig_tw_results = [total_workload_condition1_mean, total_workload_condition2_mean]
#fig_tw_err = [total_workload_condition1_std, total_workload_condition2_std] # standard deviation
fig_tw_err = [total_workload_condition1_ster, total_workload_condition2_ster] # standard error
fig_tw_ind = np.arange(len(fig_tw_xlabels))
ax_tw.bar(fig_tw_ind, fig_tw_results, width=0.7, yerr=fig_tw_err,  color=['#CD853F','silver'], ecolor='black', capsize=9)
ax_tw.set_xticks([0, 1]) 
ax_tw.set_xticklabels(fig_tw_xlabels, fontsize=14)
ax_tw.set_title("Total Workload", fontsize=15, fontweight="bold")
ax_tw.set_ylabel("TLX Score", fontsize=14)
plt.tight_layout()
fig_tw.savefig("fig_tw.png", dpi=300, bbox_inches='tight')
plt.show()


###########################################################################################################
# Subplot of the six individual measures ##################################################################

fig_all, ((ax_md, ax_pd, ax_td), (ax_pe, ax_ef, ax_fr))= plt.subplots(2, 3, figsize=(14, 8))
fig_xlabels =[condition1, condition2]
fig_ind = np.arange(len(fig_xlabels))


# Mental Demand ###########################################################################################

fig_md_results = [np.mean(md_condition1), np.mean(md_condition2)]
#fig_md_err = [np.std(md_condition1), np.std(md_condition2)] #standard deviation
fig_md_err = [st.sem(md_condition1), st.sem(md_condition2)] #standard error
ax_md.bar(fig_ind, fig_md_results, width=0.7, yerr=fig_md_err,  color=['#CD853F','silver'], ecolor='black', capsize=9)
ax_md.set_xticks([0, 1]) 
ax_md.set_xticklabels(fig_xlabels, fontsize=14)
ax_md.set_yticks([0, 20, 40, 60, 80, 100]) 
ax_md.set_title("Mental Demand", fontsize=15, fontweight="bold")
ax_md.set_ylabel("TLX Score", fontsize=14)


# Physical Demand ###########################################################################################

fig_pd_results = [np.mean(pd_condition1), np.mean(pd_condition2)]
#fig_pd_err = [np.std(pd_condition1), np.std(pd_condition2)] #standard deviation
fig_pd_err = [st.sem(pd_condition1), st.sem(pd_condition2)] #standard error
ax_pd.bar(fig_ind, fig_pd_results, width=0.7, yerr=fig_pd_err,  color=['#CD853F','silver'], ecolor='black', capsize=9)
ax_pd.set_xticks([0, 1]) 
ax_pd.set_xticklabels(fig_xlabels, fontsize=14)
ax_pd.set_yticks([0, 20, 40, 60, 80, 100]) 
ax_pd.set_title("Physical Demand", fontsize=15, fontweight="bold")
#ax_pd.set_ylabel("TLX Score", fontsize=14)

# Temporal Demand ###########################################################################################

fig_td_results = [np.mean(td_condition1), np.mean(td_condition2)]
#fig_td_err = [np.std(td_condition1), np.std(td_condition2)] #standard deviation
fig_td_err = [st.sem(td_condition1), st.sem(td_condition2)] #standard error
ax_td.bar(fig_ind, fig_td_results, width=0.7, yerr=fig_td_err,  color=['#CD853F','silver'], ecolor='black', capsize=9)
ax_td.set_xticks([0, 1]) 
ax_td.set_xticklabels(fig_xlabels, fontsize=14)
ax_td.set_yticks([0, 20, 40, 60, 80, 100]) 
ax_td.set_title("Temporal Demand", fontsize=15, fontweight="bold")
#ax_td.set_ylabel("TLX Score", fontsize=14)


# Performance ###########################################################################################

fig_pe_results = [np.mean(pe_condition1), np.mean(pe_condition2)]
#fig_pe_err = [np.std(pe_condition1), np.std(pe_condition2)] #standard deviation
fig_pe_err = [st.sem(pe_condition1), st.sem(pe_condition2)] #standard error
ax_pe.bar(fig_ind, fig_pe_results, width=0.7, yerr=fig_pe_err,  color=['#CD853F','silver'], ecolor='black', capsize=9)
ax_pe.set_xticks([0, 1]) 
ax_pe.set_xticklabels(fig_xlabels, fontsize=14)
ax_pe.set_yticks([0, 20, 40, 60, 80, 100]) 
ax_pe.set_title("Performance", fontsize=15, fontweight="bold")
ax_pe.set_ylabel("TLX Score", fontsize=14)


# Effort ###########################################################################################

fig_ef_results = [np.mean(ef_condition1), np.mean(ef_condition2)]
#fig_ef_err = [np.std(ef_condition1), np.std(ef_condition2)] #standard deviation
fig_ef_err = [st.sem(ef_condition1), st.sem(ef_condition2)] #standard error
ax_ef.bar(fig_ind, fig_ef_results, width=0.7, yerr=fig_ef_err,  color=['#CD853F','silver'], ecolor='black', capsize=9)
ax_ef.set_xticks([0, 1]) 
ax_ef.set_xticklabels(fig_xlabels, fontsize=14)
ax_ef.set_yticks([0, 20, 40, 60, 80, 100]) 
ax_ef.set_title("Effort", fontsize=15, fontweight="bold")
#ax_ef.set_ylabel("TLX Score", fontsize=14)


# Frustration ###########################################################################################

fig_fr_results = [np.mean(fr_condition1), np.mean(fr_condition2)]
#fig_fr_err = [np.std(fr_condition1), np.std(fr_condition2)] #standard deviation
fig_fr_err = [st.sem(fr_condition1), st.sem(fr_condition2)] #standard error
ax_fr.bar(fig_ind, fig_fr_results, width=0.7, yerr=fig_fr_err,  color=['#CD853F','silver'], ecolor='black', capsize=9)
ax_fr.set_xticks([0, 1]) 
ax_fr.set_xticklabels(fig_xlabels, fontsize=14)
ax_fr.set_yticks([0, 20, 40, 60, 80, 100]) 
ax_fr.set_title("Frustration", fontsize=15, fontweight="bold")
#ax_fr.set_ylabel("TLX Score", fontsize=14)


######################
plt.tight_layout()
fig_all.savefig("fig_all.png", dpi=300, bbox_inches='tight')
plt.show()

