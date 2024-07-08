def chat_bot():
    print("Welcome blud")
    response = input("What can I help you with?\n")
    if(response == "calculate"):

        func = input("what you wanna calculate?\n")
        num1 = int(input("what's your first number?\n"))
        num2 = int(input("what's your second number?\n"))

        result = 0

        if(func == "add"):
            result = num1 + num2
        elif(func == "sub"):
            result = num1 - num2
        elif(func == "mult"):
            result = num1 * num2
        elif(func == "div"):
            result = num1 / num2
        elif(func == "power"):
            result = num1 ** num2

    print("Your result is:", result)

chat_bot()