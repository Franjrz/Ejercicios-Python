def char_freq(message):
    frec = {}
    for char in message:
        frec[char] = frec.get(char, 0) + 1
    return frec