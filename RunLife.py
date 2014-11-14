#!/usr/bin/env python3

# ---------------------------
# projects/collatz/RunLife.py
# Copyright (C) 2014
# Glenn P. Downing
# ---------------------------

# -------
# imports
# -------

from sys import stdout
from Life import *

# ---------------------
# Life ConwayCell 21x13
# ---------------------
print("*** Life ConwayCell 21x13 ***")
initial = [['c', 8, 4], ['c', 8, 5], ['c', 8, 6], ['c', 8, 7], ['c', 8, 8], ['c', 9, 7], ['c', 10, 6], ['c', 11, 5], ['c', 12, 4], ['c', 12, 5], ['c', 12, 6], ['c', 12, 7], ['c', 12, 8], ['dim', 21, 13]]
to_print = list(range(1,13))
l = Life(initial)
l.Evolve(12,to_print)

"""
Simulate 12 evolutions.
Print every grid (i.e. 0, 1, 2, 3, ... 12)
"""

# ---------------------
# Life ConwayCell 20x29
# ---------------------

print("*** Life ConwayCell 20x29 ***")
initial2 = [['c', 3, 3], ['c', 3, 4], ['c', 4, 3], ['c', 4, 11], ['c', 4, 12], ['c', 4, 13], ['c', 4, 20], ['c', 4, 21], ['c', 4, 22], ['c', 4, 23], ['c', 11, 4], ['c', 11, 11], ['c', 11, 21], ['c', 12, 4], ['c', 12, 5], ['c', 12, 11], ['c', 12, 12], ['c', 12, 13], ['c', 12, 20], ['c', 12, 21], ['c', 12, 22], ['c', 13, 5], ['dim', 20, 29]]
to_print2 = list(range(0,29,4))
l2 = Life(initial2)
l2.Evolve(28,to_print2)
"""
Simulate 28 evolutions.
Print every 4th grid (i.e. 0, 4, 8, ... 28)
"""

# ----------------------
# Life ConwayCell 109x69
# ----------------------

print("*** Life ConwayCell 109x69 ***")
initial3 = [['c', 34, 34], ['c', 35, 34], ['c', 36, 34], ['c', 37, 34], ['c', 38, 34], ['c', 40, 34], ['c', 41, 34], ['c', 42, 34], ['c', 43, 34], ['c', 44, 34], ['c', 46, 34], ['c', 47, 34], ['c', 48, 34], ['c', 49, 34], ['c', 50, 34], ['c', 52, 34], ['c', 53, 34], ['c', 54, 34], ['c', 55, 34], ['c', 56, 34], ['c', 58, 34], ['c', 59, 34], ['c', 60, 34], ['c', 61, 34], ['c', 62, 34], ['c', 64, 34], ['c', 65, 34], ['c', 66, 34], ['c', 67, 34], ['c', 68, 34], ['c', 70, 34], ['c', 71, 34], ['c', 72, 34], ['c', 73, 34], ['c', 74, 34], ['dim', 109, 69]]
to_print3 = [0,1,2,3,4,5,6,7,8,9,283,323,2500]
l3 = Life(initial3)
l3.Evolve(2500, to_print3)
"""
Simulate 283 evolutions.
Print the first 10 grids (i.e. 0, 1, 2...9).
Print the 283rd grid.
Simulate 40 evolutions.
Print the 323rd grid.
Simulate 2177 evolutions.
Print the 2500th grid.
"""

# ----------------------
# Life FredkinCell 20x20
# ----------------------

print("*** Life FredkinCell 20x20 ****")
initial4 = [['f', 9, 9], ['f', 9, 10], ['c', 10, 11], ['f', 10, 9], ['f', 10, 10], ['dim', 20, 20]]
to_print4 = [1,2,3,4,5]
l4 = Life(initial4)
l4.Evolve(5,[1,2,3,4,5])
"""
Simulate 5 evolutions.
Print every grid (i.e. 0, 1, 2, ..., 5)
"""
