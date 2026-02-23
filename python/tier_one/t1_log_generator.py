import random
import time

actions = ["LOGIN", "LOGOUT", "UPLOAD", "ERROR", "DOWNLOAD"]

with open("server.log", "w") as file:
    for i in range(100):
        action = random.choice(actions)
        user_id = random.randint(100,105)
        timestamp = time.ctime()
        file.write(f"[{timestamp}] {user_id}:{action} - {user_id << 1}\n")


