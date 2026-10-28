# 1
x = []
print(type(x))


# 2
x = [10, 20, 30]
print(type(x))


# 3
x = [10, 20, 30]
print(x)


# 4
x = [10, 20, 30]
print(x[1])


# 5
x = [10, 20, 30, 40]
print(x[-1])


# 6
x = [1, 2, 3]
x[1] = 9
print(x)


# 7
x = [1, 2]
x.append([3, 4])
print(len(x))


# 8
x = [1, 2]
x.extend([3, 4])
print(x)


# 9
x = [10, 20, 30]
x.insert(1, 15)
print(x)


# 10
x = [10, 20, 20, 30]
x.remove(20)
print(x)


# 11
x = [5, 10, 15]
print(x.pop())


# 12
x = [1, 2, 3]
x.clear()
print(x)


# 13
x = [2, 4, 2, 6]
print(x.count(2))


# 14
x = [10, 20, 30, 20]
print(x.index(20))


# 15
x = [10, 20, 30, 40]
print(x[1:3])


# 16
x = [1, 2, 3]
print(x[::-1])


# 17
print([1, 2] + [3, 4])


# 18
print([1, 2] * 2)


# 19
print(3 in [1, 2, 3])


# 20
x = [4, 1, 3]
y = sorted(x)
print(x)


# 21
x = [3, 1, 2]
print(x.sort())


# 22
a = [1, 2]
b = a
b[0] = 9
print(a)


# 23
a = [1, 2]
b = a.copy()
b[0] = 9
print(a)


# 24
x = [[10, 20], [30, 40]]
print(x[1][0])


# 25
print([n*n for n in range(1, 4)])


# 26
print([n for n in range(6) if n % 2 == 0])


# 27
print(len([10, [20, 30], 40]))


# 28
for i, v in enumerate(['a', 'b']):
    print(i, v)


# 29
print(list(zip([1, 2, 3], ['a', 'b'])))


# 30
x = [1, 2, 3]
result = x.append(4)
print(result)