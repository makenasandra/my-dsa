# Assignments

if __name__ == '__main__':
    # 1. Array Reversal
    array1 = [1, 2, 3, 4, 5]

    print('Original array:', array1, '\nReversed array:', array1[::-1])


    # 2. Sentence reversal

    def reverseSentence(s, start, end):
        while start < end:
            s[start], s[end] = s[end], s[start]
            start += 1
            end -= 1


    s = 'This is a great program'
    print('\nOriginal sentence', s)

    # Convert string to list to use it as a char array
    s = list(s)
    start = 0

    while True:
        try:
            # Find the next space
            end = s.index(' ', start)

            # Call function
            # to reverse each word
            reverseSentence(s, start, end - 1)

            # Update start variable
            start = end + 1

        except ValueError:
            # Reverse the last word
            reverseSentence(s, start, len(s) - 1)
            break

    # Reverse the entire list
    s.reverse()

    # Convert the list back to

    s = "".join(s)
    print('Reversed array:', s)
