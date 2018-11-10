

def add(*args):
    print(sum(args))

add(1,2,3)


def add(*args):
    for name in args:
        print('Welcom ',name)

add('Bob','Leo','Peter')