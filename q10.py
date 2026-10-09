from mymath import isPrime

total =0
for i in range(0,10):
    if isPrime(i):
        print(i)
        total += i
print(total)
