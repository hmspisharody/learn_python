def decor(func):
    def wrap():
        num = input("Enter a number : ")
        return 2*float(num)
    return wrap

@decor
def double(num):
    return 2*num

abc = double()
