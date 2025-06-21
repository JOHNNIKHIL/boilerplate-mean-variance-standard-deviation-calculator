# mean_var_std.py

import numpy as np

def calculate(input_list):
    """
    Calculate mean, variance, standard deviation, max, min, and sum
    across rows, columns, and the entire 3x3 matrix derived from the input list.

    Parameters:
    -----------
    input_list : list of 9 numerical values
        A flat list of 9 numbers to be reshaped into a 3x3 matrix.

    Returns:
    --------
    dict
        A dictionary with keys: 'mean', 'variance', 'standard deviation', 'max', 'min', 'sum'.
        Each key maps to a list containing:
        [column-wise operation result, row-wise operation result, flattened matrix result]
    """

    # Check that exactly 9 numbers are provided
    if len(input_list) != 9:
        raise ValueError("List must contain nine numbers.")

    # Convert the input list into a 3x3 NumPy array
    matrix = np.array(input_list).reshape(3, 3)

    # Debugging: Uncomment to see the matrix
    # print("Matrix:\n", matrix)

    # Calculate statistics
    calculations = {
        'mean': [
            np.mean(matrix, axis=0).tolist(),        # Column-wise
            np.mean(matrix, axis=1).tolist(),        # Row-wise
            np.mean(matrix).item()                   # Flattened
        ],
        'variance': [
            np.var(matrix, axis=0).tolist(),         # Column-wise
            np.var(matrix, axis=1).tolist(),         # Row-wise
            np.var(matrix).item()                    # Flattened
        ],
        'standard deviation': [
            np.std(matrix, axis=0).tolist(),         # Column-wise
            np.std(matrix, axis=1).tolist(),         # Row-wise
            np.std(matrix).item()                    # Flattened
        ],
        'max': [
            np.max(matrix, axis=0).tolist(),         # Column-wise
            np.max(matrix, axis=1).tolist(),         # Row-wise
            np.max(matrix).item()                    # Flattened
        ],
        'min': [
            np.min(matrix, axis=0).tolist(),         # Column-wise
            np.min(matrix, axis=1).tolist(),         # Row-wise
            np.min(matrix).item()                    # Flattened
        ],
        'sum': [
            np.sum(matrix, axis=0).tolist(),         # Column-wise
            np.sum(matrix, axis=1).tolist(),         # Row-wise
            np.sum(matrix).item()                    # Flattened
        ]
    }

    return calculations
