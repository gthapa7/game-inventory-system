# ✅ 1. Importing and Creating Arrays
# Import NumPy and create a 1D array with values from 0 to 9.

# arr = np.arange(10)
# print(arr)


# Create a 3x3 NumPy array with all True values.
# arr = np.full((3,3),True)
# print(arr)


# Create an array of 10 zeros, and then change the fifth value to 1.
# arr = np.zeros(10)
# arr[4] = 1
# print(arr)


# Create an array of even numbers from 2 to 20.
# arr = np.arange(2,20,2)
# print(arr)

# ✅ 2. Array Operations
# Multiply each element of a 1D array [1, 2, 3, 4] by 2.
# arr = np.array([1, 2, 3, 4])
# result = arr * 2
# print(result)



# Add two arrays: [1, 2, 3] and [4, 5, 6].
# arr1 = np.array([1,2,3])
# arr2 = np.array([4,5,6])
# sum = arr1 + arr2
# print(sum)


# Square every element in the array [1, 2, 3, 4, 5]
# num = np.array([1, 2, 3, 4, 5])
# sqaure = num ** 2
# print(sqaure)
# Calculate the mean, median, and standard deviation of the array [10, 20, 30, 40, 50].
# num = np.array([10, 20, 30, 40, 50])
# mean = np.mean(num)
# median = np.median(num)
# standard_deviation = np.std(num)

# print("mean : ", mean)
# print("median", median)
# print("standard deviation", standard_deviation)

# ✅ 3. Indexing and Slicing
# Extract the third element from the array [5, 10, 15, 20, 25].


# Slice the array [0, 1, 2, 3, 4, 5] to get [2, 3, 4].

# Replace the last element of an array with 100.

# ✅ 4. Shape and Reshape
# Create a 1D array of numbers 0 to 11 and reshape it into a 3x4 matrix.

# What is the shape of np.array([[1,2],[3,4],[5,6]])?

# Flatten a 2D array into 1D.

# ✅ 5. Logical Operations
# Find all elements greater than 10 in the array [4, 12, 15, 7, 9].

# Replace all even numbers in the array [1,2,3,4,5,6] with 0.

# ✅ 6. Random and Linspace
# Create an array of 5 random integers between 1 and 10.

# Create a linearly spaced array of 5 numbers between 0 and 1.

# Generate a 2x3 array of random floats between 0 and 1.

# ✅ 7. Copying and Identity
# Show the difference between a view and a copy using an example.

# Create a 3x3 identity matrix.


# ✅ 1. From Lists: np.array(lst)
# Convert the list [1, 2, 3] into a NumPy array.
# lst = [1,2,3]
# lst1= np.array(lst)
# print(lst1)

# Create a 2D array from the list [[4, 5], [6, 7]].
# lst = [[4, 5], [6, 7]]
# lst1 = np.array(lst)
# print(lst1)

# Make a NumPy array from a tuple (10, 20, 30).
# tup = (10,20,30)
# arr = np.array(tup)
# print(arr)


# # Convert a nested list [[1, 2, 3], [4, 5, 6]] into an array.
# lst = [[1, 2, 3], [4, 5, 6]]
# lst1 = np.array(lst)
# print(lst1)

# What will be the shape of the array created from [[1], [2], [3]]?
# lst = [[1], [2], [3]]
# lst1 = np.array(lst)
# print(lst1)
# ✅ 2. Empty Array: np.array([])
# Create an empty NumPy array.
# arr = np.array([])
# print(arr)


# What is the data type of np.array([]) by default?

# Check the shape of np.array([]).

# Is np.array([]).size equal to 0?

# Convert an empty array to a list and print it.

