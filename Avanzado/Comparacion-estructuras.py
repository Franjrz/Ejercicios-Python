from operator import xor
def check_level(array1,array2):
    is1lst = type(array1) == list
    is2lst = type(array2) == list
    #SON DISTINTOS SI
    #AMBOS SON LISTAS PERO DE DISTINTA LONGITUD
    cl1 = is1lst and is2lst and len(array1) != len(array2)
    #UNO DE ELLOS ES UNA LISTA Y EL OTRO NO
    cl2 = xor(is1lst, is2lst)
    if cl1 or cl2:
        return False
    #AMBOS SON LISTAS VACÍAS
    cl4 = is1lst and is2lst and len(array1) == 0 and len(array2) == 0
    #NINGUNO ES UNA LISTA
    cl5 = not is1lst and not is2lst
    if cl4 or cl5:
        return True
    for i in range(len(array1)):
        if check_level(array1[i],array2[i]) == False:
            return False
    return True

def same_structure_as(original,other):
    return check_level(original,other)