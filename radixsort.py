test = [57,134,622,73,8,412,65,712,899,749,561,921,717,570,44,444,754,3,12,522,322,6,0,100,999,8]


def radix_sort(ls, max_digits):
    #base case
    bucket = [ [] for i in range(10) ]
    digit = 1
    for i in range(max_digits):
        for j in range(len(ls)):
            sig = ls[j]
            bucket[sig%10].append(ls[j])
            
