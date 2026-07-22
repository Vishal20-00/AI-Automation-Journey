items = ["history", "polity", "maths"]
for item in items:
    print(item)
topic = input("Which of the following topic have you completed?: (name of the topic)").lower()
if topic in items:
    print("Great! You have completed a topic in your SSC Journey.")
else:
    print("That topic is not in your current learning plan.")