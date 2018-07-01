from functools import reduce, partial


def max_product(int_list):
    """
    Calculates the maximum possible product of any combination of integers in int_list.

    E.g. [1, 3, 7, 9] returns the maximum product of 3 values as 189 (3*7*9)

    Will run in O(n log n) time and use additional O(1) memory.

    :param list, tuple int_list: A list or tuple of integers. Can be any size and can be None
    :return: The maximum possible product
    """
    # Edge cases
    if int_list is None:
        return None

    if type(int_list) != list and type(int_list) != tuple:
        raise TypeError('int_list must be list or tuple')

    if len(int_list) == 0:
        return None

    product = partial(reduce, lambda prev, curr: prev * curr)

    if len(int_list) <= 3:
        return product(int_list, 1)

    # Main cases
    int_list = sorted(int_list, reverse=True)

    # Calculate the product of the 3 largest values
    all_pos = product(int_list[:3], 1)

    # Calculate the product of the largest value and the two smallest (to include large negative values)
    two_neg = product(int_list[-2:], 1) * int_list[0]

    return max(all_pos, two_neg)


def max_product_fast(int_list):
    """
    Calculates the maximum possible product of any combination of integers in int_list.

    E.g. [1, 3, 7, 9] returns the maximum product of 3 values as 189 (3*7*9)

    Will run in O(n) time and use additional O(1) memory.

    :param list, tuple int_list: A list or tuple of integers. Can be any size and can be None
    :return: The maximum possible product
    """
    # Edge cases
    if int_list is None:
        return None

    if type(int_list) != list and type(int_list) != tuple:
        raise TypeError('int_list must be list or tuple')

    if len(int_list) == 0:
        return None

    product = partial(reduce, lambda prev, curr: prev * curr)

    if len(int_list) <= 3:
        return product(int_list, 1)

    # Main cases
    # Keep track of two subsets of ints: the first has all the largest values encountered, the second keeps the largest
    # positive value and the two negative values largest in magnitude

    all_pos = sorted(int_list[:3])
    two_neg = sorted(int_list[:3])

    for value in int_list[3:]:
        if value > all_pos[0]:
            all_pos[0] = value
            all_pos = sorted(all_pos)

        if value > two_neg[-1]:
            two_neg[-1] = value
            two_neg = sorted(two_neg)
        elif value < two_neg[1]:
            two_neg[1] = value
            two_neg = sorted(two_neg)

    return max(product(all_pos, 1), product(two_neg, 1))
