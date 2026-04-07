# Task Manager CLI

A simple Python-based Command Line Interface (CLI) Task Manager application that allows users to add, view, update, delete, and manage task statuses using a JSON file.

## Features

* Add new tasks
* View all available tasks
* Update task descriptions
* Update task status
* Delete tasks
* Automatically assign task IDs
* Store tasks in a JSON file
* Track task creation time
* Beginner-friendly Python project

## Tech Stack

* Python
* JSON
* File Handling
* Datetime Module
* CLI (Command Line Interface)

## Project Structure

```bash
task-manager/
│
├── main.py
├── tasks.json
├── README.md
```

## Task Structure

Each task is stored inside the `tasks.json` file in the following format:

```json
{
  "id": 1,
  "description": "Complete backend project",
  "current_time": "2026-04-07 10:30:00",
  "status": "ToDo"
}
```

## Functionalities

### 1. View Available Tasks

Displays all tasks with:

* Task ID
* Description
* Creation Time
* Status

Example Output:

```bash
ID:1, Description: Complete backend project, Created At: 2026-04-07 10:30:00, Status: ToDo
```

### 2. Add a Task

Users can add a new task by entering a description.

Example:

```bash
Enter Task Description: Complete Python assignment
```

### 3. Update a Task

Users can update the description of an existing task using the task ID.

Example:

```bash
Enter Task ID to update: 1
Enter new Task Description: Complete Python backend assignment
```

### 4. Update Task Status

Users can change the status of a task.

Example:

```bash
Enter Task ID to update status: 1
Enter new Task Status: Done
```

Common statuses:

* ToDo
* In Progress
* Done

### 5. Delete a Task

Users can remove a task using its task ID.

Example:

```bash
Enter Task ID to delete: 1
```

## Menu Options

```bash
Choose an Option:
1. View_Available_Tasks
2. Add_Task
3. Update_Task
4. Update_Task_Status
5. Delete_Task
6. Exit
```
## Example Workflow

```bash
Choose an Option:
1. View_Available_Tasks
2. Add_Task
3. Update_Task
4. Update_Task_Status
5. Delete_Task
6. Exit

Enter Your choice: 2
Enter Task Description: Complete README file
Task Added with ID: 1

Enter Your choice: 1
ID:1, Description: Complete README file, Created At: 2026-04-07 11:20:00, Status: ToDo
```

## Error Handling

* Handles missing `tasks.json` file
* Handles invalid JSON format in `tasks.json`
* Handles file saving errors

## Project Outcomes

By building this project, I have learned:

* How to work with Python functions
* How to use JSON files for data storage
* How to perform CRUD operations
* How to handle file operations in Python
* How to use loops and conditional statements
* How to work with Python dictionaries and lists
* How to build a simple CLI-based application
* How to handle exceptions and errors
* How to structure a beginner-friendly Python project


## Author

Deepak Vattipalli
Aspiring Backend Developer | Python Learner
