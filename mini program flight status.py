def check_status(flights, status):
    if status == "red":
        print(flights, "has been left, you are late.")
    elif status == "green":
        print(flights, "is waiting for you, Have a happy journey!")
    else:
        print("invalid response")
    

flights = ["American Flight", "Russian Flight", "Chinese Flight", "South Korean Flight", "Japanese Flight"]
for flight in flights:
    status = input(f"{flight} red/green?").lower()
    check_status(flight, status)

print("Thankyou for using our app")