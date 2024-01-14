def add(*number):
    sum = 0
    for n in number:
        sum += n
    return sum


# print(add(3, 4, 5))


def calculate(**kwargs):
    print(kwargs)


calculate(add=3, multiply=5)
