def main():
    first_name = "Chris"
    last_harris = "Harris"
    id = 10225
    height = 1.82

    new_name = input("What is your name? ").title()
    new_height = float(input("What is your height(m)? "))
    print(new_height - 0.5)

    def foo():
        value = 10
        return value
    x = foo()
    print(x)

    def foo2():
        value = 10
        print(value)
    x2 = foo2()
    print(x2)

    def foo3(number):
        result = number * number
        print(result)
    x3 = foo3(number=5)

    
def foo4(number1, number2):
    result = number1 - number2
    print(result)
x4 = foo4(10, 8)

if __name__ == '__main__':
    main()
    foo4()



