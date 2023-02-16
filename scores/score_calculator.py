# get num judges
# get judge initials
# get num contestants
# get contestant names

class Judge:
    def __init__(self,name):
        self.name = name

class Contestant:
    # CONSTRUCTOR
    def __init__(self,name):
        self.name = name
        self.score = [0, 0]
        self.total_score = 0
        self.distance = 0
    # SETTER
    def set_distance(self, distance):
        self.distance = distance
    # METHOD
    def calc_total_score(self):
        self.total_score = self.score[0] + self.score[1]

##########
# INPUTS #
##########
 
judges = []
contestants = []

# Get input for how many judges then construct instances of the judge class 
# for each
# Append each object to a list
NUM_JUDGES = int( input("How many judges? ") )
for i in range(NUM_JUDGES):
    judges.append(Judge(input(f"Judge {i+1} Initials? ")))

# Get input for how many contestants then construct instances of the 
# contestants class for each
# Append each object to a list
NUM_CONTESTANTS = int( input("How many pairs? "))
for i in range(NUM_CONTESTANTS):
    contestants.append(Contestant(input(f"Pair {i+1} Names? ")))

# For each pair set the distance property to inputted value
for pair_idx, pair in enumerate(contestants):
    contestants[pair_idx].set_distance(float(input(f"{pair.name} Distance Travelled? ")))
    # For each judge, allow them to enter scores for design and ingenuity
    # Add the scores to the class score property
    for judge_idx, judge in enumerate(judges):
        design_score = int(input(f"{judge.name} design score for pair {pair.name}: "))
        contestants[pair_idx].score[0] += design_score
        ingenuity_score = int(input(f"{judge.name} ingenuity score for pair {pair.name}: "))
        contestants[pair_idx].score[1] += ingenuity_score
    # Sum the design and ingenuity scores, saving to "Contestant.total_score"
    contestants[pair_idx].calc_total_score()
         
    # print(contestants[pair_idx].score)  
    # print(contestants[pair_idx].total_score)

################
# CALCULATIONS #
################

# Normalise the values to 0-100
def normalise(list_to_normalise):
    normalised_list = []
    for number in list_to_normalise:
        normalised_list.append(round(float(number / max(list_to_normalise)) * 100, 2))
    return normalised_list

def combine(pair_distances, pair_scores):
    # First, normalise data
    n_pair_distances = normalise(pair_distances)
    n_pair_scores = normalise(pair_scores)
    # Initialise empty list
    combined_score = []
    # loop through each contestant
    for i, _ in enumerate(contestants):
        combined_score.append( (n_pair_distances[i] + n_pair_scores[i]*2) * 2/(6*NUM_JUDGES) )
        # calculations done to evenly weight 
    print(combined_score)
    return combined_score

#################
# CSV DATAFRAME #
#################

pair_names = []
pair_distances = []
pair_scores = []
# For each recorded value (name, distance, score) create a list to add to the dataframe
for pair_idx, pair in enumerate(contestants):
    pair_names.append(contestants[pair_idx].name)
    pair_distances.append(contestants[pair_idx].distance)
    pair_scores.append(contestants[pair_idx].total_score)
    
import pandas as pd

df = pd.DataFrame(
    zip(
        pair_names,
        pair_distances,
        pair_scores,
        normalise(pair_distances),
        normalise(pair_scores),
        combine(pair_distances, pair_scores)
    ),
    columns = [
        "pair_name",
        "distance",
        "total_score",
        "normalised_distance",
        "normalised_scores",
        "final_score"])

df.to_csv("scores.csv", index = False) # export dataframe to csv

############
# PLOTTING #
############

import seaborn as sns
from matplotlib import pyplot as plt

# set up subplot 
columns, rows = 1, 2
plt.subplots(figsize=(columns*6,rows*4))

plt.subplot(rows,columns,1)
ax1 = sns.lineplot(data = df, x=df.pair_name,y=df.distance)

plt.subplot(rows,columns,2)
ax2 = sns.lineplot(data = df, x=df.pair_name,y=df.final_score)

ax1.set(xlabel='Pair Name', ylabel='Distance (m)')
ax2.set(xlabel='Pair Name', ylabel='Score (normalised)')

plt.show()

# this could be refactored to be so much cleaner and better but i really dont
# care about it enough for that