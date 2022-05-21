import numpy as np

def slice_y(y, n_slices=10):
    unique_y_value, counts = np.unique(y, return_counts=True)
    cumsum_y = np.cumsum(counts)
    slice_partition = np.hstack((0, cumsum_y))

    n_y_values = unique_y_value.shape[0]
    if n_y_values < n_slices:
        raise ValueError("number of slices should be smaller  than the number of unique values in y")
    elif n_y_values > n_slices:
        raise ValueError("Regression problem not supported yet")

    slice_indicator = np.ones(y.shape[0], dtype=int)
    for j, (start_idx, end_idx) in enumerate(zip(slice_partition, slice_partition[1:])):
        if j == len(slice_partition) - 2:
            slice_indicator[start_idx:] = j
        else:
            slice_indicator[start_idx: end_idx] = j

    slice_counts = np.bincount(slice_indicator)
    return slice_indicator, slice_counts

