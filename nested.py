medical_cause = input("Do you have a medical cause? Yes or No?")
attendance=int(input("Enter your attendance number:"))

if medical_cause== 'Yes':
    print("You are allowed")
else:
    if attendance>=75:
        print("You're allowed")
    else:
        print("You're not allowed")