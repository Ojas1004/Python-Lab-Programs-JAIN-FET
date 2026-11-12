
import json

try:
    with open("logs.json", "r") as file:
        logs = json.load(file)

    info = 0
    warning = 0
    error = 0

    print("All Log Records:\n")

    for log in logs:
        print(log["timestamp"], log["level"], log["message"])

        if log["level"] == "INFO":
            info += 1
        elif log["level"] == "WARNING":
            warning += 1
        elif log["level"] == "ERROR":
            error += 1

    print("\nLog Summary:")
    print("Total INFO messages:", info)
    print("Total WARNING messages:", warning)
    print("Total ERROR messages:", error)

except FileNotFoundError:
    print("Error: logs.json file not found.")

except json.JSONDecodeError:
    print("Error: Invalid JSON data.")

