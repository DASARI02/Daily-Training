list_of_task=[]

def end(a,b):
    d = {'taskid': a, 'status': b}
    list_of_task.append(d)

def update_task(taskId):
    for task in list_of_task:
        if task["taskid"] == taskId:
            task["status"] = "stop"
            break
def remove_list(taskId):
    global list_of_task
    list_of_task = [task for task in list_of_task if task['taskid'] != taskId]

def print_all_tasks():
    print("\nAll tasks and their statuses:")
    if not list_of_task:
        print("No tasks available.")
    for task in list_of_task:
        print(f"Task ID: {task['taskid']}, Status: {task['status']}")

def print_running_tasks():
    print("\nRunning tasks:")
    running_tasks = [task for task in list_of_task if task['status'] == 'running']
    if not running_tasks:
        print("No running tasks available.")
    for task in running_tasks:
        print(f"Task ID: {task['taskid']}, Status: {task['status']}")

        
end(1,'running')
end(2,'running')
update_task(2)
print(list_of_task)
remove_list(1)
print(list_of_task)