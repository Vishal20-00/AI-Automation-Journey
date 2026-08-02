def login(username, password):
    if username == "Vishal" and password == "python@123":
        return "Login Successful"
    else: 
        return "Login failed"

username = input("Enter username:")
password = input("Enter Password:")

result = login(username, password)
print(result)

if result == "Login Successful":
    print("Welcome to your AI Automation Dashboard!")
else:
    print("Please try again.")