#counts = 0
is_prime = True  # int -> bool
number = int(input("Input number : "))

for i in range(2, number):
    if number % i == 0:
        #counts = counts + 1  # remove +
        is_prime = False
    print(i, end=' ')

# if counts == 0:
if is_prime:  # remove ==
    print(f"\n{number} is prime number~")
else:
    print(f"\n{number} is NOT prime number! (divisors : {counts})")