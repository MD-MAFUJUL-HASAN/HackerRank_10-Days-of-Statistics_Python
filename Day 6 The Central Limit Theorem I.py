# Enter your code here. Read input from STDIN. Print output to STDOUT

import math

H = int(input())
B = int(input())
C = int(input())
INPUT = math.sqrt(B) * int(input())

print(round(0.5 * (1 + math.erf((H - (B * C)) / (INPUT * math.sqrt(2)))), 4))
