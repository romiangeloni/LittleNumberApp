def mytheresa(number, tuple_list):
    result = ""
    for n, w in tuple_list:
        if number % n == 0:
            result += w
    if result == "":
        result = number
    print("\nOutput: {}".format(result))


if __name__ == "__main__":
    number = input("Enter a number (divisible): ")
    tuple_list = input('''Enter a list of tuples (a, b), where:
        \t * a is a number that will check if is a divisor of divisible
        \t * b is a word that you want to show when the number will''' + 
        ''' dividable by divisor.\n
        \t EXAMPLE: [(3, "my"), (5, "theresa"), (7, "clothes")]\nInput: ''')
    mytheresa(int(number), list(eval(tuple_list)))