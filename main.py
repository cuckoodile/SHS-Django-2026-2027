fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
  if "a" in x:
    newlist.append(x)

# print(newlist)

# -----------------------------
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = [x for x in fruits if "a" in x]

# fruits.filter((x) => x.includes('a'))

# print(newlist)

# ----------------------------

i = 1
while i <= 10:
    # print(i)
    i += 1

# -----------------------------
# range(start=0, stop=10 (exclusive), steps=None)
# print(range(10))
# print(list(range(1, 10)))

# -----------------------------

a = [1, 2, 3, 4, 5]
b = ['a', 'b', 'c', 'd', 'e']
c = ['!', '@', ',', '.', '-']

print(list(zip(a, b, c)))