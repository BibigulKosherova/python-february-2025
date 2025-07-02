# Task1
age=int(input("How old are you? "))

if age < 13:
    print("You are a child")
elif age >= 13 and age < 18:
    print("You are a teenager")
elif age < 65 and age >= 18:
    print("You are an adult")
else:
    print("You are and elderly")

# Task2
tip=int(input("Enter tip percentage (15%, 18%, 20%, etc.): "))

if tip == 15:
    print("Standard")
elif tip == 18:
    print("Good")
elif tip == 20:
    print("Great")
elif tip > 20:
    print("My hero")


