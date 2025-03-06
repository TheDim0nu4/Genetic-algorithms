import random
import matplotlib.pyplot as plt
from knapsack_problem_solver import solve_knapsack_problem, fitness_function

#Dependence of suitability on the number of generations
def experiment_1():
    items = [{"weight": random.randint(1, 10), "value": random.randint(10, 100)} for _ in range(30)]
    generations_range = range(100, 1101, 100)
    pop_size = 100
    avg_best_fitness = []
    for generation_count in generations_range:
        knapsack_problem = {"items": items, "max_weight": 50}
        solution = solve_knapsack_problem(knapsack_problem, pop_size=pop_size, generation_count=generation_count)
        best_fitness = fitness_function(solution, knapsack_problem)
        avg_best_fitness.append(best_fitness)
    plt.figure(figsize=(10, 6))
    plt.plot(generations_range, avg_best_fitness, marker='o')
    plt.title("Závislosť vhodnosti od počtu generácií")
    plt.xlabel("Počet generácií")
    plt.ylabel("Najlepšia vhodnosť")
    plt.grid(True)
    plt.show()


#Dependence of fitness on population size
def experiment_2():
    items = [{"weight": random.randint(1, 10), "value": random.randint(10, 100)} for _ in range(30)]
    pop_size_range = range(50, 501, 50)  # Від 50 до 500
    generation_count = 500
    avg_best_fitness = []
    
    for pop_size in pop_size_range:
        knapsack_problem = {"items": items, "max_weight": 50}
        solution = solve_knapsack_problem(knapsack_problem, pop_size=pop_size, generation_count=generation_count)
        best_fitness = fitness_function(solution, knapsack_problem)
        avg_best_fitness.append(best_fitness)
    
    plt.figure(figsize=(10, 6))
    plt.plot(pop_size_range, avg_best_fitness, marker='o')
    plt.title("Závislosť vhodnosti od veľkosti populácie")
    plt.xlabel("Veľkosť populácie")
    plt.ylabel("Najlepšia vhodnosť")
    plt.grid(True)
    plt.show()


#Effect of mutation chance on fitness
def experiment_3():
    items = [{"weight": random.randint(1, 10), "value": random.randint(10, 100)} for _ in range(30)]
    mutation_chance_range = [0.1, 0.2, 0.3, 0.4, 0.5]  # Різні шанси мутації
    pop_size = 100
    generation_count = 500
    avg_best_fitness = []
    
    for mutation_chance in mutation_chance_range:
        knapsack_problem = {"items": items, "max_weight": 50}
        solution = solve_knapsack_problem(knapsack_problem, pop_size=pop_size, generation_count=generation_count, mutation_chance=mutation_chance)
        best_fitness = fitness_function(solution, knapsack_problem)
        avg_best_fitness.append(best_fitness)
    
    plt.figure(figsize=(10, 6))
    plt.plot(mutation_chance_range, avg_best_fitness, marker='o')
    plt.title("Vplyv šance mutácie na vhodnosť")
    plt.xlabel("Šanca mutácie")
    plt.ylabel("Najlepšia vhodnosť")
    plt.grid(True)
    plt.show()


#Influence of generations and population on suitability
def experiment_4():
    items = [{"weight": random.randint(1, 10), "value": random.randint(10, 100)} for _ in range(30)]
    pop_size_range = [50, 100, 200]
    generation_range = [200, 500, 1000]
    results = []

    for pop_size in pop_size_range:
        for generation_count in generation_range:
            knapsack_problem = {"items": items, "max_weight": 50}
            solution = solve_knapsack_problem(knapsack_problem, pop_size=pop_size, generation_count=generation_count)
            best_fitness = fitness_function(solution, knapsack_problem)
            results.append((pop_size, generation_count, best_fitness))

    pop_sizes, generations, fitness_values = zip(*results)
    plt.figure(figsize=(10, 6))
    for i, pop_size in enumerate(pop_size_range):
        plt.plot(generation_range, fitness_values[i::3], marker='o', label=f'populácia {pop_size}')
    
    plt.title("Vplyv generácií a populácie na vhodnosť")
    plt.xlabel("Počet generácií")
    plt.ylabel("Najlepšia vhodnosť")
    plt.legend()
    plt.grid(True)
    plt.show()


#Impact of problem complexity on suitability
def experiment_5():
    item_count_range = range(10, 101, 10)
    pop_size = 100
    generation_count = 500
    avg_best_fitness = []
    
    for item_count in item_count_range:
        items = [{"weight": random.randint(1, 20), "value": random.randint(10, 200)} for _ in range(item_count)]
        knapsack_problem = {"items": items, "max_weight": 100}
        solution = solve_knapsack_problem(knapsack_problem, pop_size=pop_size, generation_count=generation_count)
        best_fitness = fitness_function(solution, knapsack_problem)
        avg_best_fitness.append(best_fitness)
    
    plt.figure(figsize=(10, 6))
    plt.plot(item_count_range, avg_best_fitness, marker='o')
    plt.title("Vplyv zložitosti problému na vhodnosť")
    plt.xlabel("Počet predmetov")
    plt.ylabel("Najlepšia vhodnosť")
    plt.grid(True)
    plt.show()



if __name__ == "__main__":
    pass