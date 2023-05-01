# Multiple Choice Question - No code required but checked with code

# ========================
#         Solution
# ========================

from itertools import product
from fractions import Fraction

P = list(product([1, 2, 3, 4, 5, 6], repeat=2))

N = sum(1 for x, y in P if x + y == 6 and x != y)

print(Fraction(N, len(P)))

#Answer >>> 1/9
