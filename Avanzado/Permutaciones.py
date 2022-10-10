def permutations(s):
    if len(s) == 1:
        return [s]
    perm_list_total = []
    for i in range(len(s)):
        perm_list = permutations(s[:i]+s[i+1:])
        for j in range(len(perm_list)):
            perm_list[j] = s[i]+perm_list[j]
        perm_list_total += perm_list
    perm_list_total = list(set(perm_list_total))
    return perm_list_total