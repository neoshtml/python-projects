def fizz_buzz(num):
    if (num % 3 == 0 & num % 5 == 0):
        print("Fizz and Buzz")
    elif (num % 3 == 0):
        print("Fizz")
    elif (num % 5 == 0):
        print("Buzz")

    else:
        print("Not Fizz or Buzz")


fizz_buzz(25)
fizz_buzz(9)
fizz_buzz(625)
fizz_buzz(1)