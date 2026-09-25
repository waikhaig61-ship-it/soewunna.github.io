age = int(input("Enter your age: "))
is_student = input("Are you a student? (yes/no): ").lower()
is_weekend = input("Is it weekend? (yes/no): ").lower()

is_free = False

# ?????????? ???????????????? ????????????
if age < 5:
    is_free = True
    price = 0
elif age <= 12:
    price = 3000
elif age <= 59:
    price = 5000
else:
    price = 3000

# Free ticket ?????????
if is_free:
    print()
    print("Ticket price: Free")

# Free ?????????? Discount ????? Weekend fee ?????????
else:
    if is_student == "yes":
        price = price - 1000

    if is_weekend == "yes":
        price = price + 1000

    print()
    print("----- Movie Ticket Receipt -----")
    print("Age:", age)
    print("Student:", is_student)
    print("Weekend:", is_weekend)
    print("Final price:", price, "kyats")
    print("--------------------------------")



