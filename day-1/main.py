# Read the input as single string
with open('./day-1/input.txt') as f:
    raw_file = f.read().strip()
# Create a data structure that contains a list of lists
elves_food_list = [raw.split('\n') for raw in raw_file.split('\n\n')]
# Convert the calories to integer
elves_food_converted = [[int(food) for food in elf_food] for elf_food in elves_food_list]
# Compute the maximum number of calories carried by an elf.
total_elves_food = [sum(element) for element in elves_food_converted]
print(f'The elf with the highest amount of food is carrying {max(total_elves_food)} calories.')
# Compute the top-3 highest amount of calories.
ordered_elves_food = sorted(total_elves_food)
print(f'The sum of the top-3 highest amount of calories: {sum(ordered_elves_food[-3:])}.')