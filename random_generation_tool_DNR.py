from generation_utilities import *
from get_carbon_grams import *
import json

# Main part: Initialization V5.0 加入了锦标赛选择, 三个fitness functions：
# 1.Transferred data bytes 2.Page load time 3.Number of changes

print("******************** Populatoin Initialization ********************")
with open('parasettings.json','r',encoding='utf-8') as f:
    data = json.load(f)
pop_size = data['POP_SIZE']
p = creation_population_ram(pop_size)

fitness_value_transferred_data = []
fitness_value_ram = []
fitness_value_change_number = []
change_actions = []
carbon_footprint_value = []

for i in range(pop_size):
    fitness_value_transferred_data.append(p[i].fitness_transferred_data)
    fitness_value_change_number.append(p[i].fitness_change_number)
    fitness_value_ram.append(p[i].fitness_ram)
    change_actions.append(p[i].actions)
    carbon_footprint_value.append(getCarbonGrams(p[i].fitness_transferred_data))


print("Fitness Value_Quantity of transferred data: ", fitness_value_transferred_data)
print("Fitness Value_The number of Changes: ", fitness_value_change_number)
print("Fitness Value_Pgae load time: ", fitness_value_ram)
print("Change actions taken: ", change_actions)
print("Carbon Footprint Value: ", carbon_footprint_value, "g")