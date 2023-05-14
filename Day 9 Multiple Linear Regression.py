# Enter your code here. Read input from STDIN. Print output to STDOUT

from sklearn import linear_model

M, N = list(map(int, input().strip().split()))
X = [0]*N
Y = [0]*N

for i in range(N):
    inp = list(map(float, input().strip().split()))
    X[i] = inp[:-1]
    Y[i] = inp[-1]

LM = linear_model.LinearRegression()
LM.fit(X, Y)
A = LM.intercept_
B = LM.coef_

Q = int(input())

for i in range(Q):
    f = list(map(float, input().strip().split()))
    Y = A + sum([B[j] * f[j] for j in range(M)])
    print(round(Y, 2))
