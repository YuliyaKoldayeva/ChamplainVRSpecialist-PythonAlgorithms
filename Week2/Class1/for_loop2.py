# The following looping structure will demonstrate
# a nested loop.

for y in range(0,11):
    print(str(y) + ": ", end="")
    for x in range(y):
        print("*",end="")
    print()
