import numpy as np

with open('./day-8/input.txt') as f:
    input_sequence_raw = [line.strip() for line in f.readlines()]

matrix = []

for line in input_sequence_raw:
    _ = np.array(list(line), dtype=int)
    matrix.append(_)

matrix_np = np.array(matrix)

class Tree:

    def __init__(self, value: int, i: int, j: int, row : np.ndarray, column: np.ndarray) -> None:
        self.value = value
        self.pos_i = i
        self.pos_j = j
        self.right_array = np.array(row[j+1:])
        self.left_array = np.flip(np.array(row[:j]))
        self.bottom_array = np.array(column[i+1:])
        self.top_array = np.flip(np.array(column[:i]))
        self.number_of_rows = row.shape[0]
        self.number_of_cols = column.shape[0]
        self.is_edge_tree = (self.pos_i == 0 or self.pos_i == self.number_of_rows - 1) or (self.pos_j == 0 or self.pos_j == self.number_of_cols - 1)

    def is_visible_from(self):
        visible_from_right = len(self.right_array) == 0 or self.value > max(self.right_array)
        visible_from_left = len(self.left_array) == 0 or self.value > max(self.left_array)
        visible_from_bottom = len(self.bottom_array) == 0 or self.value > max(self.bottom_array)
        visible_from_top = len(self.top_array) == 0 or self.value > max(self.top_array)
        return visible_from_right, visible_from_left, visible_from_bottom, visible_from_top

    def is_visible(self):
        return any(list(self.is_visible_from()))

    def compute_direction_score(self, array: np.ndarray, is_visible: bool):
        if is_visible:
            return len(array)
        elif len(array) == 0:
            return 0
        else:
            return np.argmax(array >= self.value) + 1


    def compute_tree_score(self):
        score = 1
        score *= self.compute_direction_score(self.right_array, is_visible=self.is_visible_from()[0])
        score *= self.compute_direction_score(self.left_array, is_visible=self.is_visible_from()[1])
        score *= self.compute_direction_score(self.bottom_array, is_visible=self.is_visible_from()[2])
        score *= self.compute_direction_score(self.top_array, is_visible=self.is_visible_from()[3])
        return score

    def compute_tree_scores(self):
        right_score = self.compute_direction_score(self.right_array, is_visible=self.is_visible_from()[0])
        left_score = self.compute_direction_score(self.left_array, is_visible=self.is_visible_from()[1])
        bottom_score = self.compute_direction_score(self.bottom_array, is_visible=self.is_visible_from()[2])
        top_score = self.compute_direction_score(self.top_array, is_visible=self.is_visible_from()[3])
        return (right_score, left_score, bottom_score, top_score)
    
    def __repr__(self) -> str:
        return f'{self.value} - ({self.pos_i}, {self.pos_j})'


elements_count = 0

for i, row in enumerate(matrix_np):
    for j, cell in enumerate(row):
        column = matrix_np[:, j]
        tree = Tree(cell, i, j, row, column)
        if tree.is_edge_tree or tree.is_visible():
            elements_count += 1
            
print(f'Number of visible trees: {elements_count}')

tree_scores = []

for i, row in enumerate(matrix_np):
    for j, cell in enumerate(row):
        column = matrix_np[:, j]
        tree = Tree(cell, i, j, row, column)
        tree_scores.append((tree, tree.compute_tree_score()))

max_scored_tree, score = max(tree_scores, key = lambda x: x[1])

print(f'Max scored tree: {score}')