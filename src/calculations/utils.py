def sum_of_the_squares(n: int):
    natural_numbers = range(1, n + 1)
    squares = [i * i for i in natural_numbers]
    return sum(squares)


def square_of_the_sum(n: int):
    natural_numbers = range(1, n + 1)
    sum_value = sum(natural_numbers)
    return sum_value * sum_value