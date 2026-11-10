l = [29, 10, 14, 37, 13]
print("Начальный список: ")
print(l)
print()
for i in range(len(l)):
    min=i
    for m in range(i+1,len(l)):
        if l[m]<l[min]:
            min=m
    if min != i:
        l[i],l[min]=l[min],l[i]
    print(l)
    print()
print("Отсортированный список выбором: ")
print(l)