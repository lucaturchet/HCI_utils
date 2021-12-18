'''
Creativity Support Index calculator
Author: Luca Turchet @ University of Trento
Date: 11/11/2020

This program computes the score of the Creativity Support Index and prints it on the console.
It takes in input two .csv files: the file of the factors and that of the pairwise comparisons

Usage: python csi.py 
You need to amend the variables "factordata" ad "pairwisedata" to asign the path to your files

'''

import numpy as np
#import sys
import csv


# Load data from csv file
factordata = 'csi-input-factor-data.csv'
pairwisedata = 'csi-input-pairwise-data.csv'
#factordata = sys.argv[1]
#pairwisedata = sys.argv[2]


CSIScore = []
CSIScoreByFactors = []


# PART1

with open(factordata, mode='r') as csv_file:
    csv_reader = csv.DictReader(csv_file, delimiter = ',')

    csi_collab_sum = []
    csi_enjoy_sum = []
    csi_expl_sum = []
    csi_expr_sum = []
    csi_immer_sum = []
    csi_effor_sum = []

    for row in csv_reader:
      
        collaboration_sum = (int(row['Collaboration1']) + int(row['Collaboration2']))
        enjoyment_sum = (int(row['Enjoyment1']) + int(row['Enjoyment2']))
        exploration_sum = (int(row['Exploration1']) + int(row['Exploration2']))
        expressiveness_sum = (int(row['Expressiveness1']) + int(row['Expressiveness2']))
        immersion_sum = (int(row['Immersion1']) + int(row['Immersion2']))
        results_worth_effort_sum = (int(row['ResultsWorthEffort1']) + int(row['ResultsWorthEffort2']))
     
        csi_collab_sum.append(collaboration_sum)
        csi_enjoy_sum.append(enjoyment_sum)
        csi_expl_sum.append(exploration_sum)
        csi_expr_sum.append(expressiveness_sum)
        csi_immer_sum.append(immersion_sum)
        csi_effor_sum.append(results_worth_effort_sum)
        

# PART2

with open(pairwisedata, mode='r') as csv_file:
    csv_reader = csv.DictReader(csv_file, delimiter = ',')

    csi_collab_count = 0
    csi_enjoy_count = 0
    csi_expl_count = 0
    csi_expr_count = 0
    csi_immer_count = 0
    csi_effor_count = 0    

    csi_collab_count_total = []
    csi_enjoy_count_total = []
    csi_expl_count_total = []
    csi_expr_count_total = []
    csi_immer_count_total = []
    csi_effor_count_total = []    


    for row in csv_reader:
     
        for key, value in row.items():

            if value == 'Work with other people':
                csi_collab_count = csi_collab_count + 1
            elif value == 'Enjoy using the system or tool':
                csi_enjoy_count = csi_enjoy_count + 1
            elif value == 'Explore many different ideas, outcomes, or possibilities':
                csi_expl_count = csi_expl_count + 1
            elif value == 'Be creative and expressive':
                csi_expr_count = csi_expr_count + 1
            elif value == 'Become immersed in the activity':
                csi_immer_count = csi_immer_count + 1
            elif value == 'Produce results that are worth the effort I put in':
                csi_effor_count = csi_effor_count + 1    

        
        csi_collab_count_total.append(csi_collab_count)
        csi_enjoy_count_total.append(csi_enjoy_count)
        csi_expl_count_total.append(csi_expl_count)
        csi_expr_count_total.append(csi_expr_count)
        csi_immer_count_total.append(csi_immer_count)
        csi_effor_count_total.append(csi_effor_count)   

        # Reset counters to zero
        csi_collab_count = 0
        csi_enjoy_count = 0
        csi_expl_count = 0
        csi_expr_count = 0
        csi_immer_count = 0
        csi_effor_count = 0


