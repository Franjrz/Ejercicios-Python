def order_word(s):
    if type(s) == type("") and len(s) > 0: 
        return ''.join(sorted(s))
    else:
        return 'Invalid String!'