def is_prime(func):
    def wrapper(*args, **kwargs):
        n = func(*args, **kwargs)

        if n <= 1:
            print("Ни простое и не составное")
        elif n <= 3:
            print("Простое")
        elif n % 2 == 0 or n % 3 == 0:
            print("Составное")
        else:
            i = 5
            is_prime_number = True
            while i * i <= n:
                if n % i == 0 or n % (i + 2) == 0:
                    is_prime_number = False
                    break
                i += 6
            if is_prime_number:
                print("Простое")
            else:
                print("Составное")

        return n

    return wrapper


@is_prime
def sum_three(a, b, c):
    return a + b + c


result = sum_three(2, 3, 6)
print(result)
