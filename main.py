#Collatz Conjecture

num = int(input("Enter a natural number/positive integer: "))

while num != 1:
    if num % 2 == 0:
        num = num / 2
    else:
        num = num*3+1
    print(num)
    