import numpy as np 

# 1D Array 

# a = np.array ([1 , 5 , 45 , 6 , 7])

# 1️⃣ sum() — TOTAL

# print(np.sum(a))

# 2️⃣ min() & max() — LOWEST & HIGHEST

# print(np.max(a))
# print(np.min(a))

# 3️⃣ mean() — AVERAGE

# print(np.mean(a))

# 4️⃣ median() — MIDDLE VALUE

# print(np.median(a))

# 5️⃣ std() — SPREAD OF DATA

# print(np.std(a))


# Axis --> axis = 0  → vertical (columns) ⬇  
#         .axis = 1  → horizontal (rows) ➡

# 2d array

Marks = np.array([
    [ 1 , 2 , 5],
    [ 6 , 7 , 8], 
    [9 , 10 , 11]
])

# print(np.sum(Marks))

# 6️⃣ sum(axis=0) — COLUMN-WISE TOTAL

# print (np.sum(Marks, axis = 0))

# 7️⃣ sum(axis=1) — ROW-WISE TOTAL

# print (np.sum(Marks, axis = 1))

# Mean 

# print(np.mean(Marks , axis = 1))
# print(np.mean(Marks , axis = 0))

# Min() & Max()

print(np.min(Marks , axis = 0))
print(np.max(Marks , axis = 0))
print(np.min(Marks , axis = 1))
print(np.max(Marks , axis = 1))


