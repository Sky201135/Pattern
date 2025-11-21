rowSize = int(input("Enter number of rows: "))
if rowSize%2==0:
    halfDiamondRow = rowSize // 2
else:
    halfDiamondRow = rowSize // 2 + 1

# Upper half including middle row
for i in range(1, halfDiamondRow + 1):
    # leading spaces
    print("  " * (halfDiamondRow - i), end="")
    # numbers from 1 to (2*i-1)
    for num in range(1, 2 * i):
        print(num, end="")
    print()

# Lower half
for i in range(halfDiamondRow - 1, 0, -1):
    print("  " * (halfDiamondRow - i), end="")
    for num in range(1, 2 * i):
        print(num, end="")
    print()