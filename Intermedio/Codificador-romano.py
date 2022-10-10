a = [['I','V'],['X','L'],['C','D'],['M']]
def solution(n):
    sol = ""
    n = [int(d) for d in str(n)]
    n = n[::-1]
    for i in range(len(n)):
        if n[i] < 4:
            sol = a[i][0]*n[i] + sol
        elif n[i] == 4:
            sol = a[i][0]+a[i][1] + sol
        elif n[i] < 9:
            sol = a[i][1]+a[i][0]*(n[i]-5) + sol
        elif n[i] == 9:
            sol = a[i][0]+a[i+1][0] + sol
    return sol