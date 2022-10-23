def kabanchik() -> None:
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))

    if a == b:
        print(f"Numbers {a} and {b} are equal.")
    elif a < b:
        print(f"Number {a} is smaller than {b}.")
    else:
        print(f"Number {a} is greater than {b}.")


kabanchik()
