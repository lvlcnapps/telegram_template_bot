import datacleaning as dc

class UserCleaning():
    def __init__(self):
        print('UC module started')
        self.tasks = []

    def getProgress(self):
        ans = ""
        i = 0
        for task in self.tasks:
            ans += f'№{i} - Name: {task.getName()} - Mark: {task.getMark()}\n'
            i += 1
        print(ans)
        return ans

    def getDone(self):
        ans = ""
        i = 0
        for task in self.tasks:
            if (task.getMark() == 1):
                ans += f'№{i} - Name: {task.getName()} - Mark: {task.getMark()}\n'
            i += 1
        print(ans)
        return ans

    def makeTask(self, text):
        temp_dc = dc.DataCleaning()
        temp_dc.setName(text)
        temp_dc.setMark(0)
        self.tasks.append(temp_dc)
        print("")

    def removeTask(self, num):
        temp = self.tasks.pop(num)
        print("")
        return temp.getName()

    def removeDoneTasks(self):
        new_tasks = []
        for task in self.tasks:
            if (task.getMark() != 1):
                new_tasks.append(task)
        self.tasks = new_tasks
        print("")

    def clearTasks(self):
        self.tasks.clear()
        print("")

    def markTask(self, num):
        self.tasks[num].setMark(1)
        print("")
        return self.tasks[num].getName()

    def unmarkTask(self, num):
        self.tasks[num].setMark(0)
        print("")
        return self.tasks[num].getName()

    def getLastTask(self):
        return len(self.tasks) - 1