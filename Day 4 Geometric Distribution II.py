# Enter your code here. Read input from STDIN. Print output to STDOUT

ans = 0
p = 1 / 3
for i in range(1, 6):
    ans += (1-p)**(i-1) * p
print(round(ans, 3))
