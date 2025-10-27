def generate_sandglass(n):
    """
    Function to return a sandglass pattern of '*' of side n as a list of strings.
    
    Parameters:
    n (int): The height of the sandglass.
    
    Returns:
    list: A list of strings where each string represents a row of the sandglass pattern.
    """
    result = []
    for i in range(n,0, -1):
        result.append(" "*(n-i) + "*"* ((2*i)-1)+ " "*(n-i))
        
    result.extend(result[-2::-1])
    return result


print(generate_sandglass(5))