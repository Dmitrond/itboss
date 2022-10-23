# def goblin(x: int, b: int = 10, a: int = 15) -> int:
#     '''функція множить числа'''
#     result = x * b * a
#     return result
#
#
# print(goblin(23, 55, 12))
# print(goblin(34, 56, 34))
# print(goblin(5))


# def fn_name() -> str:
#     name = input("Enter your name: ")
#     age = input("Enter your age: ")
#     name_str = "My name is: " + name + "."
#     age_str = "I am " + str(age) + " years old."
#     result = name_str + " " + age_str
#     return result
#
#
# person_1 = fn_name()
# print(person_1)
# person_2 = fn_name()
# print(person_2)


# def speak():
#     print("Hello, who are you?")
#     answer = input("Answer the question: ")
#     print("My name is " + answer)
#     if answer == "Dima":
#         print("Happy to meet you, " + answer)
#     elif answer == "Anton":
#         print("Nice to meet you, " + answer)
#     else:
#         print("Get to the chopper!!! A-a-a-a!")
#
#
# speak()


def tomioka(x: str, n: str) -> str:
    """function return the kimetsu by naiba"""
    result = x + " " + n + "."
    return result


print(tomioka("kimetsu no", "naiba"))


def ninja_name(name: str, surname: str) -> str:
    """"""
    return f"This is {name} {surname}."


ninja = ninja_name("Subaru", "Toyota")
print(ninja)
