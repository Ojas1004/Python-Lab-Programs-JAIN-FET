# num = [1,2,3,4,5]
# squares = {i: i**2 for i in num}
# print(squares)

# num = [1, 2, 3, 4, 5]
# squares = {i: i**2 for i in num if i % 2 == 0}
# print(squares)

# word = "python"
# letters = {i for i in word}
# print(letters)
#output = {'o', 't', 'p', 'y', 'h', 'n'}


# word = "python"
# letters = [i for i in word]
# print(letters)
#output = [P,Y,T,H,O.N]


# sub = ["C++", "java", "C"]
# result = {i: len(i) for i in sub}
# print(result)

# word = "python"
# print(word[-3:-6:-1])

# P Y T H O N
# -6  -5  -4  -3  -2  -1    


# a = "Hello"
# b = "World"
# print(a + " nice " + b)

num = [1,2,2,3,4,4,3,5,6]
freq = {i: num.count(i) for i in num}
print(freq)


