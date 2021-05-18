# Implementation of a queue using two stacks.

# The queueOperations() function takes in queries, where each query is one of the following  types:
# 1 x: Enqueue element  into the end of the queue.
# 2: Dequeue the element at the front of the queue.
# 3: Print the element at the front of the queue.f
def queueOperations(queries):
    my_queue = []
    for q in queries:
        if len(q) > 1:
            my_queue.insert(0, q[1])
        elif q[0] == 2:
            my_queue.pop()
        if q[0] == 3:
            print(my_queue[-1])


if __name__ == '__main__':
    queries_input = [10, [1, 42], [2], [1, 14], [3], [1, 28], [3], [1, 60], [1, 78], [2], [2]]

    queries = []
    for q in range(1, queries_input[0] + 1):
        queries.append(queries_input[q])

    print(queries)
    queueOperations(queries)
