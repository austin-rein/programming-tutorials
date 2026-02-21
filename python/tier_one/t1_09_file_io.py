guests = ["Alice", "Bob", "Charlie"]

with open("guest_list.txt", "w", encoding="utf-8") as file:
    for name in guests:
        file.write(name + "\n")

with open("guest_list.txt", "r", encoding="utf-8") as file:
    lines = file.readlines()

for line in lines:
    print(line)