import numpy as np

def descriptive_statistics(data: list | np.ndarray) -> dict:
    """
    Calculate various descriptive statistics metrics for a given dataset.
    
    Args:
        data: List or numpy array of numerical values
    
    Returns:
        Dictionary containing mean, median, mode, variance, standard deviation,
        percentiles (25th, 50th, 75th), and interquartile range (IQR)
    """
    # Your code here
    # Convert to NumPy array
    arr = np.array(data, dtype=float)
    
    # Mean
    mean = np.mean(arr)
    
    # Median
    median = np.median(arr)
    
    # Mode (returns smallest mode if multiple)
    seen = {}
    for num in arr: 
        if num not in seen:
            seen[num] = 1
        else:
            seen[num] += 1
    mode = 0
    occ = 0
    for val in seen:
        if seen.get(val) > occ:
            mode = val
            occ = seen.get(val)
        elif seen.get(val) == occ:
            if val < mode:
                mode = val
    mode = int