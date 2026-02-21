with open("server.log", "r") as file:
    clean_data = [tuple(line[27:].strip().split(' - ')) for line in file]

for info, checksum in clean_data:
    if (uid := int(info.split(":")[0])) << 1 == int(checksum):
        pass
    else:
        print(f"SECURITY ALERT: Corrupt data for user {uid}")

error_users = { int(info.split(':')[0]) for info, checksum in clean_data if "ERROR" in info}
print(error_users)