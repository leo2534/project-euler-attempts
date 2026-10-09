number = 8753276854832754324632
output = ""

def isPrime(number):
    for i in range(2,number>>1):
        if number % i == 0:
            return False
    return True

for i in range(1, number>>1,2):
    if number == 1:
        break
    if isPrime(i):
        if number % i == 0:
            number = number / i
            
            print(i)

