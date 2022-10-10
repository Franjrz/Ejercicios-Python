def is_valid_walk(walk):
    #determine if walk is valid
    # If there are more or less steps than minutes then is not correct
    time = 10
    if len(walk) != time:
        return False
    # The number of the 'n' steps must be equal to 's' steps. The same for 'e' and 'w'
    pos = 0
    # Due to not waste resources one variable is used to measure the equilibrium both in vertical and horizontal axes
    # But to not avoid to mix both of them, weight of every one is different.

    way = {'n': 1, 's': -1,'e': time, 'w': -time}
  
    for step in walk:
        pos = pos + way[step]
    if pos != 0:
        return False
    return True