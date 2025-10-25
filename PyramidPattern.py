def generate_pyramid(n):
    """
    Function to return a pyramid pattern of '*' of side n as a list of strings.
    
    Parameters:
    n (int): The number of rows in the pyramid.
    
    Returns:
    list: A list of strings where each string represents a row of the pyramid.
    """
    pyramid = []
    for i in range(1,n+1):
        stars = "*"*((2*i)-1)
        space = " "*(n-i)
        pyramid.append(space + stars + space)
    return pyramid