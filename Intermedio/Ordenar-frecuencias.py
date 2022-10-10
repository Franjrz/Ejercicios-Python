def solve(arr):
    frecuency = {}
    for i in arr:
        if i in frecuency.keys():
            frecuency[i] += 1
        else:
            frecuency[i] = 1
    
    temp = {}
    
    for key, value in frecuency.items():
        if value in temp.keys():
            temp[value] += [key]
        else:
            temp[value] = [key]
    
    temp = list(temp.items())
    temp.sort(key=lambda row: (row[0]), reverse=True)
    final = []
    
    for item in temp:
        item[1].sort()
        for elem in item[1]:
            final += [elem]*item[0]
    
    return final