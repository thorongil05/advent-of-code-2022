from enum import Enum, IntEnum

class AdversaryPlay(Enum):

    ROCK = "A"
    PAPER = "B"
    SCISSOR = "C"

class PlayerPlay(Enum):

    ROCK = "X"
    PAPER = "Y"
    SCISSOR = "Z"

class Point(IntEnum):
    
    ROCK = 1
    PAPER = 2
    SCISSOR = 3
    WIN = 6
    DRAW = 3
    LOST = 0


def compute_points(adversary_play : str, player_play: str) -> int:
    if adversary_play == AdversaryPlay.ROCK.value:
        if player_play == PlayerPlay.ROCK.value: return Point.ROCK + Point.DRAW
        if player_play == PlayerPlay.PAPER.value: return Point.PAPER + Point.WIN
        if player_play == PlayerPlay.SCISSOR.value: return Point.SCISSOR + Point.LOST
    if adversary_play == AdversaryPlay.PAPER.value:
        if player_play == PlayerPlay.ROCK.value: return Point.ROCK + Point.LOST
        if player_play == PlayerPlay.PAPER.value: return Point.PAPER + Point.DRAW
        if player_play == PlayerPlay.SCISSOR.value: return Point.SCISSOR + Point.WIN
    if adversary_play == AdversaryPlay.SCISSOR.value:
        if player_play == PlayerPlay.ROCK.value: return Point.ROCK + Point.WIN
        if player_play == PlayerPlay.PAPER.value: return Point.PAPER + Point.LOST
        if player_play == PlayerPlay.SCISSOR.value: return Point.SCISSOR + Point.DRAW
    

with open('./day-2/input.txt') as f:
    input_sequence_raw = f.readlines()

games = [(line.strip().split(' ')[0], line.strip().split(' ')[1]) for line in input_sequence_raw]
total_points = sum([compute_points(game[0], game[1]) for game in games])

print(f'Total number of points: {total_points}')


# Part 2

class ExpectedResult(Enum):

    WIN = "Z"
    DRAW = "Y"
    LOST = "X"


def compute_points_with_expected_result(adversary_play : str, expected_result: str) -> int:
    if adversary_play == AdversaryPlay.ROCK.value:
        if expected_result == ExpectedResult.DRAW.value: return Point.ROCK + Point.DRAW
        if expected_result == ExpectedResult.WIN.value: return Point.PAPER + Point.WIN
        if expected_result == ExpectedResult.LOST.value: return Point.SCISSOR + Point.LOST
    if adversary_play == AdversaryPlay.PAPER.value:
        if expected_result == ExpectedResult.LOST.value: return Point.ROCK + Point.LOST
        if expected_result == ExpectedResult.DRAW.value: return Point.PAPER + Point.DRAW
        if expected_result == ExpectedResult.WIN.value: return Point.SCISSOR + Point.WIN
    if adversary_play == AdversaryPlay.SCISSOR.value:
        if expected_result == ExpectedResult.WIN.value: return Point.ROCK + Point.WIN
        if expected_result == ExpectedResult.LOST.value: return Point.PAPER + Point.LOST
        if expected_result == ExpectedResult.DRAW.value: return Point.SCISSOR + Point.DRAW

total_points_with_expected_result = sum([compute_points_with_expected_result(game[0], game[1]) for game in games])
print(f'Total number of points with expected result: {total_points_with_expected_result}')