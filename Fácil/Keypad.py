def computer_to_phone(numbers):
    rep = {"7":"1","8":"2","9":"3","1":"7","2":"8","3":"9"}
    numbers = list(numbers)
    for i in range(len(numbers)):
        if numbers[i] in rep.keys():
            numbers[i] = rep[numbers[i]]
    
    return ''.join(numbers)