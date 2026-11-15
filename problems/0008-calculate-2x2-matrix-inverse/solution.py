
def inverse_2x2(matrix: list[list[float]]) -> list[list[float]] | None:
    """
    Calculate the inverse of a 2x2 matrix.
    
    Args:
        matrix: A 2x2 matrix represented as [[a, b], [c, d]]
    
    Returns:
        The inverse matrix as a 2x2 list, or None if the matrix is singular
        (i.e., determinant equals zero)
    """
    # Your code here

    if det(matrix)==0:
        return None
    else:
        const = 1/det(matrix)
        const = round(const, 2)
        return [[const*matrix[1][1], -const*matrix[0][1]],[-const*matrix[1][0],const*matrix[0][0]]] 
def det(matrix):
    return matrix[0][0] * matrix[1][1] - matrix[0][1]*matrix[1][0]