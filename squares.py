def generate_squares():
    squares = []
    for i in range(1, 31):
        square = i ** 2
        squares.append(square)
    print("Squares of numbers from 1 to 30: ", squares)
generate_squares()