def missing_number(numbers):
    n = len(numbers)

    expected_sum = n * (n + 1) // 2
    actual_sum = sum(numbers)

    return expected_sum - actual_sum


numbers = [4, 3, 1, 0]

result = missing_number(numbers)

print("Missing number --->", result)
