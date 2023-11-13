def find_factors(num):
    """Find factors of num, in increasing order.

    >>> find_factors(10)
    [1, 2, 5, 10]

    >>> find_factors(11)
    [1, 11]

    >>> find_factors(111)
    [1, 3, 37, 111]

    >>> find_factors(321421)
    [1, 293, 1097, 321421]
    """
    # We will store all factors in `result`
    result = []
    i = 1
    # This will loop from 1 to int(sqrt(x))
    while i * i <= num:
        # Check if i divides x without leaving a remainder
        if num % i == 0:
            result.append(i)
            # Handle the case explained in the 4th
            if num // i != i:  # In Python, // operator performs integer/floored division
                result.append(num // i)
        i += 1
    # Return the list of factors of x
    return result

