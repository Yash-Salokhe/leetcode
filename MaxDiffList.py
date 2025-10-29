def max_consecutive_difference(lst):
    maxDiff = 0
    for i in range(len(lst)-1):
        check =abs(lst[i]-lst[i+1])
        if maxDiff< check:
            maxDiff = check
    return maxDiff

lst = [1, 7, 3, 10, 5]
print(max_consecutive_difference(lst))