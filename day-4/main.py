with open('./day-4/input.txt') as f:
    input_sequence_raw = f.readlines()

class SectionRange:

    def __init__(self, range_str: str) -> None:
        splitted_range = range_str.strip().split('-')
        self.range_start = int(splitted_range[0])
        self.range_end = int(splitted_range[1])

    def get_range_as_set(self):
        return set(range(self.range_start, self.range_end+1))

    def __str__(self) -> str:
        return f'{self.range_start}-{self.range_end}'


class SectionPair:

    def __init__(self, pair_str: str) -> None:
        cleaned_pair = pair_str.strip().split(',')
        self.first_section_range = SectionRange(cleaned_pair[0])
        self.second_section_range = SectionRange(cleaned_pair[1])

    def is_range_contained(self):
        first_range_set = self.first_section_range.get_range_as_set()
        second_range_set = self.second_section_range.get_range_as_set()
        if first_range_set.issubset(second_range_set): 
            return True
        if second_range_set.issubset(first_range_set):
            return True
        return False

    def is_range_overlapping(self):
        first_range_set = self.first_section_range.get_range_as_set()
        second_range_set = self.second_section_range.get_range_as_set()
        if first_range_set.intersection(second_range_set): return True
        return False


section_pairs = [SectionPair(raw_pair) for raw_pair in input_sequence_raw]

total_contained_pairs = 0

for pair in section_pairs:
    if pair.is_range_contained(): 
        total_contained_pairs += 1

print(f'Total contained pairs: {total_contained_pairs}')

# Part 2

total_overlapping_pairs = 0

for pair in section_pairs:
    if pair.is_range_overlapping():
        total_overlapping_pairs += 1

print(f'Total overlapping pairs: {total_overlapping_pairs}')
