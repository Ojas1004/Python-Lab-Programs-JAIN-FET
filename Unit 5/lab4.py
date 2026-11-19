import matplotlib.pyplot as plt

dates = []
products = []
sales = []

# Reading CSV file
with open("sales.csv", "r") as file:
    data = file.read()
    lines = data.split("\n")

    for row in lines[1:]:
        if row:
            values = row.split(",")

            dates.append(values[0])
            products.append(values[1])
            sales.append(int(values[2]))

# line graph
plt.plot(dates, sales, marker='o')
plt.title("Retail Sales")
plt.xlabel("Date")
plt.ylabel("Sales")
plt.show()

# bar chart
plt.bar(dates, sales)
plt.title("Product Sales")
plt.xlabel("Date")
plt.ylabel("Sales")
plt.show()