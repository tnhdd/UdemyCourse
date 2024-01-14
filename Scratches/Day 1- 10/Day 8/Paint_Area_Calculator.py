def paint_calc(height, width, cover):
    square_meter = test_h * test_w
    num_of_can = square_meter / coverage
    print(f"The amount of paint needed are {num_of_can}")


test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall: "))
coverage = 5
paint_calc(height=test_h, width=test_w, cover=coverage)
