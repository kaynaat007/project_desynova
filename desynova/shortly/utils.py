from constants import digit_to_alphabet_map


def to_string(num):
    """
    :param num:
    :return:
    """
    function = to_string.__name__
    try:
        res = ""
        while num:
            r = num % 10
            res += digit_to_alphabet_map[r]
            num /= 10
        return res[::-1]
    except Exception as e:
        raise Exception(function, e.args)
