def naive_cubed_sum(a, b):
    total_sum = 0
    for i in range(a, b + 1):
        total_sum += i ** 3
    return total_sum

def naive_cubed_sum_even(a, b):
    total_sum = 0
    for i in range(a, b + 1):
        if i % 2 == 0:
            total_sum += i ** 3
    return total_sum

def naive_cubed_sum_odd(a, b):
    total_sum = 0
    for i in range(a, b + 1):
        if i % 2 == 1:
            total_sum += i ** 3
    return total_sum