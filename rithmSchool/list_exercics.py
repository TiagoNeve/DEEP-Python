# 1
print("01 Exercícios")
for i in [1, 2, 3, 4]:
    print(i)

# 2
print("02 Exercícios")
print([i*20 for i in [1, 2, 3, 4]])

# 3
print("03 Exercícios")
arr = []
for i in ["Elie", "Tim", "Matt"]:
    arr.append(i[0])
print(arr)

# 4
print("04 Exercícios")
print([i for i in [1, 2, 3, 4, 5, 6] if i % 2 == 0])

# 5
print("05 Exercícios")
print([i for i in [1, 2, 3, 4] if i in [3, 4, 5, 6]])

# 6
print("06 Exercícios")
arr = []
for i in ["Elie", "Tim", "Matt"]:
    arr.append(i[::-1].lower())
print(arr)

# 7
print("07 Exercícios")
arr = []
for i in "first":
    if i in "third":
        arr.append(i)
print(arr)

# 8
print("8 Exercícios")
print([i for i in range(1, 100) if i % 12 == 0])

# 9
print("9 Exercícios")
print([i for i in "amazing" if i not in ['a', 'e', 'i', 'o', 'u']])

# 10
print("10 Exercícios")
print([[i for i in range(0, 3)] for num in range(0, 3)])

# 11
print("11 Exercícios")
print([[i for i in range(0, 10)] for num in range(0, 10)])
