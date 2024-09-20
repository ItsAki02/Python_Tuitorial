'''Write a Python function histoggram(s) that takes as input a list of integers with repitions and retuns a list of pairs as follows:
-> for each number n that appears in ls, there should be exactly one pair (n,r) in the list returned by the function, where r is the number of repitions of n is ls.
-> he final list shoukd be sorted in ascending order by r, the number of repitions.For numbers that occur with the same number of repitions,arrange the pairs in ascending order of the value of the number.For instances:
1.histogram([13,12,11,13,14,13,7,7,13,14,12])]
Result is [(11,1),(7,2),(12,2),(14,2),(13,4)]'''


def histogram(ls):
    d = {}
    for i in ls:
        if i in d:
            d[i] += 1
        else:
            d[i] = 1
    return sorted(d.items(), key = lambda x : (x[1],x[0]))

print(histogram([13,12,11,12,14,13,7,7,13,14,12]))

