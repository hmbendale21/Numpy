import numpy as np

# a = np.array([1,2,3,4,5,6,7,8,9,10])
# print(a[1:6])
# print(a[:8])

# 2D slicing 
  
# m = np.array([[45,6,2],[8,6,4],[77,3,5]])
# # print(m[1:3])          # print row
# # print(m[0])

# print(m[:,0])           #print coloumn

# print(m[0:2, 1:3])


# Him = np.array([1,2,5,9,6 , 50 , 20 , 15 , 60 , 90 , 70 , 22 , 13])
# print (Him[Him>3])


# multiple conditions
# print (Him[(Him > 3) &(Him < 20 )])
# print(Him[(Him > 5) | (Him > 30)])

# h = np.array([2,55,46,33,15,45])
# h[h < 30] = -1
# print(h)


# np.where() (CONDITIONAL ASSIGNMENT)

# h = np.array([2,55,46,33,15,45])
# new_array = np.where( h > 30 , 1 , 0)
# print(new_array)

# Fancy indexing (select by index list)
# arr =np.array([1 , 5 , 9 , 6 , 56 , 23])
# print(arr[[1 , 5 , 3 ]])

# arr= np.array([[1 , 5 , 9 , 6 , 3 , 7  , 55 ,69],[ 1 , 2, 7 , 6 , 3 , 1 , 4 ,6]])
# print (arr[[ 0 , 1] ,[0 , 1 ]])

#  COPY vs VIEW (VERY IMPORTANT)

# View
# him = np.array([ 1 , 2  , 3 , 88 , 45 ])
# a = him[1:3]
# him[2] = 50
# print (him)

# Copy
# him = np.array([ 1 , 2  , 3 , 88 , 45 ])
# b=  him[1:5].copy()
# b [2] = 20
# print("b = ", b)
# print("him =", him)

# Q1.From matrix:
# [[1 2 3]
#  [4 5 6]
#  [7 8 9]]
# Select:
# middle row
# last column
# sub-matrix [[2,3],[5,6]]

# h =np.array([[1,2,3] ,[ 4,5,6] , [7,8,9]])
# print(h[1])
# print(h[:,2])
# print(h[0:2,1:3])

#  Q2:From array:
# [5, 12, 25, 7, 30]
# Print values between 10 and 30
# Replace values < 10 with 0

# h = np.array([5, 12, 25, 7, 30])
# print(h[(h>10) & (h<30)])
# h[h<10]= 0
# print(h)

# Use np.where() to mark: 
# values ≥ 20 as 1
# else 0

# a = np.array([2 , 55, 4 , 40 , 556 , 3 ,7])
# h_array = np.where(a >= 20 , 1 , 0)
# print(h_array)














