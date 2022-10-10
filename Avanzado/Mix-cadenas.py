from collections import defaultdict

def fun(str):
    return (ord(str[0]), ord(str[2]))

def divideList(lst):
    group_by_len = defaultdict(list)
    for ele in lst:
        group_by_len[len(ele)].append(ele)
         
    res = []
    for key in sorted(group_by_len):
        group_by_len[key].sort(key = fun)
        res.append(group_by_len[key])
    res.reverse()
    return res

def coutLower(s):
    times = [0]*26
    for letter in list(s):
        if letter.isalpha() and letter.islower():
            times[ord(letter)-97] += 1
    return times

def mix(s1, s2):
    timess1 = coutLower(s1)
    timess2 = coutLower(s2)
    num = ['1', '2','=']
    times = list(set([(max(timess1[t],timess2[t]) > 1)*(num[0]*(timess1[t]>timess2[t])+num[1]*(timess1[t]<timess2[t])+num[2]*(timess1[t]==timess2[t])+':'+chr(t+97)*max(timess1[t],timess2[t])) for t in range(len(timess1))]))
    times.remove('')
    times = divideList(times)
    times = [item for sublist in times for item in sublist]
    times = '/'.join(times)
    return times