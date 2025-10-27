def generate_floyds_triangle(n):
    """
    Function to return the first n rows of Floyd's Triangle as a list of strings.
    
    Parameters:
    n (int): The number of rows in the triangle.
    
    Returns:
    list: A list of strings where each string represents a row of Floyd's Triangle.
    """
    floyd_triangle = []        
    floyd_number = 0
    for i in range(1,n+1):
        floyd_triangle.append(' '.join(str(floyd_number+j) for j in range(1,i+1)))
        floyd_number += i
    return floyd_triangle
