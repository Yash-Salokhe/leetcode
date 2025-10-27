def generate_diamond(n):
    """
    Function to return a diamond pattern of '*' of side n as a list of strings.
    
    Parameters:
    n (int): The number of rows for the upper part of the diamond.
    
    Returns:
    list: A list of strings where each string represents a row of the diamond.
    """
    diamond_pattern = []
    for i in range(1,n+1):
        diamond_pattern.append(' '*(n-i) + '*'*((2*i)-1)+' '*(n-i))
        
    diamond_pattern.extend(diamond_pattern[-2::-1])
    return diamond_pattern
