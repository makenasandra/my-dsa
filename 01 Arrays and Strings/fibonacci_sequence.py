# Given a number in the find the fibonacci sequence next value in the sequence

def find_next(num):
    arr = [1, 2, 3, 5]
    a = 1
    b = 2
    c = 0
    for i in range(num):
        c = a + b
        if c > num == b:
            print(f'Found it! Next number in the sequence is {c}')
            break
        elif c > num != b:
            print('That number is not in the Fibonacci sequence.')
            break
        else:
            a = b
            b = c


if __name__ == '__main__':
    find_next(12)
