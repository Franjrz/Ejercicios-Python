a = [['I','V'],['X','L'],['C','D'],['M']]
def solution(n):
    solu = ""
    n = [int(d) for d in str(n)]
    n = n[::-1]
    for i in range(len(n)):
        if n[i] < 4:
            solu = a[i][0]*n[i] + solu
        elif n[i] == 4:
            solu = a[i][0]+a[i][1] + solu
        elif n[i] < 9:
            solu = a[i][1]+a[i][0]*(n[i]-5) + solu
        elif n[i] == 9:
            solu = a[i][0]+a[i+1][0] + solu
    return solu