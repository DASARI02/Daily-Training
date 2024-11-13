list_of_task = []

def end(a, b):
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

def menu():
    while True:
        print("\nMenu:")
        print("1. Add task")
        print("2. Update task status to 'stop'")
        print("3. Remove task")
        print("4. Print all tasks and statuses")
        print("5. Print only running tasks")
        print("6. Exit")

        choice = input("Enter your choice: ")
        
        if choice == "1":
            task_id = int(input("Enter task ID: "))
            status = input("Enter task status: ")
            end(task_id, status)
        elif choice == "2":
            task_id = int(input("Enter task ID to update: "))
            update_task(task_id)
        elif choice == "3":
            task_id = int(input("Enter task ID to remove: "))
            remove_list(task_id)
        elif choice == "4":
            print_all_tasks()
        elif choice == "5":
            print_running_tasks()
        elif choice == "6":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

end(1, 'running')
end(2, 'running')
update_task(2)

menu()
