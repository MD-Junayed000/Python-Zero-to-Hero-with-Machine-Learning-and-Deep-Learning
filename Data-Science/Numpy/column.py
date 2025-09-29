
#### For 1D Array

arr =      [10, 20, 30, 40, 50]
# Indexes:  0   1   2   3   4

print(arr[2:3])

# Starts at index 2, ends just before index 3
#
# Includes only the element at index 2

print(arr[2:6])

#Starts from the beginning (index 0), ends just before index 3

print('Includes index 0, 1, 2: ',arr[:3])

print('tarts at index 1, goes to the end',arr[1:])

#arr[start : end : step]

print('Starts at index 0, ends before index 5, and skips every 2nd element: ' , arr[0:5:2])

### For 2D Array

import numpy as np

arr = np.array([[10, 20, 30],
                [40, 50, 60],
                [70, 80, 90]])

# 🔸 1. arr[2:3]
# This slices rows, like in a list.
#
# From row 2 to before row 3 → only row 2.


print('Take specific row:' ,arr[2:3])

# 🔸 2. arr[:3]
# Again slicing rows

# From start to row 3 (exclusive) → rows 0, 1, and 2


###### What about selecting columns

print('arr[row_slice, col_slice]:\n', arr[0:2, 1:3])
















