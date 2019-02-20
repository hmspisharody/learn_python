def is_prime(x):
    i=2
    while i<=(x//2):
        if x%i == 0:
            return 0
        i+=1        
    return 1

def primes(x):
    for i in range(2, x+1):
        if is_prime(i):
            yield i
num = int(input("Enter a number to generate all primes till that number : "))
a = list(primes(num))

#a = is_prime(3)
print(a)

