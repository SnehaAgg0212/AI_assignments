#Find the minimum value of a function y = (x+3)^2. 
# Write a python program to find the minimum value,
# use the numerical method described in this link. 

import math


def gradientDescent(x, alpha, num_iters):
    y_history = [[]*2 ]*num_iters

    for i in range(0, num_iters):
        y = (x+3) ** 2
        y_history[i] = [x,y]
        update = (2*x) + 6
        x = x- (alpha * update)
    return y_history

def minNum(res, num_iters):
    minNo = res[0][1]
    for i in range(1,num_iters-1):
        if (res[i][1])< minNo:
            minNo = res[i][1]
    return minNo

res = gradientDescent(-7, 0.3, 20)
print("Minimum point in y", minNum(res, 20))

    