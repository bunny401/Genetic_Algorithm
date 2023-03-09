import random

# Define the range of possible values of x
x_min = -10
x_max = 10

# Define the parameters of the genetic algorithm
population_size = 10
mutation_rate = 0.1
generations = 50

# Define the fitness function
def fitness(x):
    return x**2

# Generate an initial population
population = [random.uniform(x_min, x_max) for i in range(population_size)]

# Repeat the genetic algorithm for a fixed number of generations
for generation in range(generations):
    # Evaluate the fitness of each chromosome
    fitness_values = [fitness(x) for x in population]

    # Select the fittest chromosomes
    fittest_chromosomes = [population[i] for i in sorted(range(population_size), key=lambda i: fitness_values[i], reverse=True)[:population_size//2]]

    # Create new offspring chromosomes through mutation and crossover
    offspring_chromosomes = []
    for i in range(population_size//2):
        parent1 = random.choice(fittest_chromosomes)
        parent2 = random.choice(fittest_chromosomes)
        offspring = (parent1 + parent2) / 2  # simple average crossover
        if random.random() < mutation_rate:
            offspring += random.uniform(-1, 1)
        offspring_chromosomes.append(offspring)

    # Evaluate the fitness of the offspring chromosomes
    offspring_fitness_values = [fitness(x) for x in offspring_chromosomes]

    # Select the fittest offspring chromosomes and replace the weakest members of the population with them
    population = [population[i] for i in sorted(range(population_size), key=lambda i: fitness_values[i], reverse=True)[:population_size//2]] + [offspring_chromosomes[i] for i in sorted(range(population_size//2), key=lambda i: offspring_fitness_values[i], reverse=True)]

# Find the best chromosome in the final population
best_chromosome = max(population, key=lambda x: fitness(x))
best_fitness = fitness(best_chromosome)

print("Best chromosome:", best_chromosome)
print("Best fitness:", best_fitness)
