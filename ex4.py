l = [12, 4, 9, 1, 6, 3]
print("Иcходный список:")
print(l)
def merge_sort(l):
    if len(l) <=1:
        return l
    mid = len(l) // 2
    left = merge_sort(l[:mid])
    right = merge_sort(l[mid:])
    return merge(left,right)
def merge(left,right):
    sl = []
    i=j=0
    while i<len(left) and j<len(right):
        if left[i] < right[j]:
            sl.append(left[i])
            i +=1
        else:
            sl.append(right[j])
            j +=1
    sl.extend(left[i:])
    sl.extend(right[j:])
    return sl
print("Отсортированный список:")
print(merge_sort(l))