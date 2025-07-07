def days():
    day=years*365
    return day

years=int(input("Enter number of years: "))
x=days()
print(f"There are {x} in {years} years.")

