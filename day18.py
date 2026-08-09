completed = []
print("Starting AI Assistant......")

completed . append("Read PDF") #it adds the item in the list
completed . append("Extract Text")
completed . append("Summarize")
completed . append("Save Report")
print(completed)
print(len(completed)) #len tells the number of item in the list it count's so the counting start from 1.

completed . remove("Read PDF") #it removes the item by the name we tell it to remove.
completed . remove("Extract Text")
print(completed)
print(len(completed))

fruits = ["Apple", "Mango", "Banana", "Orange", "Guava", "Blue Barry"]
fruits.pop(2) #it removes the item according to the given number, here index value starts from 0
print(fruits)