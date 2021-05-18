class RecentCounter(object):

    def __init__(self):
        self.requests = []
        self.count = 0
        return

    def ping(self, t):
        """
        :type t: int
        :rtype: int
        """
        self.requests.append(t)
        for r in self.requests:
            # if len(r) == 0:
            #     return self.count
            if r <= 3000:
                self.count += 1
                print(self.count)

        return self.count


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)

if __name__ == '__main__':
    recentCounter = RecentCounter()
    # recentCounter.ping([])
    recentCounter.ping(10)
    print(recentCounter.ping(100))
    requests = recentCounter.requests
    print(requests)
