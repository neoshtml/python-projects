def atm(balance, withdraw, deposit):
    withdraw=int(input("How much would you like to withdraw?"))
    deposit=int(input("How much would you like to deposit?"))
    if (withdraw > balance):
        print("Unable to withdraw")
    if (withdraw > deposit):
        print ("Unable to withdraw.")
    if (deposit > withdraw):
        print (balance + deposit)
        print("You have this much balance left: ", balance + deposit)
    elif (balance >= withdraw):
        print(balance - withdraw)
        print("Your withdraw balance is ", balance - withdraw)
    return balance


atm(1900, 0, 100)