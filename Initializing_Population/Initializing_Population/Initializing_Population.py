import random

# Define the range of values
MIN_VALUE = -10
MAX_VALUE = 10

# Define the size of the population
POPULATION_SIZE = 50

# Create an initial population of chromosomes
population = []
for i in range(POPULATION_SIZE):
    chromosome = random.uniform(MIN_VALUE, MAX_VALUE)
    population.append(chromosome)

# Print the population
print("Initial population:")
print(population)

