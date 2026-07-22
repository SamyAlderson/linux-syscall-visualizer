# Linux System Call Visualizer
A simple tool for visualizing Linux system calls

## What it does

This project parses Linux system call events and visualizes them. I needed a simple way to inspect system call behavior and didn't find anything that fit the bill. So, I built this.

## Install

```bash
pip3 install -r requirements.txt
```

## Usage

```bash
./visualizer.py -h
```

This will print a help message with usage instructions. You can also specify a system call log file with the `-l` option.

## Build from source

```bash
git clone https://github.com/SamyAlderson/linux-syscall-visualizer.git
cd linux-syscall-visualizer
python3 setup.py build
```

## Run tests

```bash
python3 -m unittest discover tests
```

## Project structure

* `src/visualizer.py`: System call parser and visualizer
* `tests/test_visualizer.py`: Unit tests for the visualizer
* `tests/test_data/`: Sample system call log files for testing
* `requirements.txt`: Dependencies for running the project
* `setup.py`: Build script for building the project

## License

Copyright (c) 2026 SamyAlderson

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.