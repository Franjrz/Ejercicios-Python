def descending_order(num):
    # First of all cast from int to list

    num = [d for d in str(num)]
    # Second sort the list in reverse order
    num.sort(reverse = True)
    # Third make the reverse last cast

    num = int("".join(num))
    # Return the result
    return num