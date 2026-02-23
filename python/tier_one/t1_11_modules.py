import random
import python.tier_one.t1_my_tools as t1_my_tools

if __name__ == "__main__":
    names = ["Alice", "Bob", "Charlie"]
    print(t1_my_tools.greet(random.choice(names)))