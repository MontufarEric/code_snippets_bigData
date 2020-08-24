class Calculator: 
    def add(x, y):
    #     Addition Function
        return x + y


    def subtract(x, y):
    #     Subtraction Function
        return x - y


    def multiply(x, y):
    #     Multiplication Function
        return x * y


    def divide(x, y):
    #     Division Function
        if y == 0:
            raise ValueError('Can not divide by zero!')
        return x / y
