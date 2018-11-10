
try:
    print(10/8)
    print(10+'o')
except ArithmeticError as e:
    print(e)
except Exception:
    print('\nThere is something wrong')
