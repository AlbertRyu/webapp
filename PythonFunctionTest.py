
def say_name(func):
    print('Albert! Say this one first!')

    def repeat():
        for i in range(1, 4):
            func()
    return repeat


@say_name
def say_hello():
    print("hello!")

say_hello()