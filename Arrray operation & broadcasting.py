import numpy as np

# a = np.array([1, 5, 33 , 46 , 85])
# b = np.array([55 , 65 , 22 , 78 , 2])
# print(a+b)
# print(a-b)
# print(a*b)
# print(a/b)


# Array + scaler

# a = np.array ([2,5,7,9])
# print(a+2)
# print(a-1)
# print(a*2)
# print(a/2)

# Broadcasting
#  1D + scaler

# arr = np.array([2,4,6,8,10])
# print(arr+5)


# 2D + scaler

# mat =np.array([[2 , 5 , 8],[3 , 6  , 9]])
# print(mat+5)

# COMPARISON OPERATIONS

# arr = np.array([10,20,30,90])
# print(arr>20)


# arr = np.array([10,20,30,90]) 
# a = arr > 25
# print(arr[a])

# print(arr[arr>25])   ...shortcut


# MODIFY ARRAY USING CONDITIONS

# arr = np.array([10,20,30,90]) 
# arr[arr<25] = 0
# print(arr)

# MATHEMATICAL FUNCTIONS (INTRO)

# a  = np.array([10, 50 , 90])
# print(np.sum(a))
# print(np.max(a))
# print(np.min(a))
# print(np.mean(a))
# print(np.median(a))


# 1. Create array: [5, 10, 15, 20] Add 5 to each element.

# a = np.array([5 , 10, 15 , 20])
# print(a+5)


# 2. From array: [10, 25, 30, 5, 40] Print only values greater than 20.

# a = np.array([10, 25, 30, 5, 40])
# print(a[a>20])

# 3. Replace all values less than 15 with 0.

a = np.array([10, 20 ,2 ,55,60])
a[a<15] = 0
print(a)

