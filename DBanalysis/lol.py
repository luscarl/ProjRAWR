r = 1

def mystery(n,m):
    r = 1
    i = 2
    r = n
    while i <= m:
        r = r*n
        print(r)
        i+=1
    return r

print("answer:" + str(mystery(2,3)))