coloumns=int(input("columns"))
rows=int(input("rows"))
symbol=(input("enter a symbol to use"))
for row in range(rows):
    for column in range(coloumns):
        print(f"{symbol} ", end="")
    print()

print("pattern complete")
print(f"you made a {coloumns} x  {rows} using {symbol}")
print("excellent work🎉!! youre a pattern master")