import random

# Define the fitness function based on user input
def fitness_function(x, equation):
    return eval(equation)  # Evaluate the equation using the provided input

# Create an initial population of potential solutions
def create_population(size, x_min, x_max):
    return [random.uniform(x_min, x_max) for _ in range(size)]

# Selection: choose the best half of the population
def selection(population, equation):
    sorted_population = sorted(population, key=lambda x: fitness_function(x, equation))
    return sorted_population[:len(sorted_population) // 2]

# Crossover: create new offspring
def crossover(parent1, parent2):
    return (parent1 + parent2) / 2  # Simple averaging crossover

# Mutation: randomly change a solution slightly
def mutate(x, mutation_rate=0.1):
    if random.random() < mutation_rate:
        return x + random.uniform(-1, 1)  # Small random change
    return x

# Main genetic algorithm function
def genetic_algorithm(pop_size, x_min, x_max, generations, equation):
    population = create_population(pop_size, x_min, x_max)
    
    for generation in range(generations):
        population = selection(population, equation)
        
        # Create the next generation
        next_generation = []
        while len(next_generation) < pop_size:
            parent1, parent2 = random.sample(population, 2)
            child = crossover(parent1, parent2)
            child = mutate(child)
            next_generation.append(child)
        
        population = next_generation

    # Return the best solution found
    best_solution = min(population, key=lambda x: fitness_function(x, equation))
    return best_solution, fitness_function(best_solution, equation)

# Get user input for the equation
equation = input("Enter the equation in terms of 'x' (e.g., 'x**2 - 4*x + 4'): ")

# Set default parameters
POPULATION_SIZE = 100
X_MIN = -10
X_MAX = 10
GENERATIONS = 100

# Run the genetic algorithm
solution, fitness = genetic_algorithm(POPULATION_SIZE, X_MIN, X_MAX, GENERATIONS, equation)

print(f"Best solution found: x = {solution}, with fitness (minimum value) = {fitness}")