class Solution(object):
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """

        if n == 0:
            schedule_len = len(tasks)
            count = 0
            while schedule_len != 0:
                tasks.pop()
                count += 1
                schedule_len -= 1
        else:
            completed_task = tasks.pop(0)
            schedule_len = len(tasks)
            count = 1
            # Returns the first instance of element that is not equal to element passed
            def checkOtherTask(tasks_list, task):
                for t in tasks_list:
                    if t != task:
                        return t

                return False

            while schedule_len != 0:
                #print(tasks)
                next_task = tasks[0]
                #print('completed', completed_task)
                #print('next is ', next_task)

                if next_task == completed_task:
                    # print(f'completed:{completed_task}\t next:{next_task}')
                    another = checkOtherTask(tasks, completed_task)
                    #print('another one:', another)
                    if another == False:
                        completed_task = tasks.pop(0)
                        count += n+1
                        schedule_len -= 1
                        #print("when flase",completed_task)
                    else:

                        popped = tasks.pop(tasks.index(another))
                        schedule_len -= 1
                        count += 1
                        #print('popped', popped)
                        #print(tasks)
                        upcoming = checkOtherTask(tasks, completed_task)
                        #print('upcoming',upcoming)
                        if upcoming != False:
                            completed_task = tasks.pop(tasks.index(upcoming))
                            count += 1
                            #print('popped', completed_task)
                            schedule_len -= 1


                else:
                    same_task = tasks.pop(0)
                    #print('popped', same_task)
                    completed_task = same_task
                    count += 1
                    schedule_len -= 1
                #print(schedule_len)

                #print(tasks)


            #print(tasks)
        return count


if __name__ == '__main__':
    tasks2 = ["A", "A", "A", "B", "B", "B"]
    tasks = ["A", "A", "A", "A", "A", "A", "B", "C", "D", "E", "F", "G"]
    n = 2
    sol = Solution()
    result = sol.leastInterval(tasks, n)
    print(result)
