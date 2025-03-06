from bisect import bisect_right

def next_smallest(a, x):
    if not a or x < a[0] or x > a[-1]:
        return -1

    # Find the insertion point for x
    idx = bisect_right(a, x)

    # If x is greater than the last element, return -1
    if idx == len(a) and a[idx - 1] != x:
        return -1

    # If x is in the list, return x
    if a[idx - 1] == x:
        return x

    # Otherwise, return the next smallest element
    return a[idx - 1] if idx - 1 < len(a) else -1

def next_biggest(a, x):
    if not a or x < a[0] or x > a[-1]:
        return -1

    idx = bisect_right(a, x)

    if idx == len(a) and a[idx -1] != x:
        return -1

    if a[idx] == x:
        return x

    return a[idx] if idx < len(a) else -1

# Test cases with expected results
small_test_cases = [
    (12, 12),
    (13, 12),
    (2, -1),
    (21, 21),
    (22, -1),  # This should return -1 because 22 is greater than the last element
    (9, 9),
    (5, 4),
]

big_test_cases = [
    (12, 12),
    (13, 14),
    (2,  -1),
    (21, 21),
    (22, -1),
    (9,   9),
    (5,   6),
]

# Run tests
for x, expected in small_test_cases:
    result = next_smallest([3, 4, 6, 9, 10, 12, 14, 15, 17, 19, 21], x)
    status = "PASS" if result == expected else "FAIL"
    print(f"next_smallest(a, {x}) = {result}, Expected = {expected} → {status}")


for x, expected in big_test_cases:
    result = next_biggest([3, 4, 6, 9, 10, 12, 14, 15, 17, 19, 21], x)
    status = "PASS" if result == expected else "FAIL"
    print(f"next_biggest(a, {x}) = {result}, Expected = {expected} → {status}")
