from enum import Enum
from typing import List
import numpy as np
import math
from PIL import Image as im

class InstructionType(Enum):

    NOOP = 'noop'
    ADD_X = 'addx'

class Instruction:

    def __init__(self, line: str) -> None:
        splitted_line = line.strip().split(' ')
        instruction_str = splitted_line[0]
        self.instruction_type = None
        self.cycles_needed = None
        self.argument = None
        self.start_cycle = None
        self.terminated = False
        if instruction_str == InstructionType.NOOP.value:
            self.instruction_type = InstructionType.NOOP
            self.cycles_needed = 1
        else:
            self.instruction_type = InstructionType.ADD_X
            self.cycles_needed = 2
            self.argument = int(splitted_line[1])

    def start_instruction(self, actual_cycle: int):
        self.start_cycle = actual_cycle
        self.remaining_cycles = self.cycles_needed
    
    def execute_instruction(self, x: int):
        self.remaining_cycles = self.remaining_cycles - 1
        self.terminated = max(self.remaining_cycles, 0) == 0
        if self.instruction_type == InstructionType.ADD_X and self.terminated:
            return x + self.argument
        return x

    def __str__(self) -> str:
        value = 'RUNNING'
        if self.terminated: value = 'TERMINATED'
        if self.instruction_type.ADD_X:
            return f'{self.instruction_type.value} - {self.argument} - {value}'
        return f'{self.instruction_type.value} - {value}'

    def __repr__(self) -> str:
        return self.__str__()

class Signal:

    def __init__(self, x: int, cycle: int) -> None:
        self.x = x
        self.cycle = cycle

    def get_strength(self):
        return self.x * self.cycle

    def __str__(self) -> str:
        return f'Register: {self.x} - Cycle: {self.cycle}'

class Execution:

    def __init__(self, instructions : List[Instruction]) -> None:
        self.instructions: List[Instruction] = instructions
        self.current_cycle = 1
        self.register = 1
        self.next_instruction_pos = 0
        self.running_instructions : List[Instruction] = []
        self.signals : List[Signal] = []
        self.start_next_instruction()

    def execute_running_instructions(self, matrix: np.chararray):
        for running_instruction in self.running_instructions:
            self.draw(matrix)
            x = running_instruction.execute_instruction(self.register)
            self.register = x
            self.current_cycle += 1
            self.signals.append(Signal(x, self.current_cycle))

    def start_next_instruction(self):
        if self.next_instruction_pos < len(self.instructions):
            next_instruction = self.instructions[self.next_instruction_pos]
            next_instruction.start_instruction(self.current_cycle)
            self.running_instructions.append(next_instruction)
            self.next_instruction_pos += 1

    def update_running_instructions(self):
        self.running_instructions = [instruction for instruction in self.running_instructions if not instruction.terminated]

    def is_execution_running(self):
        return len(self.running_instructions) > 0

    def draw(self, matrix: np.ndarray):
        row = math.floor((self.current_cycle - 1) / 40)
        col = ((self.current_cycle - 1) % 40)
        if col == self.register - 1 or col == self.register or col == self.register + 1:
            matrix[row, col] = '#'
        else:
            matrix[row, col] = '.'

    def __str__(self) -> str:
        return f'Current cycle: {self.current_cycle} - {self.register} - Running instructions: {len(self.running_instructions)}'


with open('./day-10/input.txt') as f:
    input_sequence = f.readlines()

matrix = np.chararray((6,40), unicode=True)
instructions = [Instruction(line) for line in input_sequence]
execution = Execution(instructions)

while execution.is_execution_running():
    execution.execute_running_instructions(matrix)
    execution.start_next_instruction()
    execution.update_running_instructions()

signal_strenght_sum = 0

for signal in execution.signals:
    if (signal.cycle + 20) % 40 == 0: 
        signal_strenght_sum += signal.get_strength()

print(f'Signal strength: {signal_strenght_sum}')

np.savetxt('./day-10/output.txt', matrix, fmt="%s")