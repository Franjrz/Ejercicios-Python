import numpy as np

def get_nubers(expr):
    expr = expr[1:]
    aux = []
    i = 0
    while i < len(expr) and not expr[i].isalpha():
        aux.append(expr[i])
        i += 1
    expr = expr[len(aux):]
    if len(aux) == 0:
        a = 1
    elif len(aux) == 1 and aux[0] == '-':
        a = -1
    else:
        a = int(''.join(aux))
    x = expr[0]
    expr = expr[1:]
    aux = []
    i = 0
    while i < len(expr) and expr[i] != ')':
        aux.append(expr[i])
        i += 1
    expr = expr[len(aux):]
    if len(aux) == 0:
        b = 0
    else:
        b = int(''.join(aux))
    expr = expr[2:]
    n = int(expr)
    return a,x,b,n

def fact(n):
    return np.math.factorial(n)

def aoverb(n,k):
    nf = fact(n)
    kf = fact(k)
    nkf = fact(n-k)
    return int(nf/(kf*nkf))

def power(n,m):
    return np.power(n,m)

def get_string(polinomio,x):
    resultado = ""
    for i in range(0,len(polinomio)):
        if polinomio[i] > 0:
            c = '+'+str(polinomio[i])
        elif polinomio[i] == 0:
            c = '+'
        else:
            c = str(polinomio[i])
        if len(polinomio)-1-i == 0:
            monomio = c
        elif len(polinomio)-1-i == 1:
            monomio = c+x
        else:
            monomio = c+x+str('^')+str(len(polinomio)-1-i)
        if i == 0 and c == "+1": 
            monomio = monomio[2:]
        elif i == 0 and c == "-1": 
            monomio = '-'+monomio[2:]
        resultado += monomio
    if resultado[0] == '+':
        resultado = resultado[1:]
    return resultado
    
def expand(expr):
    a,x,b,n = get_nubers(expr)
    if n == 0:
        return "1"
    if n == 1:
        return expr[1:-3]
    if b == 0 and a !=0:
        return expr.split(')')[1][1:]
    polinomio = []
    for i in range(n+1):
        polinomio.append(aoverb(n,i)*power(a,n-i)*power(b,i))
    return get_string(polinomio,x)