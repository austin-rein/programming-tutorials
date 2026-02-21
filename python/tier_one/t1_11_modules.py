import random
import my_tools

if __name__ == "__main__":
    names = ["Alice", "Bob", "Charlie"]
    print(my_tools.greet(random.choice(names)))