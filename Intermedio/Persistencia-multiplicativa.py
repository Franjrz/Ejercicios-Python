from functools import reduce

def persistence(n):
    salida = 0;
    while n > 9:
        nd = []
        while n > 9:
            print(n%10)
            nd.append(n%10)
            print(n//10)
            n = n//10
        nd.append(n%10)
        print(nd)
        n = reduce(lambda x, y: x*y, nd)
        salida += 1
    return salida