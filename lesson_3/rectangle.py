def get_perimeter(a: int, b: int) -> None:
    """
    Calculates rectangle perimeter with given sides
    """
    perimeter = (a + b) * 2
    result = f"Perimeter is {perimeter} cm."
    print(result)


def get_area(a: int, b: int) -> None:
    """
    Calculates rectangle area with given sides
    """
    area = a * b
    result = f"Area is {area} cm2."
    print(result)


side_a = int(input("Enter side a (cm) of the rectangle: "))
side_b = int(input("Enter side b (cm) of the rectangle: "))
get_perimeter(side_a, side_b)
get_area(side_a, side_b)
