import math
def solve(m):
    # your code
    # sum n from 1 to inf of n*x**n = x/(x-1)**2 = m
    # x = - (-2*m + sqrt(4*m + 1) - 1)/(2*m)
    return - (-2*m + math.sqrt(4*m+1)-1)/(2*m)