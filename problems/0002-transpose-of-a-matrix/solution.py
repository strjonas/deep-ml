import numpy as np
def transpose_matrix(a: list[list[int|float]]) -> list[list[int|float]]:
    """
    Transpose a 2D matrix by swapping rows and columns.
    
    Args:
        a: A 2D matrix of shape (m, n)
    
    Returns:
        The transposed matrix of shape (n, m)
    """
    # Your code here
    a = np.array(a)
    
    #np.transpose(a) # too simple 
    
    s = a.shape
    b = np.zeros((s[1], s[0]))
    # or manually 
    for i, x in enumerate(a):
        for j, y in enumerate(x):
            b[j][i] = y

    return b
