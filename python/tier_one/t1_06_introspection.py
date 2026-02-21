my_global = "I am global"

def investigate(obj):
    my_local = 99
    print(type(obj))
    print(id(obj))
    print(locals())

investigate(my_global)
print(f"Is my_global a string? {isinstance(my_global, str)}")
print(dir(my_global)[-1])