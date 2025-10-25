def generate_number_triangle(n):
    """
    Function to return a right-angled triangle of repeated numbers of side n as a list of strings.
    
    Parameters:
    n (int): The height of the triangle.
    
    Returns:
    list: A list of strings where each string represents a row of the triangle.
    """
    rat_numbers = []
    for i in range(1,n+1):
        rat_numbers.append(str(i)*i)
    return rat_numbers