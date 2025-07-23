foods=["pizza","tacos","burgers","sushi", "fries"]
print("starting food list:", foods)
new_food=input("enter one food to add to the list:")
foods.append(new_food)
print("added! nnew list:",foods)
remove_food=input("enter a food you  want to remove from the list:")
if remove_food in foods:
    foods.remove(remove_food)
    print(f"removed {remove_food}.")
else:
    print(f"{remove_food} is not in the list.")
    print("current list", foods)
print("total items in the list:", len(foods))
should_sort=input("do you want to sort the list alphabetically? (yes/no):")
if should_sort=="yes":
    foods.sort()
    print("sorted list", foods)
else:
    print(" Skipping sort. Final list remains:")
    print(foods)
