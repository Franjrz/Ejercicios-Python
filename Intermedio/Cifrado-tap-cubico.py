dict_encode = {}
dict_decode = {}
alphabet = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"," "]
points = [".", "..", "..."]
for i in range(3):
    for j in range(3):
        for k in range(3):
            sample_points = points[k] + " " + points[j] + " " + points[i]
            sample_letter = alphabet[i*9+j*3+k]
            dict_decode[sample_points] = sample_letter
            dict_encode[sample_letter] = sample_points

def encode(string):
    code = ""
    for i in string:
        code += dict_encode[i] + " "
    return code[:-1]


def decode(string):
    code = ""
    string = string.split(" ")
    letra = ""
    for i in range(len(string)):
        if i%3 != 2:
            letra += string[i] + " "
        else:
            letra += string[i]
            code += dict_decode[letra]
            letra = ""
    return code