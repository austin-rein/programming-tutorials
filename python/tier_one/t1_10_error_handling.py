user_inputs = ["10", "5", "0", "hello", "20"]

for input in user_inputs:
    try:
        result = 100 / int(input)
    except ValueError:
        print(f"Value Error: {input} is not a number.")
    except ZeroDivisionError:
        print("Math Error: Cannot divide by zero.")
    else:
        print(f"Success: 100 / {input} = {result}")
    finally:
        print("--- Processing complete ---")

