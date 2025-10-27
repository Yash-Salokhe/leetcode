def generate_hollow_right_angled_triangle(n):
    """
    Function to return a hollow right-angled triangle of '*' of side n as a list of strings.
    
    Parameters:
    n (int): The height of the triangle.
    
    Returns:
    list: A list of strings where each string represents a row of the triangle.
    """
    result = []
    for i in range(1,n+1):
        if i<=2 or i ==n:
            result.append("*"*i)
        else:
            result.append("*" + " "*(i-2) + "*")        
    return result  
