def generate_hollow_inverted_right_angled_triangle(n):
    """
    Function to return a hollow inverted right-angled triangle of '*' of side n as a list of strings.
    
    Parameters:
    n (int): The height of the triangle.
    
    Returns:
    list: A list of strings where each string represents a row of the triangle.
    """
    result = []
    for i in range(n,0,-1):
        if i==n or i<=2:
            result.append("*"*i)
        else:
            result.append("*"+" "*(i-2)+ "*")
    
    return result