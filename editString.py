userInput = input("Enter a String: ")
while True:
    changes = input("Make changes: ").lower()
    if changes == "x":
        print("Your final chnage is ", userInput)
        break
    elif changes == "u":
        recent = userInput
        userInput = userInput.upper()
        print(userInput)
    elif changes == "l":
        recent = userInput
        userInput = userInput.lower()
        print(userInput)
    elif changes == "r":
        recent = userInput
        userInput = userInput[::-1]
        print(userInput)
    elif changes.startswith("c") and len(changes) == 5:
        recent = userInput
        if userInput.isupper():
            changes = changes.upper()
            userInput = userInput.replace(changes[2], changes[4])
            print(userInput)
        else:
            userInput = userInput.replace(changes[2], changes[4])
            print(userInput)
    elif changes == "z":
        userInput = recent
        print(userInput)