# # ✅ 3. Ranges: np.arange(start, stop)
# # Create an array of numbers from 0 to 9.
# arr = np.arange(0,10)
# print(arr)
# # Generate an array from 5 to 14.
# arr = np.arange(5,15)
# print(arr)
# # Create an array from 10 to 20 with step size 2.
# arr = np.arange(10,22,2)
# print(arr)
# # What does np.arange(1, 1) return?
# arr = np.arange(1,1)
# print(arr)
# # Predict the output of np.arange(2, 10, 3).
# arr = np.arange(2,10,3)
# print(arr)
# ✅ 4. Constant Values
# a. Zeros: np.zeros((rows, cols))
# # Create a 3x2 array filled with zeros.
# arr = np.zeros((3,2))
# print(arr)
# # What is the shape of np.zeros((4,))?
# arr = np.zeros((4,))
# print(arr)
# # Create a 1x5 array of zeros.
# arr = np.zeros((1,5))
# print(arr)
# # Change the data type to int in a zero array.
# arr = np.zeros(5, dtype = int)
# print(arr)

# arr = np.zeros(5)
# arr = arr.astype(int)
# print(arr)

# # What is the sum of all elements in np.zeros((2, 3))?
# arr = np.zeros((2,3))
# print(np.sum(arr))

# arr = np.zeros((2,3))
# arr1 = np.sum(arr)
# print(arr1)


# ## b. Ones: np.ones((rows, cols))
# # Create a 2x3 array of ones.
# arr = np.ones((2,3))
# print(arr)



# # Multiply a ones array by 5. What do you get?
# arr = np.ones((2,3))
# product = arr * 5
# print(product)

# # Convert a ones array to integer type.
# arr = np.ones(5,dtype = int)
# print(arr)

# arr = np.ones(5)
# arr = arr.astype(int)
# print(arr)
# arr = np.ones((5,3), dtype = int)
# print(arr)

# # What’s the shape of np.ones((1, 4))?
# arr = np.ones((1,4))
# print(arr)
# Add a ones array to a zeros array of the same shape.
# arr1 = np.ones(((2,3)))
# arr2 = np.zeros((2,3))

# arr = np.add(arr1,arr2)
# print(arr)

# arrs = arr1 + arr2
# print(arrs)
# ✅ 5. Identity Matrix: np.eye(n)
# Create a 3x3 identity matrix.

# What does np.eye(4)[2] return?

# What is the trace (sum of diagonals) of np.eye(5)?

# Is np.eye(3).T the same as np.eye(3)?

# Use np.eye(n) to create a 4x4 matrix and multiply it by 3.

# ✅ 6. Diagonal: np.diag([elements])
# Create a diagonal matrix with [1, 2, 3] on the diagonal.

# Extract the diagonal from a 2D array.

# Create a diagonal matrix with values [4, 5, 6, 7].

# Use np.diag() to form a matrix and then find its trace.

# What does np.diag([10, 20], k=1) do?

# ✅ 7. Even Spacing: np.linspace(start, stop, num=n)
# Create 5 evenly spaced numbers from 0 to 10.

# What does np.linspace(1, 2, 3) return?

# Generate 10 numbers between -1 and 1.

# What is the spacing between elements in np.linspace(0, 1, 5)?

# Use np.linspace() to create 4 numbers from 2 to 8, and reshape them to (2, 2).


import numpy as np


arr = np.array([
    [46, 30,  8, 49, 66, 58],
    [87, 32, 40, 42, 45, 33],
    [32, 28,  3, 79, 98, 95],
    [57, 50, 17, 81, 89, 73],
    [59, 48, 76, 23, 94, 22]
])

# Get the element at the 2nd row, 3rd column.

arr[1,2]
print(arr[1,2])

# 40

# Get the last element of the last row.
print(arr[4,5])
# arr[4, 5] or arr[-1, -1]

# Get the entire 3rd row.
print(arr[2,:])
# arr[2, :]

# Get the entire 2nd column.
print(arr[:,1])
# arr[:, 1]

# Get a subarray of the top-left 2x3 block.
# (First 2 rows and first 3 columns)
print(arr[0:2,0:3])
# arr[0:2, 0:3]

# Get a subarray of the center 3x2 block.
# (Rows 1 to 3, Columns 2 to 3)
print
# arr[1:4, 2:4]

# Get every element in the last column.

# arr[:, -1]

# Get the diagonal elements (top-left to bottom-right).

# np.diag(arr)

# Get all rows where the first column is greater than 50.

# arr[arr[:, 0] > 50]

# Get a reversed version of the array row-wise.

# arr[::-1, :]

