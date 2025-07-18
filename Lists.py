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

# Do not change: Number of customers each day for the last month
num_customers = [137, 147, 135, 128, 170, 174, 165, 146, 126, 159,
                 141, 148, 132, 147, 168, 153, 170, 161, 148, 152,
                 141, 151, 131, 149, 164, 163, 143, 143, 166, 171]
average_first_seven = sum(num_customers[:7]) / 7
average_last_seven = sum(num_customers[-7: ]) / 7
max_month= max(num_customers)
min_month= min(num_customers)

print("Average number of customers first seven days:", average_first_seven)
print("Average number of customers last seven days:", average_last_seven)
print("Maximum customers in a day:", max_month)
print("Minimum customers in a day:", min_month)