import numpy as np
import matplotlib.pyplot as plt

population_size = 100
beta = 0.3
gamma = 0.05
population = np.zeros((population_size, population_size))

outbreak = (np.random.choice(population_size), np.random.choice(population_size))
population[outbreak] = 1

time_steps = 100
for _ in range(time_steps):

    plt.imshow(population, cmap='viridis', interpolation='nearest')
    plt.show()
