def quick_sort(ls):
    if len(ls) <= 1:
        return ls
    else:
        pivot = ls.pop(0)
        left = [x for x in ls if x < pivot]
        right = [x for x in ls if x >= pivot]
        
        return quick_sort(left) + [pivot] + quick_sort(right)


test = [3,7,88,5,3,99,54,4]

print(quick_sort(test))