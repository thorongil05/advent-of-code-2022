from enum import Enum
from typing import List

class CommandType(Enum):

    CD = 'cd'
    LS = 'ls'

class File:

    def __init__(self, line: str) -> None:
        self.dimension = int(line.split(' ')[0])
        self.file_name = line.split(' ')[1]

    def __str__(self) -> str:
        return f'- {self.file_name} (file, size={self.dimension})'

class Directory:

    def __init__(self, line: str) -> None:
        splitted_line = line.split(' ')
        if len(splitted_line) > 1:
            self.name = line.split(' ')[1]
        else:
            self.name = line
        self.children_directories : List[Directory] = []
        self.children_files : List[File] = []
        self.parent = None
        self.level = 0

    def add_dir_child(self, child_directory):
        self.children_directories.append(child_directory)
        child_directory.parent = self
        child_directory.level = self.level + 1

    def add_file_child(self, file_child: File):
        self.children_files.append(file_child)

    def get_size(self):
        total = 0
        for file in self.children_files:
            total += file.dimension
        for directory in self.children_directories:
            total += directory.get_size()
        return total

    def get_all_subdirectories(self):
        subdirectories = self.children_directories.copy()
        for child in self.children_directories:
            subdirectories.extend(child.get_all_subdirectories())
        return subdirectories

    def __gt__(self, other):
        return self.get_size() >= other.get_size()

    def __str__(self) -> str:
        tabs = self.level * '\t'
        file_tabs = (self.level + 1) * '\t' 
        value = f'{tabs}- {self.name} (dir)\n'
        for child in self.children_directories:
            value += f'{child}\n'
        for child in self.children_files:
            value += f'{file_tabs}{child}\n'
        return value

    def __repr__(self) -> str:   
        return self.name

class Command:

    def __init__(self, line: str) -> None:
        self.command_type = line.split(' ')[1]
        self.is_change_directory_command = self.command_type == CommandType.CD.value
        self.is_list_command = self.command_type == CommandType.LS.value
        if self.is_change_directory_command:
            self.argument = line.split(' ')[2]

    def change_directory(self, root: Directory):
        if root == None:
            return Directory('/')
        if self.argument == '..':
            return root.parent
        for child in root.children_directories:
            if child.name == self.argument:
                return child

    def list(self, root: Directory):
        return root.children_directories[0]