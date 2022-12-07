from model import Command, Directory, File
from typing import List

SIZE_LIMIT = 100000

with open('./day-7/input.txt') as f:
    input_sequence_raw = [line.strip() for line in f.readlines()]
        
current_root = None
root = None

for line in input_sequence_raw:
    line_start = line.split(' ')[0]
    if line_start == '$':
        command = Command(line)
        if command.is_change_directory_command:
            current_root = command.change_directory(current_root)
        if root == None: 
            root = current_root
    elif line_start== 'dir':
        new_directory = Directory(line)
        current_root.add_dir_child(new_directory)
    else:
        new_file = File(line)
        current_root.add_file_child(new_file)



all_directories = root.get_all_subdirectories()
all_directories.append(root)

removable_directories = [element for element in all_directories if element.get_size() <= SIZE_LIMIT]
removable_directories_size = [element.get_size() for element in removable_directories]

print(f'Number of removable directories: {len(removable_directories_size)}')
print(f'Sum of removable directories: {sum(removable_directories_size)}')

# Part 2

TOTAL_MEMORY_AVAILABLE = 70000000
TOTAL_UNUSED_SPACE_NEEDED = 30000000

total_used_space = root.get_size()
actual_unused_space = TOTAL_MEMORY_AVAILABLE - total_used_space

print(f'Used space {total_used_space} of {TOTAL_MEMORY_AVAILABLE} -> {actual_unused_space} left')

target_directories : List[Directory]= []

for directory in all_directories:
    directory_size = directory.get_size()
    if actual_unused_space + directory_size > TOTAL_UNUSED_SPACE_NEEDED:
        target_directories.append(directory)

smallest_directory = min(target_directories)
print(f'Smallest directory to delete: {smallest_directory.name} with size {smallest_directory.get_size()}')