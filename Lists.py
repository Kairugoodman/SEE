Car_list = ["subaru", "Toyota", "Nissan", "Mazda", "Honda", "BMW"]
print(type(Car_list))
print(len(Car_list))
print("First_entry:", Car_list[0])
print("Fourth_entry:", Car_list[3])
#slicing in lists
print("First_three_entries:", Car_list[ :3])
print("Last_two_entries:", Car_list[-2:])
print(Car_list[ :2])
#Removing items
Car_list.remove("Nissan")
print(Car_list)
#Adding items
Car_list.append("Ford")