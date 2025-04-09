from is_emptyFunction import is_empty

R = set()

n = int(input("What is the number of elements in the relation: "))

for _ in range(n):
    x, y = input("Enter a pair of elements (ex: a b): ").split()
    R.add((x, y))



if is_empty(R):
    print("This relation is empty.")
else:
    print("This relation is not empty.")
