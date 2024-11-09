list = []
def start(taskId,status):
    d = {'taskId': taskId, 'status': status}
    list.append(d)
    return list
def update_list(taskId):
    for task in list:
        if task['taskId'] == taskId:
            task['status'] = 'stopped'
        return task
    
def remove_dict(taskId):
    for task in list:
        if task['taskId'] == taskId:
            task.pop(taskId)
            
            


        



