cmake_minimum_required(VERSION 3.10 FATAL_ERROR)
project(linux-syscall-visualizer)

# Check for required dependencies
find_package(Python 3.8 REQUIRED)
find_package(pybind11 2.6 REQUIRED)

# Set up Python package configuration
pybind11_add_module(syscalls src/syscalls.cpp)
pybind11_add_module(utils src/utils.cpp)

# Build main executable
add_executable(main src/main.py)

# Add install target
install(TARGETS main DESTINATION bin)
install(DIRECTORY ${CMAKE_CURRENT_SOURCE_DIR}/src DESTINATION share)