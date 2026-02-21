tasks = ["check email", "call client", "lunch", "meeting", "write report"]

for index, task in enumerate(tasks):
    if task == "lunch":
        continue
    elif index == 3:
        break
    else:
        print(f"Processing task {index}: {task}")