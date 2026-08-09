#1
tasks = ["Study", "Exercise"]
tasks.extend(["Read", "Code", "Excel"]) #extend adds more than one item in the list at the same time. 
print(tasks)
print(len(tasks))

#2
names = ["Aman", "Rohit", "Neeraj"]
names.insert(1, "Vishal") #insert put the item in a specific place according to the indexation, the indexation in python starts from  0
print(names)

#3
numbers = [8, 9, 2, 10, 1, 3, 17, 21]
numbers.sort() #sort rearranges the number in the ascending order.
print(numbers)

#4
scores = [100, 300, 200, 500, 400, 900]
scores.sort(reverse=True)
print(scores)

#5
names = ["Vishal", "Shubham", "Neeraj", "Manjeet", "Rakhi", "Rashmi"]
names.sort() #rearranges alphabetically
print(names)

#6
fruits = ["Orange", "Banana", "Apple", "Mango"]
fruits.reverse() #it just reverse the existing order
print(fruits)

#7
names = ["Aman", "Vishal", "Aman", "Rohit", "Aman"]
print(names.count("Aman"))
