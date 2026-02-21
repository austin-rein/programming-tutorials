temperature = 60
mode = "auto"

match mode:
    case "off":
        print("System is off.")
    case "auto":
        if temperature < 70:
            print("Heating on.")
        elif temperature > 80:
            print("Cooling on.")
        else:
            print("System standby.")