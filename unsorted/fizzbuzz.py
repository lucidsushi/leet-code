def fizzbuzz(input: int) -> str:

    # divisors = {
    #     'fizz': 3,
    #     'buzz': 5,
    #     'crank': 7
    # }
    # for word, divisor in divisors.items():
    #     try using unpacking **divisor?
    #     pass

    def has_and_divisible(input: int, divide_by: int) -> str:
        if input % divide_by == 0 or str(divide_by) in str(input):
            return True
        else:
            return False

    if has_and_divisible(input, 3 * 5):
        return "fizzbuzz"
    elif has_and_divisible(input, 3):
        return "fizz"
    elif has_and_divisible(input, 5):
        return "buzz"
    else:
        return str(input)


assert fizzbuzz(1) == 1
assert fizzbuzz(3) == "fizz"
assert fizzbuzz(23) == "fizz"
assert fizzbuzz(5) == "buzz"
assert fizzbuzz(25) == "buzz"
assert fizzbuzz(15) == "fizzbuzz"
