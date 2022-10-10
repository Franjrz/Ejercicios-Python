def pattern(n):
    string = ""
    for i in range(1, n+1, 2):
        string += str(i)*i+"\n"
    return string[:-1]