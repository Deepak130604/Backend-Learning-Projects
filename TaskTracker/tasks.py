import os,json,sys
from datetime import datetime

file_name = "tasks.json"
# Fetch the available tasks....
def load_tasks():
    if not os.path.exists(file_name):
        return []
    try:
        with open(file_name,"r") as f:
            return json.load(f)
    except json.JSONDecodeError:
        print("Error: Could not decode JSON from tasks file.")
        return []

# Save the tasks to the JSON file
def save_tasks(tasks):
    try:
        with open(file_name,'w') as f:
            json.dump(tasks,f,indent=4)
    except Exception as e:
        print(f"Error: Could not save tasks to file. {e}")

# Add a new task to the list
def add_tasks(description):
    tasks = load_tasks()
    if len(tasks) == 0:
        task_id = 1
    else:
        task_id = tasks[-1]["id"] + 1
    
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    new_task ={
        "id": task_id,
        "description": description,
        "current_time": current_time,
        "status": "ToDo"
    }
    tasks.append(new_task)
    save_tasks(tasks)
    print(f'Task Added with ID: {task_id}')

# Update a task by its ID
def update_task(task_id, description):
    tasks = load_tasks()
    task_update = None
    for task in tasks:
        if task["id"]== task_id:
            task['description'] = description
            task_update = task     
            break 
    if task_update:
        save_tasks(tasks)
        print(f"Task with ID: {task_id} has been updated.")

def update_task_status(task_id, status):
    tasks = load_tasks()
    task_update = None
    for task in tasks:
        if task["id"] == task_id:
            task['status'] = status
            task_update = task
            break
    if task_update:
        save_tasks(tasks)
        print(f"Task with ID: {task_id} has been updated with new status: {status}.")


# Delete a task by its ID
def delete_task(task_id):
    tasks = load_tasks()
    tasks_delete = None
    for task in tasks:
        if task["id"] == task_id:
            tasks_delete = task
            break
    if tasks_delete:
        tasks.remove(tasks_delete)
        save_tasks(tasks)
        print(f"Task with ID: {task_id} has been deleted.")
    
def main():
    print("Welome ")
    while True:
        print("Choose an Option:")
        print("1. Veiw_Available_tasks.")
        print("2. Add_Task.\n3. Update_Task.\n4. Update_Task_Status.\n5. Delete_Task.\n6. Exit.")
        choice = int(input("Enter Your choice: "))
        match  choice:
            case 1: 
                print("Available Tasks:")
                tasks = load_tasks()
                if not tasks:
                    print("No tasks found.")
                else:
                    for task in tasks:
                        print(f'ID:{task["id"]}, Description: {task["description"]}, Created At: {task["current_time"]}, Status: {task["status"]}')
            case 2: 
                description = input("Enter Task Description: ")
                add_tasks(description)
            case 3:
                task_id = int(input("Enter Task ID to update: "))
                description = input("Enter new Task Description: ")
                update_task(task_id, description)
            case 4:
                task_id = int(input("Enter Task ID to update status: "))
                status = input("Enter new Task Status: ")
                update_task_status(task_id, status)

            case 5: 
                task_id = int(input("Enter Task ID to delete:"))
                delete_task(task_id)
            case 6:
                print("Thank You for using Task Manager. Goodbye!")
                sys.exit(0)
            case _:
                print("Invalid choice. Please try again.")
if __name__ == "__main__":
    main()