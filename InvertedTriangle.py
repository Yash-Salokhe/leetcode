def generate_inverted_triangle(n):
    """
    Function to return an inverted right-angled triangle of '*' of side n as a list of strings.
    
    Parameters:
    n (int): The height and base of the triangle.
    
    Returns:
    list: A list of strings where each string represents a row of the triangle.
    """
    inverted_traingle = []
    while(n>0):
        inverted_traingle.append("*"*n)
        n=n-1
    return inverted_traingle
