# -*- coding: utf-8 -*-
"""Untitled9.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1z1hlX6NKrILZTRb-yKcXClCWMjUPUmyC
"""

import math
print(math.pow(9,3))

from itertools import count
for number in count(start=5, step=3):
  if number > 10:
    break
  print(number)

x = range(3,10)
for n in x:
  print(n)

import decimal
float_division = 22/7
decimal_devision=decimal.Decimal(22)/decimal.Decimal(7)
print("Result for float division of 4 by 3:")
print(float_division)
print("Result for decimal division of 4 by 3:")
print(decimal_devision)

from fractions import Fraction
print(Fraction(84,21))
print(Fraction(81,7))
print(Fraction(23,17))

import decimal
from decimal import Decimal
x = Decimal('0.8')
y = Decimal('0.9')
z = Decimal('0.7')
s = x+y+z
print(s)