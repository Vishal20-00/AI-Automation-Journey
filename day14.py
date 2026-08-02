def check_password(password):
    if password is "0719":
        return "Access Granted"
    else:
        return "Access Denied"

variable = check_password("019")
print(variable)