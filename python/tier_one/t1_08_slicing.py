data = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
middle = data[3:6]
evens = data[::2]
data[-2:] = [99,100]
backward = data[::-1]

print(middle)
print(evens)
print(backward)