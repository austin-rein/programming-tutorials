raw_inventory = ["apple", "banana", "apple", "orange", "banana", "grape"]

unique_inventory = set(raw_inventory)

store_info = ("The Fruit Stand", "Wakefield")

prices = {
    "apple": 0.50,
    "banana": 0.30,
    "orange": 0.80,
    "grape": 1.20
}

print(store_info[0])

for item in unique_inventory:
    print(f"Item: {item} - Price: ${prices[item]}")