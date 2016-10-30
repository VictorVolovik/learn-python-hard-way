def add(a, b):
    print("Adding %d + %d" % (a ,b))
    return a + b

def substract(a, b):
    print("Subtracting %d - %d" % (a, b))
    return a - b

def multiply(a, b):
    print("Multiplying %d * %d" % (a, b))
    return a * b

def divide(a, b):
    print("Divinding %d / %d" % (a, b))
    return a / b

print("Let's do some math")

addition = add(5, 10)
substraction = substract(addition, 5)
multiplication = multiply(substraction, 10)
division = divide(multiplication, 25)

print(addition, substraction, multiplication, division)

