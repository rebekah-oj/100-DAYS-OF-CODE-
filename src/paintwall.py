from math import ceil

test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall: "))
coverage = 5


def paint_calc(height, weight, cover):
    number_of_cans = ceil(height * weight / cover)
    print(f"The number of cans needed are: {number_of_cans}")


paint_calc(height=test_h, weight=test_w, cover=coverage)

"""def paint_clac(height=test_h, width=test_w, cover=coverage):
    number_of_cans = round(height * width / cover)

    print(f"The number of cans needed are: {number_of_cans}")
    paint_clac()
"""
