# Statistics Assignment
# Q1. 


import statistics
list = [4,1,5,4,3,7,2,3,4,1] # 10 household 
statistics.mode(list) # output 4

statistics.mean(list)  # output 3.4

statistics.median(list)  # output 3.5

# Calculate the probability that a household chosen at random from those in the survey would have (i) exactly 4 children (ii) more than 4 children (iii) less than 4 children.

# Data: number of children in 10 households
children_counts = [4, 1, 5, 4, 3, 7, 2, 3, 4, 1]

# Total number of households
total_households = len(children_counts)

# Count occurrences using lambda functions
count_4 = sum(map(lambda x: 1 if x == 4 else 0, children_counts))
count_more_than_4 = sum(map(lambda x: 1 if x > 4 else 0, children_counts))
count_less_than_4 = sum(map(lambda x: 1 if x < 4 else 0, children_counts))
print(count_4, '\n', count_more_than_4, '\n', count_less_than_4   )  # output 3  , 2  , 5

# Calculate probabilities
prob_exactly_4 = 3 / 10
prob_more_than_4 = 2 / 10
prob_less_than_4 = 5/ 10

# Print results
print(f"Probability of exactly 4 children: {prob_exactly_4:.2f}")  # output = Probability of exactly 4 children: 0.30
print(f"Probability of more than 4 children: {prob_more_than_4:.2f}")  # output= Probability of more than 4 children: 0.20

print(f"Probability of less than 4 children: {prob_less_than_4:.2f}") # output = Probability of less than 4 children: 0.50
