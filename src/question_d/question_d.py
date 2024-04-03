def is_prime(num):
    if num <= 3:
        return num > 1
    if num % 2 == 0 or num % 3 == 0:
        return False
    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
    return True

print(is_prime(4))
print(is_prime(5))
print(is_prime(11))

# Not sure if this will actually account for ALL prime numbers, but it should at least rule out anything divisible by 2 or by itself.
# Not actually sure what the conjecture is wrt finding any prime and I can't account for every number.