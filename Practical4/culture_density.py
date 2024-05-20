initial_density = 5  
doubling_rate = 2  
max_density = 90  
current_density = initial_density
days = 0

while current_density <= max_density:
    days += 1
    current_density *= doubling_rate  

print(f"The cell density goes over 90% on day {days}.")
