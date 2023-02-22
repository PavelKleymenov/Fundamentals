"""Write a Python program that calculates the area of a circle based on the radius entered by the user."""

from math import pi

import math

r = float(input("Sample radius is: "))

s = pi * math.pow(r, 2)

print(f"The area of a circle with radius {r} is {s}")