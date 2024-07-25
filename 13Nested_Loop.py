rows=int(input("Enter rows: "))
columns=int(input("Enter columns: "))
symbol=input("Enter the symbol: ")
for  i in range(rows):
    for j in range(columns):
        print(symbol , end="")
    print()
