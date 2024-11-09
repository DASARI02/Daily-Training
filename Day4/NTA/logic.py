class Logic:
    # def d1(self):
    #     print("f1 at work")
    # pass

    def __init__(self):
        self.tasks = []
    def add(self, task):
        for i in self.tasks:
            if i.taskId == task.taskId:
                return False 
        self.tasks.append(task)
        return True 
    
    def view_all(self):
        return self.tasks





