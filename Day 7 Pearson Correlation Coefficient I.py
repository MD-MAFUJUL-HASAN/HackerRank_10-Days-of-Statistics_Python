# Enter your code here. Read input from STDIN. Print output to STDOUT

def std(x):
    return (sum([(i-(sum(x))/len(x))**2 for i in x])/len(x))**0.5

N = int(input())
X = list(map(float, input().split()))
Y = list(map(float, input().split()))

X_M = sum(X)/len(X)
Y_M = sum(Y)/len(Y)

X_S = std(X)
Y_S = std(Y)

print(round(sum([(i-X_M)*(j-Y_M) for i, j in zip(X, Y)])/(N*X_S*Y_S), 3))
