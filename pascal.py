from math import sqrt, log10, floor, pi
from sys import argv


def pascal_triangle(n: int) -> None:
    """Prints a pascal triangle with n rows."""
    max_value_size: int = _pascal_size_max(n)
    _pascal_helper(1, n, [1], max_value_size)


def _pascal_size_max(row: int) -> int:
    """Calculates an approximation of the number of digits in the largest
       number in the Pascal triangle of size n"""
    # the approximation is too obviously wrong for small numbers
    cache: list[int] = [1, 1, 1, 1, 1, 2, 2, 2, 2, 3]
    if row <= len(cache):
        return cache[row-1]

    # math stuff going on... using Stirling's approximation
    n: float = row / 2
    approx_bin_coff: float = 2**(2 * n) / sqrt(pi * n)
    return floor(log10(approx_bin_coff)) + 1


def _pascal_helper(current: int, max: int, row: list[int], max_value_size: int) -> None:
    """Given a row of the pascal triangle, print it and calculate the next.
       Recurse and continue until current has reached max."""
    for num in row:
        print(str(num).rjust(max_value_size + 1), end='')

    print()

    if current < max:
        sums: list[int] = [a + b for a, b in zip(row, row[1:])]
        new_row: list[int] = [1, *sums, 1]
        _pascal_helper(current + 1, max, new_row, max_value_size)


def main():
    if len(argv) == 2:
        try:
            pascal_triangle(int(argv[1]))
        except ValueError:
            print("Program argument isn't a number!")
    else:
        pascal_triangle(6)


if __name__ == '__main__':
    main()
