s_values = [0, 2.33, 1.69, 1.32, 0.88]


def s_value(number_of_brands_rated):
    if number_of_brands_rated <= 1:
        return 0
    elif number_of_brands_rated > 5:
        return s_values[4]
    else:
        return s_values[number_of_brands_rated - 1]
