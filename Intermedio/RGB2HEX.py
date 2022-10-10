def channel2hex(c):
    if c <= 0:
        return "00"
    if c >= 255:
        return "FF"
    hex = ["0","1","2","3","4","5","6","7","8","9","A","B","C","D","E","F"]
    first = c//16
    second = c-first*16
    return hex[first]+hex[second]

def rgb(r, g, b):
    return channel2hex(r) + channel2hex(g) + channel2hex(b)