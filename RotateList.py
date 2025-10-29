def rotate_list(lst, k):
    temp = []
    if len(lst) != 0:
        n = k%len(lst)
        if k == 0:
            return lst
        for i in range(n,0,-1):
            temp.append(lst[len(lst)-i])
        for i in range(len(lst)-(n)):
            temp.append(lst[i])
        
    return temp