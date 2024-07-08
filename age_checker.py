def age_checker():
    while True:
        try:
            age = int(input("Please enter your age: "))
            if age < 0:
                print("Age cannot be negative. Please try again.")
            else:
                return age
        except ValueError:
            print("Invalid input. Please enter a valid age.")

def classify_age(age):
    if age <= 12:
        return "child"
    elif age <= 17:
        return "teen"
    else:
        return "adult"

def main():
    while True:
        age = age_checker.py()
        category = classify_age(age)
        print(f"You are classified as: {category}")

if __name__ == "__main__":
    main()