import string
from typing import List

with open('./day-3/input.txt') as f:
    input_sequence_raw = f.readlines()

class Rucksack:
    
    def __init__(self, raw_line: str) -> None:
        line = raw_line.strip()
        half = len(line)//2
        self.first_compartment = line[:half]
        self.second_compartment = line[half:]

    def get_common_item(self):
        return set(self.first_compartment).intersection(set(self.second_compartment)).pop()

alphabet_lowercase = list(string.ascii_lowercase)
alphabet_uppercase = list(string.ascii_uppercase)

alphabet = alphabet_lowercase + alphabet_uppercase

priority_mapping = {}
for i, letter in enumerate(alphabet, start=1):
    priority_mapping[letter] = i

priority_total = 0

for line in input_sequence_raw:
    rucksack = Rucksack(line)
    item = rucksack.get_common_item()
    priority_total = priority_total + priority_mapping[item]

print(f'The total priority is: {priority_total}')

# Part 2

class GroupRucksack:
    
    def __init__(self, raw_lines: List[str]) -> None:
        self.elves_items = []
        for line in raw_lines:
            self.elves_items.append(line.strip())

    def get_common_item(self):
        common_items = set(self.elves_items[0])
        for elf_items in self.elves_items:
            common_items = common_items.intersection(set(elf_items))
        return common_items.pop()

group_priority = 0

for i in range(0, len(input_sequence_raw)-1, 3):
    group_rucksack = GroupRucksack(raw_lines=input_sequence_raw[i:i+3])
    item = group_rucksack.get_common_item()
    group_priority = group_priority + priority_mapping[item]

print(f'The total group priority is: {group_priority}')