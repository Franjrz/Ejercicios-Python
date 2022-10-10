import numpy as np

def get_generation(cells, generation):
    for population in range(generation):
        cells2 = [0 for j in range(0, len(cells))]
        for i in range(len(cells)):
            cells2[i] = [0 for j in range(0, len(cells[i]))]
        for i in range(len(cells)):
            for j in range(len(cells[0])):
                lista1 = [i-1,i,i+1]
                if lista1[-1] == len(cells):
                    lista1[-1] = 0
                lista2 = [j-1,j,j+1]
                if lista2[-1] == len(cells[0]):
                    lista2[-1] = 0
                suma = 0
                for k in lista1:
                    for l in lista2:
                        suma += cells[k][l]
                suma -= cells[i][j]
                if (cells[i][j] == 1 and (suma != 2 and suma != 3)) or (cells[i][j] == 0 and suma != 3):
                    cells2[i][j] = 0
                elif (cells[i][j] == 1 and (suma == 2 or suma == 3)) or (cells[i][j] == 0 and suma == 3):
                    cells2[i][j] = 1
        cells = cells2
    return cells