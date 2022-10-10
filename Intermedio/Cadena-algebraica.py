import numpy

def sum_prod(strexpression):
    strexpression = strexpression.split('+')
    total = 0
    for elem in strexpression:
        total += numpy.prod(list(map(float,elem.split('*'))))
    return "{:.5e}".format(total)