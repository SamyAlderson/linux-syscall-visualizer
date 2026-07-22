# main.py
# This is the main entry point for the Linux system call visualizer

import sys
from src.utils import parse_args
from src.syscalls import Visualizer

def main():
    """Run the visualizer"""
    args = parse_args()

    if args.help:
        print("Usage: main.py [options]")
        print("Options:")
        print("  -h, --help    Show this message")
        print("  -i, --input   Specify input file")
        print("  -o, --output  Specify output file")
        sys.exit(0)

    try:
        visualizer = Visualizer(args.input, args.output)
        visualizer.run()
    except FileNotFoundError as e:
        print(f"Error: Input file '{args.input}' not found")
        sys.exit(1)
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
```

```python
# utils.py
# Utility functions for the Linux system call visualizer

import argparse

def parse_args():
    """Parse command line arguments"""
    parser = argparse.ArgumentParser(description="Linux system call visualizer")
    parser.add_argument("-i", "--input", help="Specify input file")
    parser.add_argument("-o", "--output", help="Specify output file")
    parser.add_argument("-h", "--help", action="store_true")
    return parser.parse_args()