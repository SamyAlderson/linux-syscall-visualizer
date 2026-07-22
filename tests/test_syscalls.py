# tests/test_syscalls.py

import unittest
import sys
import subprocess
import os

class TestSyscalls(unittest.TestCase):
    def test_parse_syscall(self):
        # Create a test file with a single syscall
        test_file = "test_syscall.c"
        with open(test_file, "w") as f:
            f.write("#include <linux/syscall.h>\n")
            f.write("int main() { return syscall(SYS_open, \"test.txt\", O_RDWR, 0); }\n")

        # Compile the test file
        try:
            subprocess.check_output(["gcc", "-c", test_file])
        except subprocess.CalledProcessError as e:
            self.fail(f"Compilation failed with error: {e}")

        # Run the test file with objdump
        try:
            subprocess.check_output(["objdump", "-d", test_file + ".o"])
        except subprocess.CalledProcessError as e:
            self.fail(f"objdump failed with error: {e}")

        # Remove the test file
        os.remove(test_file)

    def test_invalid_syscall(self):
        # Create a test file with an invalid syscall
        test_file = "test_syscall_invalid.c"
        with open(test_file, "w") as f:
            f.write("#include <linux/syscall.h>\n")
            f.write("int main() { return syscall(SYS_invalid, \"test.txt\", O_RDWR, 0); }\n")

        # Compile the test file
        try:
            subprocess.check_output(["gcc", "-c", test_file])
        except subprocess.CalledProcessError as e:
            # This should raise an error because SYS_invalid is not a valid syscall
            self.fail(f"Compilation succeeded unexpectedly with error: {e}")

        # Remove the test file
        os.remove(test_file)

    def test_invalid_args(self):
        # Test that an invalid number of arguments raises an error
        try:
            subprocess.check_output(["objdump", "-d", "nonexistent_file.o"])
            self.fail("Expected objdump to fail with error")
        except subprocess.CalledProcessError as e:
            # This should raise an error because nonexistent_file.o does not exist
            self.assertEqual(e.returncode, 1)

if __name__ == "__main__":
    unittest.main()