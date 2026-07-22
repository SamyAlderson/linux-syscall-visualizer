# src/utils.py

import logging
import os

def get_syscall_dir():
    """Return the directory containing the system call binary."""
    return os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def get_syscall_path():
    """Return the path to the system call binary."""
    return os.path.join(get_syscall_dir(), 'syscall.bin')

def load_syscall_data():
    """Load the system call data from the binary file."""
    try:
        with open(get_syscall_path(), 'rb') as f:
            return f.read()
    except FileNotFoundError:
        logging.error('System call binary not found')
        raise
```

```python
# setup.py

import setuptools
from setuptools import find_packages

setuptools.setup(
    name='linux-syscall-visualizer',
    version='1.0',
    packages=find_packages(),
    install_requires=['pybind11>=2.6', 'cmake>=3.10'],
    setup_requires=['pybind11>=2.6', 'cmake>=3.10'],
    entry_points={
        'console_scripts': ['syscall-visualizer=main:main'],
    },
)