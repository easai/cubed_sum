from enum import Enum


class Parity(Enum):
    ODD = 'odd'
    EVEN = 'even'
    BOTH = 'both'


def sum_of_cubes(m: int, parity=Parity.BOTH) -> int:
    total_sum = 0
    if m < 0:
        n = -m
    else:
        n = m
    if parity == Parity.ODD:
        if n % 2 == 0:
            n -= 1
        n = (n+1) // 2
        total_sum = n*n*(2*n*n-1)
    elif parity == Parity.EVEN:
        if n % 2 == 1:
            n -= 1
        n //= 2
        total_sum = 2 * ((n * (n + 1)) ** 2)
    elif parity == Parity.BOTH:
        total_sum = (n * (n + 1) // 2) ** 2
    if m < 0:
        total_sum = -total_sum
    return total_sum


def cubed_sum(a: int, b: int, parity=Parity.BOTH) -> int:
    if a > b:
        raise ValueError("a should be less than or equal to b")
    total_sum = 0
    if 0 <= a:
        total_sum = sum_of_cubes(b, parity) - sum_of_cubes(a - 1, parity)
    else:
        if 0 <= b:
            total_sum = sum_of_cubes(b, parity) + sum_of_cubes(a, parity)
        else:
            total_sum = sum_of_cubes(b, parity) - sum_of_cubes(a+1, parity)
    return total_sum
