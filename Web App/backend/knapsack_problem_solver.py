import random

def generate_population( items_count, pop_size ):

    population = list()
    for i in range( pop_size ):
        pop_unit = [ random.choice([True, False]) for _ in range( items_count ) ]
        population.append( pop_unit )

    return population


def fitness_function( pop_unit, knapsack_problem ):

    weight, value = 0, 0
    for index, item in enumerate( knapsack_problem["items"] ):
        if pop_unit[index] is True:
            weight += item["weight"]
            value += item["value"]

    if weight > knapsack_problem["max_weight"]:
        value = 0

    return value


def crossover( parent1, parent2 ):

    child = list()
    for chromosome1, chromosome2 in zip( parent1, parent2):
        new_chromosome = random.choice([chromosome1, chromosome2])
        child.append( new_chromosome )

    return child


def mutation( child, mutation_chance, num_generation, generation_count ):

    mutation_chance = mutation_chance - (mutation_chance-0.1) * (num_generation / generation_count) # gradually reduce the mutation chance from the highest (mutation_chance) to 0.1

    if random.random() < mutation_chance: 
        mutation_child = child[:]
        random_chromosome = random.randint(0, len( mutation_child )-1)
        mutation_child[ random_chromosome ] = not mutation_child[ random_chromosome ]

        return mutation_child

    return child


def create_new_generation( population, knapsack_problem, pop_size, mutation_chance, num_generation, generation_count ):

    new_generation = list()
    all_parents = sorted( population, key=lambda pop_unit: fitness_function( pop_unit, knapsack_problem), reverse=True )[:round(pop_size*0.4)] # We take 40% of the best from the population for crossing

    for _ in range( round(pop_size*0.2) ): # *0.2 because we took 0.4, i.e. 40% of the population for crossing, in each iteration we generate 2 parents, so we need 0.4/2 iterations
        parent1 = random.choice( all_parents )
        all_parents.remove( parent1 )
        parent2 = random.choice( all_parents )
        all_parents.remove( parent2 )

        child = crossover( parent1, parent2 )
        mutation_child = mutation( child, mutation_chance, num_generation, generation_count )
        new_generation.append( mutation_child )

    new_population = population + new_generation

    return sorted( new_population, key=lambda pop_unit: fitness_function( pop_unit, knapsack_problem), reverse=True )[:pop_size] # [:pop_size] leave the population unchanged in size


def solve_knapsack_problem( knapsack_problem, pop_size=100, generation_count=1000, mutation_chance=0.5 ):

    pop_size =  determinate_pop_size( len( knapsack_problem["items"] ) )

    population = generate_population( len( knapsack_problem["items"] ), pop_size )
    for num_generation in range( generation_count ):
        population = create_new_generation( population, knapsack_problem, pop_size, mutation_chance, num_generation, generation_count )

    best_pop_unit = population[0]
    
    fitnes = fitness_function( best_pop_unit, knapsack_problem )
    items = knapsack_problem["items"]
    best_items = [ {"name": items[index]["name"], "weight": items[index]["weight"], "value": items[index]["value"] } for index, item in enumerate(best_pop_unit) if item is True ] # return the items that were taken
    weight = sum( [ item["weight"] for item in best_items] )

    return best_items, weight, fitnes


def determinate_pop_size( count_items ):
    return 20*count_items

 

