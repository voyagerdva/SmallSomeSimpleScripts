a = [[1,2,3],[4,5,6],[7,8,9]]

# we should have [1,2,3,4,5,6,7,8,9]

b = []

for i in range(len(a)):
    for j in range(len(a[i])):
        b.append(a[i][j])

print(b)
print(*b)