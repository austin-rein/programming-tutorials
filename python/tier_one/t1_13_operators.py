buffer = [10, 3, 5, 8]

key = 0b101

while (count := len(buffer)) > 0:
    item = buffer.pop()
    if item & 1:
        print(f"Item {item} is odd")
    else:
        print(f"Item {item} is even")

    encrypted = item ^ key

    print(f"Encrypted & Shifted: {encrypted << 1}")
