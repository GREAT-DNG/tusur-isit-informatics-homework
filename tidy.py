def is_tidy(n):
    return n == int("".join(sorted(str(n)))) # pyright: ignore
