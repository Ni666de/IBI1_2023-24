import numpy as np
import matplotlib.pyplot as plt

N = 10000  
beta = 0.3 
gamma = 0.05  
S, I, R = N - 1, 1, 0  
S_list, I_list, R_list = [], [], []

time_steps = 1000
for _ in range(time_steps):
    new_infections = np.random.binomial(S, I / N)
    new_recoveries = np.random.binomial(I, gamma)
    
    S -= new_infections
    I += new_infections - new_recoveries
    R += new_recoveries
    
    S_list.append(S)
    I_list.append(I)
    R_list.append(R)

plt.plot(S_list, label='Susceptible')
plt.plot(I_list, label='Infected')
plt.plot(R_list, label='Recovered')
plt.xlabel('Time')
plt.ylabel('Number of People')
plt.title('SIR Model')
plt.legend()
plt.show()
