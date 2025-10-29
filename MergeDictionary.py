def merge_lists_to_dictionary(keys, values):
    merge_dict = {}
    if len(keys)==len(values):
        for i in range(len(values)):
            merge_dict[keys[i]] = values[i]
    else: 
        return False
    return merge_dict