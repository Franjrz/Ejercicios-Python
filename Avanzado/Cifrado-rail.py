def encode_rail_fence_cipher(string, n):
    mascara = list(range(1,n+1))+list(range(n-1,1,-1))
    dict_aux = {}
    for i in range(1,n+1):
        dict_aux[i] = []
    for i in range(len(string)):
        dict_aux[mascara[i%(2*n-2)]].append(string[i])
    if type(string) == str:
        salida = ""
    else:
        salida = []
    for i in range(1,n+1):
        if len(string) > 0 and type(string[0]) == int:
            salida.extend(dict_aux[i])
        else:
            salida += ''.join(dict_aux[i])
    return salida
        
def decode_rail_fence_cipher(string, n):
    mascara = encode_rail_fence_cipher([i for i in range(len(string))], n)
    if len(mascara) == 0:
        return ''
    salida = [' ']*len(string)
    for i in range(len(string)):
        salida[mascara[i]] = string[i]
    return ''.join(salida)