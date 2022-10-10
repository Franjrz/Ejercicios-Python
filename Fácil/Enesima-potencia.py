import math
def index(array, n):
    if len(array) <= n:
        return -1
    else:
        return math.pow(array[n],n)