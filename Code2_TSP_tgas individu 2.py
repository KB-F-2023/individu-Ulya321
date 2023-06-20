import numpy as np
import random

# Inisialisasi populasi
def init_population(num_cities, population_size):
    population = []
    for i in range(population_size):
        individual = np.arange(num_cities)
        np.random.shuffle(individual)
        population.append(individual)
    return population

# Fungsi fitness
def calculate_fitness(individual, distances):
    total_distance = 0
    for i in range(len(individual)-1):
        total_distance += distances[individual[i]][individual[i+1]]
    return 1/total_distance

# Seleksi orang tua
def parent_selection(population):
    fitness_values = [calculate_fitness(individual, distances) for individual in population]
    total_fitness = sum(fitness_values)
    probabilities = [fitness/total_fitness for fitness in fitness_values]
    parents = random.choices(population, weights=probabilities, k=2)
    return parents

# Crossover
def crossover(parents):
    child = [-1]*len(parents[0])
    start = random.randint(0, len(parents[0])-2)
    end = random.randint(start+1, len(parents[0])-1)
    for i in range(start, end):
        child[i] = parents[0][i]
    j = 0
    for i in range(len(child)):
        if child[i] == -1:
            while parents[1][j] in child:
                j += 1
            child[i] = parents[1][j]
            j += 1
    return child

# Mutasi
def mutation(child, mutation_rate):
    for i in range(len(child)):
        if random.uniform(0, 1) < mutation_rate:
            j = random.randint(0, len(child)-1)
            child[i], child[j] = child[j], child[i]
    return child

# Algoritma Genetika
def genetic_algorithm(num_cities, distances, population_size, num_generations, mutation_rate):
    population = init_population(num_cities, population_size)
    for i in range(num_generations):
        new_population = []
        for j in range(population_size//2):
            parents = parent_selection(population)
            child1 = crossover(parents)
            child1 = mutation(child1, mutation_rate)
            child2 = crossover([parents[1], parents[0]])
            child2 = mutation(child2, mutation_rate)
            new_population.extend([child1, child2])
        population = new_population
    best_individual = max(population, key=lambda individual: calculate_fitness(individual, distances))
    return best_individual

# Contoh penggunaan
if __name__ == '__main__':
    # Jarak antar kota (misalnya berdasarkan koordinat)
    distances = np.array([
        [0, 10, 15, 20],
        [10, 0, 35, 25],
        [15, 35, 0, 30],
        [20, 25, 30, 0]
    ])
    num_cities = distances.shape[0]
    population_size = 100
    num_generations = 100
    mutation_rate = 0.01
    best_individual = genetic_algorithm(num_cities, distances, population_size, num_generations, mutation_rate)
    print('Individu terbaik:', best_individual)
