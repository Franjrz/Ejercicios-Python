def filter_string(string):
    numbers = []
    for i in string:
        if i in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
            numbers.append(int(i))
    string2 = [str(integer) for integer in numbers]
    string2 = "".join(string2)

    return int(string2)