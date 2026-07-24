# Linux System Call Visualizer
A simple visualizer for Linux system calls

## What it does

This project provides a basic visual representation of Linux system calls, allowing you to see what happens under the hood when your program interacts with the kernel.

It exists because I wanted to better understand the system call interface and see how my programs interact with the kernel.

## Install

You can install it via pip with:
```bash
pip install linux-syscall-visualizer
```

## Usage

To use it, simply run:
```bash
linux-syscall-visualizer
```
This will display a simple graph showing system calls made by your program.

## Build from source

To build from source, clone this repository and run:
```bash
python setup.py build
```
Then, you can install it with:
```bash
pip install .
```

## Tests

To run the tests, use:
```bash
python -m unittest tests
```
This will run all the unit tests in the `tests` directory.

## Project Structure

* `linux_syscall_visualizer.py`: the main program
* `tests.py`: the test suite
* `setup.py`: the build script
* `README.md`: this file
* `LICENSE`: the license file

## License

Copyright (c) 2026 SamyAlderson

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.