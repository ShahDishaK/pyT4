<center><h1> NUMPY EXERCISE </h1></center>

## Create a 1D NumPy array named arr1 with elements [1, 2, 3, 4, 5].

import numpy as np 
arr1=np.array([[1,4,3],[4,5,6]])

## Create a 2D NumPy array named arr2 with elements [[6, 7, 8], [9, 10, 11]].

import numpy as np 
arr2=np.array([[6,7,8],[9,10,11]])

## Perform array indexing to extract the element 4 from arr1 and the element 10 from arr2.

print(arr1[3])
print(arr2[1][1])

## Use array slicing to create a new 1D array slice_arr from arr1 containing elements [2, 3, 4].

slice_arr=arr1[1:4]
print(slice_arr)

## Determine the shape of arr2.

np.shape(arr2)

## Reshape arr1 into a 3x2 array named reshaped_arr.

arr2.reshape(3,2)

## Iterate through the elements of arr2 and print each element.

for i in np.nditer(arr2):
    print(i)

## Use the np.concatenate function to concatenate arr1 and arr2 horizontally into a new array named concatenated_arr.

concatenate_arr=np.concatenate((arr1,arr2),axis=0)
print(concatenate_arr)

## Use the np.array_split function to split concatenated_arr into three equal-sized arrays.

np.array_split(concatenate_arr,3,axis=1)

## Use the np.where function to find the indices of elements in concatenated_arr that are greater than 5.

np.where(concatenate_arr>5)#array and the index of value in array



## Use the np.sort function to sort arr1 in ascending order.

np.sort(arr1)#np.sort(arr1)[::-1]

__.__
<!-- import numpy as np

# 1. Create a 1D array
arr1 = np.array([1, 2, 3, 4, 5])

# 2. Create a 2D array
arr2 = np.array([[6, 7, 8], [9, 10, 11]])

# 3. Array indexing
element_from_arr1 = arr1[3]  # Element: 4
element_from_arr2 = arr2[1, 1]  # Element: 10

# 4. Array slicing
slice_arr = arr1[1:4]  # Elements: [2, 3, 4]

# 5. Determine the shape
shape_of_arr2 = arr2.shape  # Shape: (2, 3)

# 6. Reshape arr1 (using size 5)
reshaped_arr = arr1.reshape(1, 5)  # Reshape to a 1x5 array

# 7. Iteration
for element in np.nditer(arr2):
    print(element)

# 8. Concatenate horizontally after reshaping arr1
reshaped_arr = np.repeat(reshaped_arr, arr2.shape[0], axis=0)  # Repeat rows to match arr2
concatenated_arr = np.concatenate((reshaped_arr, arr2), axis=1)

# 9. Array splitting
split_arrays = np.array_split(concatenated_arr, 3)

# 10. np.where
indices_gt_5 = np.where(concatenated_arr > 5)

# 11. np.sort
sorted_arr1 = np.sort(arr1)

# Display results
print("Element from arr1:", element_from_arr1)
print("Element from arr2:", element_from_arr2)
print("Sliced array:", slice_arr)
print("Shape of arr2:", shape_of_arr2)
print("Reshaped arr1:", reshaped_arr)
print("Concatenated array:", concatenated_arr)
print("Split arrays:", split_arrays)
print("Indices greater than 5:", indices_gt_5)
print("Sorted arr1:", sorted_arr1)
 -->