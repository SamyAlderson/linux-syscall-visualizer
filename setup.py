from setuptools import setup, find_packages

def read_file(filename):
    """Read the contents of a file into a string."""
    with open(filename, 'r') as f:
        return f.read()

def get_long_description():
    """Get the long description from README.md."""
    return read_file('README.md')

def get_requirements(filename):
    """Get the dependencies from a file."""
    with open(filename, 'r') as f:
        return [line.strip() for line in f.readlines() if line.strip() and not line.startswith('#')]

def get_keywords(filename):
    """Get the keywords from a file."""
    with open(filename, 'r') as f:
        return [line.strip() for line in f.readlines() if line.strip() and not line.startswith('#')][0].split(',')

setup(
    name='linux-syscall-visualizer',
    version='1.0',
    description='A simple visualizer for Linux system calls',
    long_description=get_long_description(),
    long_description_content_type='text/markdown',
    author='Samy Alderson',
    author_email='samy.alderson@example.com',
    url='https://example.com/linux-syscall-visualizer',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    install_requires=get_requirements('pyproject.toml'),
    extras_require={
        'dev': get_requirements('pyproject.toml'),
    },
    keywords=get_keywords('pyproject.toml'),
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
    ],
    project_urls={
        'Documentation': 'https://example.com/linux-syscall-visualizer/docs',
        'Source Code': 'https://example.com/linux-syscall-visualizer',
        'Tracker': 'https://example.com/linux-syscall-visualizer/issues',
    },
    python_requires='>=3.7',
)