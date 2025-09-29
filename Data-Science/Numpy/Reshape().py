##🔸 What is .reshape()?
# In Python (NumPy), .reshape() is used to change the shape (i.e., number of rows and columns) of an array without changing its data.

import numpy as np

# Step 1: Create a 1D array
arr=np.array([1,2,3,4,5,6,])

# Step 2: Reshape into 2 rows and 3 columns
reshaped_arr=arr.reshape(2,3)


print('Original 1D array: ')
print(arr)


print('\n Reshaped to 2x3: ')
print(reshaped_arr)

##### in reshape -1 means automatic

arr = np.array([10, 20, 30, 40])
print('Automatic')
print(arr.reshape(2, -1))  # Automatically becomes (2, 2)

#.reshape(-1, 1)
# "Reshape the array into a column vector with 1 column and as many rows as needed automatically."

import numpy as np

arr = np.array([10, 20, 30, 40, 50, 60])

reshaped = arr.reshape(-1, 1)

print("Original 1D array shape:", arr.shape)
print("Reshaped shape:", reshaped.shape)
print("\nReshaped array:\n", reshaped)

