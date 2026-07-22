# src/syscalls.py
"""
System call parser and visualizer.

This module takes in a list of system calls and returns a parsed representation.
It's used to visualize the system calls.
"""

import re

class SystemCallParser:
    def __init__(self, syscall_list):
        self.syscall_list = syscall_list

    def parse_syscalls(self):
        """
        Parse system call list and return a list of tuples (syscall_name, args).
        """
        syscall_pattern = r"^(\w+)\((.*)\)$"
        parsed_syscalls = []

        for syscall in self.syscall_list:
            match = re.match(syscall_pattern, syscall)
            if match:
                syscall_name = match.group(1)
                args = match.group(2).split(',')
                # Strip leading/trailing whitespaces from args
                args = [arg.strip() for arg in args]
                parsed_syscalls.append((syscall_name, args))
            else:
                raise ValueError(f"Invalid syscall format: {syscall}")

        return parsed_syscalls

class SystemCallVisualizer:
    def __init__(self, parsed_syscalls):
        self.parsed_syscalls = parsed_syscalls

    def visualize_syscalls(self):
        """
        Visualize system call list and return a string representation.
        """
        visualized_syscalls = []

        for syscall_name, args in self.parsed_syscalls:
            visualized_syscalls.append(f"{syscall_name}({', '.join(args)})")

        return '\n'.join(visualized_syscalls)

def load_syscalls_from_string(syscall_str):
    """
    Load system call list from a string.
    """
    syscall_list = [syscall.strip() for syscall in syscall_str.split('\n') if syscall]
    return syscall_list

def get_syscalls_from_file(file_path):
    """
    Load system call list from a file.
    """
    with open(file_path, 'r') as file:
        syscall_str = file.read()
    return load_syscalls_from_string(syscall_str)

def main(syscall_str=None, file_path=None):
    """
    Main entry point for system call parser and visualizer.
    """
    if syscall_str is None and file_path is None:
        raise ValueError("Either syscall_str or file_path must be provided")

    if syscall_str:
        syscall_list = load_syscalls_from_string(syscall_str)
    elif file_path:
        syscall_list = get_syscalls_from_file(file_path)

    parser = SystemCallParser(syscall_list)
    parsed_syscalls = parser.parse_syscalls()
    visualizer = SystemCallVisualizer(parsed_syscalls)
    visualized_syscalls = visualizer.visualize_syscalls()

    print(visualized_syscalls)

if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1:
        main(file_path=sys.argv[1])
    else:
        main()