collaboration_sub = [a*b for a,b in zip(csi_collab_sum,csi_collab_count_total)]
enjoyment_sub = [a*b for a,b in zip(csi_enjoy_sum,csi_enjoy_count_total)]
exploration_sub = [a*b for a,b in zip(csi_expl_sum,csi_expl_count_total)]
expressiveness_sub = [a*b for a,b in zip(csi_expr_sum,csi_expr_count_total)]
immersion_sub = [a*b for a,b in zip(csi_immer_sum,csi_immer_count_total)]
results_worth_effort_sub = [a*b for a,b in zip(csi_effor_sum,csi_effor_count_total)]


CSI_score = [sum(x)/3.0 for x in zip(collaboration_sub, enjoyment_sub, exploration_sub, expressiveness_sub, immersion_sub, results_worth_effort_sub)]
CSI_score_mean = np.mean(CSI_score)
CSI_score_std = np.std(CSI_score)


collab_mean  = np.mean(collaboration_sub)
collab_std   = np.std(collaboration_sub)
enjoy_mean   = np.mean(enjoyment_sub)
enjoy_std    = np.std(enjoyment_sub)
explor_mean  = np.mean(exploration_sub)
explor_std   = np.std(exploration_sub)
express_mean = np.mean(expressiveness_sub)
express_std  = np.std(expressiveness_sub)
immers_mean  = np.mean(immersion_sub)
immers_std   = np.std(immersion_sub)
effort_mean  = np.mean(results_worth_effort_sub)
effort_std   = np.std(results_worth_effort_sub)


print("----------------------------------------------------------------------------")
print(f"CSI score (out of 100), mean: {CSI_score_mean}, std: {CSI_score_std}")



print("----------------------------------------------------------------------------")
print("Factor counts (out of 5), mean and std:")
print(f"Collaboration count, mean: {np.mean(csi_collab_count_total)}, std {np.std(csi_collab_count_total)}")
print(f"Enjoyment count, mean: {np.mean(csi_enjoy_count_total)}, std {np.std(csi_enjoy_count_total)}")
print(f"Exploration count, mean: {np.mean(csi_expl_count_total)}, std {np.std(csi_expl_count_total)}")
print(f"Expressiveness count, mean: {np.mean(csi_expr_count_total)}, std {np.std(csi_expr_count_total)}")
print(f"Immersion count, mean: {np.mean(csi_immer_count_total)}, std {np.std(csi_immer_count_total)}")
print(f"Results worth effort count, mean: {np.mean(csi_effor_count_total)}, std {np.std(csi_effor_count_total)}")


print("----------------------------------------------------------------------------")
print("Factor score (out of 20), mean and std:")
print(f"Collaboration score, mean: {np.mean(csi_collab_sum)}, std {np.std(csi_collab_sum)}")
print(f"Enjoyment score, mean: {np.mean(csi_enjoy_sum)}, std {np.std(csi_enjoy_sum)}")
print(f"Exploration score, mean: {np.mean(csi_expl_sum)}, std {np.std(csi_expl_sum)}")
print(f"Expressiveness score, mean: {np.mean(csi_expr_sum)}, std {np.std(csi_expr_sum)}")
print(f"Immersion score, mean: {np.mean(csi_immer_sum)}, std {np.std(csi_immer_sum)}")
print(f"Results worth effort score, mean: {np.mean(csi_effor_sum)}, std {np.std(csi_effor_sum)}")



print("----------------------------------------------------------------------------")
print("Weighted Factor scores (out of 100), mean and std:")
print(f"collab_mean: {collab_mean}, collab_std: {collab_std}")
print(f"enjoy_mean: {enjoy_mean}, enjoy_std: {enjoy_std}")
print(f"explor_mean: {explor_mean}, explor_std: {explor_std}")
print(f"express_mean: {express_mean}, express_std: {express_std}")
print(f"immers_mean: {immers_mean}, immers_std: {immers_std}")
print(f"effort_mean: {effort_mean}, effort_std: {effort_std}")
print("----------------------------------------------------------------------------")



