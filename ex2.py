s = [2,5,8,11,14,18,21,25,30] 
e = 18
f = 0
l = len(s)-1
i=-1
while f<=l:
    m = (f+l)//2
    if s[m] == e:
        i = m
        break
    elif s[m] < e:
        f = m+1
    else:
        l = m-1
if i == -1:
    print("-1") 
else:
    print("Индекс элемента: ", i)