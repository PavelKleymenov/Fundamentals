"""Write a Python program to find out what version of Python you are using"""
import sys

print (f"You are using this version {sys. version} {sys. version_info}")

# Another way to solve this problem is as follows

import platform

print(platform.python_version ())