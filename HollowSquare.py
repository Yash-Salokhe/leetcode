def generate_hollow_square(n):
    """
    Function to return a hollow square pattern of '*' of side n as a list of strings.
    
    Parameters:
    n (int): The size of the square.
    
    Returns:
    list: A list of strings where each string represents a row of the hollow square.
    """ 
    
    result = []
    for i in range(n):
        if i == 0 or i == n-1:
            result.append('*'*n)
        else:
            result.append('*' + ' ' * (n - 2) + '*')
    return result



