def merge(ls1,ls2):
    results = []

    while ls1 and ls2:
        if ls1[0] > ls2[0]:
            results.append(ls2.pop(0))
        else:
            results.append(ls1.pop(0))
    
    return results+ls1+ls2


def merge_sort(ls):
    if len(ls) <= 1:
        return ls
    else:
        mid = len(ls)//2
        left = merge_sort(ls[:mid])
        right = merge_sort(ls[mid:])
        
        return merge(left,right)


test = [2,78,6,97, 3, 4, 44]

print(merge_sort(test))