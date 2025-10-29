def merge_two_sorted_lists(list1, list2):
    temp = []
    i,j=0,0
    while i < len(list1) and j < len(list2):
        if list1[i] < list2[j]:
            temp.append(list1[i])
            i +=1 
        else:
            temp.append(list2[j])
            j+=1 
            
    while i< len(list1):
        temp.append(list1[i])
        i+=1
        
    while j < len(list2):
        temp.append(list2[j])
        j+=1 

    return temp
        