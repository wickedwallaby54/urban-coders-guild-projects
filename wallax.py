print("welcome to the top 3 snacks collector")
snacks=[]
count=0
while count< 3:
    snack=input(f"enter snack #{count+1}:")
    snacks.append(snack)
    count+=1
print("\n your favorite snacks are:", snacks)
snacks.sort()
print("sorted snacks", snacks)
remove_item=input("\n oops! wnat to remove a snack? type it in:")
if remove_item in snacks:
    snacks.remove(remove_item)
    print("removed snack:", remove_item)
else:
    print("snack not found!")
print("\n final snack list", snacks)
print("total snacks now", len(snacks))