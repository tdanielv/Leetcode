def reverse(x: int) -> int:
    if x > 0:
        x = [i for i in str(x)][::-1]
        return 2**31
    else:
        x = [i for i in str(x * -1)][::-1]
        return -1 * int(''.join(x))

print(reverse(1534236469))