# This is a project containing my work(assignments) from the GOL DSA clinics.

def minimumBribes(q):
    bribes = 0
    for i in range(len(q) - 1):
        print('index:', i)
    #     bribe = q[i] - 1 - q.index(q[i])
    #     if q[i] - 2 > 0:
    #         maxAdvance = q[i] - 2
    #     else:
    #         #The second item can only make one advance and the
    #         maxAdvance = 0

        if q.index(q[i]) < q[i] - 1:
            bribe = q[i] - 1 - q.index(q[i])
            if bribe >= 3 :
                print("Too chaotic")
                return None
            else:
                bribes += bribe
        elif q[i] > q[i+1]:
            bribe = 1
            bribes += bribe

    print(bribes)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    q = [1, 2, 5, 3, 7, 6, 4,6]
    q1 = [2, 1, 5, 3, 4]
    q2 = [2, 5, 1, 3, 4]
    q3 = [1, 2, 5, 3, 7, 8, 6, 4]


    minimumBribes(q3)


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
