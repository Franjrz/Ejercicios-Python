from operator import xor
#1 1*4, 2 1*3, 3 1*2, 4 1*1

def check_ship(x,y,field,lon): 
    xm0 = x > 0
    xm9 = x < 9
    xl = lon + x < 11
    ym0 = y > 0
    ym9 = y < 9
    yl = lon + y < 11
    
    if not xl and not yl:
        print(xl, yl)
        print("False porque se pasa de los margenes en " + str([x,y]) + " " + str(lon))
        return False
    
    s = 0
    for i in range(x-1+1*(not xm0),x+2-1*(not xm9)):
        for j in range(y-1+1*(not ym0),y+2-1*(not ym9)):
            s+=field[i][j]
    if s == 1 and lon == 1:
        return True
    
    #vertical
    if xl :
        s = 0
        p = True
        v = True
        print(range(x-1+1*(not xm0),lon+x-1*(not xm9)),range(y-1+1*(not ym0),y+2-1*(not ym9)))
        for i in range(x-1+1*(not xm0),lon+x-1*(not xm9)):
            for j in range(y-1+1*(not ym0),y+2-1*(not ym9)):
                s+=field[i][j]
                if i >= x and i < x+lon and j == y and field[i][j] == 0:
                    p = False
        if s != lon or p == False:
            v = False
    else:
        v = False
    #horizontal
    if yl:
        s = 0
        p = True
        h = True
        print(range(y-1+1*(not ym0),lon+y-1*(not ym9)),range(x-1+1*(not xm0),x+2-1*(not xm9)))
        for i in range(y-1+1*(not ym0),lon+y-1*(not ym9)):
            for j in range(x-1+1*(not xm0),x+2-1*(not xm9)):
                s+=field[j][i]
                if i >= y and i < y+lon and j == x and field[j][i] == 0:
                    p = False
        if s != lon or p == False:
            h = False
    else:
        h = False
    if not xor(v,h):
        print("Print final de detectar en " + str([x,y]) + " " + str(lon) + " " + str([v,h]))
        return False
    return True


def detect_ship(x,y,field,ships):
    l = 0
    for lon in range(4,0, -1):
        if check_ship(x,y,field,lon):
            print("BARCO RECONOCIDO EN " + str(x) + "," + str(y) + " LONGITUD:" + str(lon))
            ships[lon-1] += 1
            l = lon
            break
    
    if ships[0] > 5 or ships[1] > 4 or ships[2] > 3 or ships[3] > 2 or l == 0:
        print("False en " + str([x,y]) + " porque más barcos de la cuenta: " + str(ships[0] > 5) + " " + str(ships[1] > 4) + " " + str(ships[2] > 3) + " " + str(ships[3] > 2) + " " + str(l == 0) + " " + str(ships[0]) + " " + str(ships[1]) + " " + str(ships[2]) + " " + str(ships[3]) + " " + str(l))
        return field, ships, False
    
    #Borrar barco
    else:
        if l == 1:
            field[x][y] = 0
        else:
            if x + lon < 11 and field[x+1][y] == 1:
                for i in range(x,x+lon):
                    field[i][y] = 0
            elif y + lon < 11 and field[x][y+1] == 1:
                for i in range(y,y+lon):
                    field[x][i] = 0 
                    
    for i in field:
        print(i)
    return field, ships, True


def validate_battlefield(field):
    ships = [0,0,0,0]
    for i in range(len(field)):
        for j in range(len(field[i])):
            if field[i][j] == 1:
                field, ships, validate = detect_ship(i,j,field,ships)
                if validate == False:
                    return False
    if ships[0] != 4 or ships[1] != 3 or ships[2] != 2 or ships[3] != 1:
        return False
    return True