try:
    with open("log.txt", "r") as file:

        error_count = 0

        line = file.readline()

        while line:
            print(line.strip())

            if "ERROR" in line:
                error_count += 1

            line = file.readline()

        print("\nTOtal ERROR messages:", error_count)

except FileNotFoundError:
    print("Log files does not exist")
