import random

# Define the fitness function that evaluates the fitness of a solution

def fitness_function(solution):
    # In this example, we'll use a simple function f(x) = x^2
    return solution ** 2

# Generate a random solution within the problem space
def generate_random_solution():
    return random.uniform(-10, 10)

# Generate an initial population of solutions
def generate_initial_population(population_size):
    return [generate_random_solution() for _ in range(population_size)]

# Select two parent solutions from the population using tournament selection
def select_parents(population, fitnesses, tournament_size=3):
    # Randomly select a few solutions from the population and choose the fittest
    tournament = random.sample(list(enumerate(population)), tournament_size)
    fittest_solution = max(tournament, key=lambda x: fitnesses[x[0]])
    # Remove the fittest solution from the tournament and choose the fittest of the remaining
    tournament.remove(fittest_solution)
    second_fittest_solution = max(tournament, key=lambda x: fitnesses[x[0]])
    return fittest_solution[1], second_fittest_solution[1]

# Recombine the genes of the two parent solutions to create a child solution
def recombine_parents(parents):
    return (parents[0] + parents[1]) / 2.0

# Mutate the genes of a solution to create a new solution
def mutate_solution(solution, mutation_rate, mutation_range):
    if random.random() < mutation_rate:
        return solution + random.uniform(-mutation_range, mutation_range)
    else:
        return solution

# Run the genetic algorithm
def run_genetic_algorithm(population_size, num_generations, mutation_rate, mutation_range):
    # Generate an initial population of solutions
    population = generate_initial_population(population_size)

    # Iterate through the generations
    for i in range(num_generations):
        # Evaluate the fitness of each solution in the population
        fitnesses = [fitness_function(solution) for solution in population]

        # Generate a new population by selecting and recombining the fittest solutions
        new_population = []
        for _ in range(population_size):
            parents = select_parents(population, fitnesses)
            child = recombine_parents(parents)
            child = mutate_solution(child, mutation_rate, mutation_range)
            new_population.append(child)
        population = new_population

    # Return the fittest solution
    return max(population, key=fitness_function)

# Example usage
best_solution = run_genetic_algorithm(
    population_size=50,
    num_generations=100,
    mutation_rate=0.1,
    mutation_range=2.0
)

print(f"Best solution found: x = {best_solution}, f(x) = {fitness_function(best_solution)}")
