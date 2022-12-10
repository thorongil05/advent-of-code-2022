import numpy as np
from enum import Enum

class CommandType(Enum):

    RIGHT = 'R'
    LEFT = 'L'
    UP = 'U'
    DOWN = 'D'

class Command:

    def __init__(self, line: str) -> None:
        splitted_line = line.strip().split(' ')
        self.command_type = splitted_line[0]
        self.steps = int(splitted_line[1])

    def __str__(self) -> str:
        return f'{self.command_type}: {self.steps}'
    
    def __repr__(self) -> str:
        return self.__str__()

class Position:

    def __init__(self, x: int, y: int) -> None:
        self.x = x
        self.y = y

    def is_adiacent(self, position):
        if self.x == position.x:
            return self.y == position.y or self.y + 1 == position.y or self.y - 1 == position.y
        if self.y == position.y:
            return self.x == position.x or self.x + 1 == position.x or self.x - 1 == position.x
        if abs(self.x - position.x) == 1 and abs(self.y - position.y) == 1: return True
        return False

    def get_direction(self, target):
        if self.x < target.x:
            if self.y < target.y: return CommandType.RIGHT, CommandType.DOWN
            if self.y == target.y: return None, CommandType.DOWN
            if self.y > target.y: return CommandType.LEFT, CommandType.DOWN
        if self.x > target.x:
            if self.y < target.y: return CommandType.RIGHT, CommandType.UP
            if self.y == target.y: return None, CommandType.UP
            if self.y > target.y: return CommandType.LEFT, CommandType.UP
        if self.x == target.x:
            if self.y < target.y: return CommandType.RIGHT, None
            if self.y > target.y: return CommandType.LEFT, None
        return None, None
        

    def move(self, command_type: str):
        if command_type == CommandType.UP.value:
            self.x -= 1
        if command_type == CommandType.DOWN.value:
            self.x += 1
        if command_type == CommandType.LEFT.value:
            self.y -= 1
        if command_type == CommandType.RIGHT.value:
            self.y += 1
    
    def follow(self, target):
        if not self.is_adiacent(target): 
            x_direction, y_direction = self.get_direction(target)
            if x_direction:
                self.move(command_type=x_direction.value)
            if y_direction:
                self.move(command_type=y_direction.value)

    def __str__(self) -> str:
        return f'({self.x}, {self.y})'

    def __repr__(self) -> str:
        return f'({self.x}, {self.y})'

    def __eq__(self, __o: object) -> bool:
        if isinstance(__o, Position):
            return (self.x == __o.x and self.y == __o.y)
        return False

    def __hash__(self) -> int:
        return hash(str(self.x) + str(self.y))


with open('./day-9/input.txt') as f:
    input_sequence = [Command(line) for line in f.readlines()]

head_pos = Position(4, 0)
tail_pos = Position(4, 0)
starting_pos = Position(4, 0)

tail_positions = []

for command in input_sequence:
    for _ in range(0, command.steps):
        head_pos.move(command.command_type)
        tail_pos.follow(head_pos)
        tail_positions.append(Position(tail_pos.x, tail_pos.y))

tail_positions_set = set(tail_positions)
print(f'Number of positions visited by the tail: {len(tail_positions_set)}')

# Part - 2

rows = 21
cols = 26

head = Position(15, 11)
knots = [Position(15, 11) for _ in range(9)]

tail_visited_positions = []

for command in input_sequence:
    for _ in range(0, command.steps):
        head.move(command.command_type)
        for i, knot in enumerate(knots):
            if i == 0: 
                knot.follow(head)
            else:
                knot.follow(knots[i-1])
            if i == len(knots)-1:
                tail_visited_positions.append(Position(knot.x, knot.y))

tail_visited_positions_set = set(tail_visited_positions)
print(f'Number of positions visited by the rope: {len(tail_visited_positions_set)}')