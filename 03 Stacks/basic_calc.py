import re


def left_to_right_cal(s):
    result = int(s[0])
    for i in range(1, len(s), 2):
        if s[i] == '+':
            result += int(s[i + 1])

        else:
            result -= int(s[i + 1])

    return result


def bodmas(expression, indices):
    # TODO: Finish this function which takes into account brackets in expression
    start_index = 0
    for i in range(len(indices)):
        if len(indices) == 1:
            start_index = indices[i]
            result = expression[start_index + 1]
            break
        elif indices[i] >= len(expression) / 2:
            start_index = indices[i - 1]
            result = expression[start_index + 1]
            break


def calculate(s: str) -> int:
    s = list(s)

    # Checking for rounded brackets
    indices = [i for i, x in enumerate(s) if x == "("]

    if indices:
        bodmas(s, indices)
    else:
        res = left_to_right_cal(s)

    return res




if __name__ == '__main__':
    s = "(1+(4+5+2)-3)+(6+8)"
    s1 = '1+1+2'
    l = []
    # print(s1[0])

    print(calculate(s1))
