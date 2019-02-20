def decor(func):
    def wrap():
        num = input("Enter a number : ")
        return func(int(num))**2
    return wrap

@decor
def double(num):
    return 2*num

abc = double()
print(abc)
