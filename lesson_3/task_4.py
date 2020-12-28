def num_pow(x, y):
    try:
        result = 1.0
        if y < 0:
            x = 1/x
            y = -y
        while y > 0:
            if (y & 1) == 1:
                result *= x
                y = y - 1
            else:
                x *= x
                y = y >> 1
        return result
    except TypeError:
        return None


print(str(num_pow(1.5, -25)))
