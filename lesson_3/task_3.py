def my_func(arg_1, arg_2, arg_3):
    try:
        return arg_1 + arg_2 + arg_3 - min(arg_1, arg_2, arg_3)
    except TypeError:
        return None


print(str(my_func(-1, 32, -103)))
