import re
from typing import List

with open('./day-5/input.txt') as f:
    input_sequence_raw = f.read()

stacks_raw = input_sequence_raw.split('\n\n')[0]
instructions_raw = input_sequence_raw.split('\n\n')[1]


def create_data_structure(stacks_raw: str):
    stacks_rows = stacks_raw.split('\n')
    stacks_info = stacks_rows[-1]
    crates_pos = [i for i, elem in enumerate(stacks_info) if elem != '' and elem != ' ']
    stacks = [[] for _ in range(len(crates_pos))]
    for row in stacks_rows[:-1]:
        for i, pos in enumerate(crates_pos):
            if row[pos] != ' ': stacks[i].append(row[pos])
    return stacks

def execute_instructions(stack_data_structure : List, instructions_raw : str, is_new_mover_version : bool = False):
    instruction_list = instructions_raw.strip().split('\n')
    for instruction in instruction_list:
        command = Command(instruction)
        if is_new_mover_version:
            command.execute_command(stacks=stack_data_structure, is_new_mover_version=True)
        else:
            command.execute_command(stacks=stack_data_structure)

class Command:
    
    def __init__(self, line: str) -> None:
        values = re.findall(r'\d+', line)
        self.number_of_elements = int(values[0])
        self.start = int(values[1]) - 1
        self.end = int(values[2]) - 1

    def execute_command(self, stacks : List[List[str]], is_new_mover_version : bool = False):
        start_stack = stacks[self.start]
        destination_stack = stacks[self.end]
        if is_new_mover_version:
            temp = []
            for _ in range(self.number_of_elements):
                temp.insert(0, start_stack.pop(0))
            for element in temp:
                destination_stack.insert(0, element)
        else:
            for _ in range(self.number_of_elements):
                stacks[self.end].insert(0, stacks[self.start].pop(0))

    def __str__(self) -> str:
        representation = "------------Command------------\n"
        representation += f"Number of elements to move: {self.number_of_elements}\n"
        representation += f"From stack {self.start} to stack {self.end}\n"
        return representation

stacks_crate_mover_9000 = create_data_structure(stacks_raw)
execute_instructions(stacks_crate_mover_9000, instructions_raw)
    
top_crates = ''.join([stack.pop(0) for stack in stacks_crate_mover_9000])
print(f'Top crates with Crate Mover 9000: {top_crates}')

stacks_crate_mover_9001 = create_data_structure(stacks_raw)
execute_instructions(stacks_crate_mover_9001, instructions_raw, is_new_mover_version=True)

top_crates_new_crate_mover = ''.join([stack.pop(0) for stack in stacks_crate_mover_9001])
print(f'Top crates with Crate Mover 9001: {top_crates_new_crate_mover}')