def add(a, b):
    return a + b


def main():
    nums = ((1, 3), (1, 33), (4, 44))
    for a, b in nums:
        result = add(a, b)
        print("a + b = ", result)


if __name__ == "__main__":
    main()
