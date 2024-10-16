def recursive_sum():
    n = input('>>> ')
    if not n:
        return 0.0
    return int(n) + recursive_sum()


res = recursive_sum()
print(res)