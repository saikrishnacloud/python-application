import json
import os

# File where tasks will be stored
DATA_FILE = "tasks.json"

def load_tasks():
    """Load tasks from the JSON file. Return an empty list if file doesn't exist."""
    if not os.path.exists(DATA_FILE):
        return []
    try:
        with open(DATA_FILE, "r") as file:
            return json.load(file)
    except json.JSONDecodeError:
        return []

def save_tasks(tasks):
    """Save the current list of tasks to the JSON file."""
    with open(DATA_FILE, "w") as file:
        json.dump(tasks, file, indent=4)

def add_task(tasks):
    """Prompt the user to add a new task."""
    title = input("\nEnter task title: ").strip()
    if title:
        task = {"id": len(tasks) + 1, "title": title, "completed": False}
        tasks.append(task)
        save_tasks(tasks)
        print(f"🎉 Task '{title}' added successfully!")
    else:
        print("⚠️ Task title cannot be empty.")

def list_tasks(tasks):
    """Display all tasks with their completion status."""
    if not tasks:
        print("\n📭 No tasks found.")
        return

    print("\n--- Current Tasks ---")
    for task in tasks:
        status = "✅ Done" if task["completed"] else "❌ Pending"
        print(f"{task['id']}. {task['title']} [{status}]")

def complete_task(tasks):
    """Mark a specific task as completed."""
    list_tasks(tasks)
    if not tasks:
        return
        
    try:
        task_id = int(input("\nEnter the ID of the task to complete: "))
        for task in tasks:
            if task["id"] == task_id:
                task["completed"] = True
                save_tasks(tasks)
                print(f"👍 Task {task_id} marked as complete!")
                return
        print("⚠️ Task ID not found.")
    except ValueError:
        print("⚠️ Please enter a valid number.")

def delete_task(tasks):
    """Remove a task from the list."""
    list_tasks(tasks)
    if not tasks:
        return

    try:
        task_id = int(input("\nEnter the ID of the task to delete: "))
        for i, task in enumerate(tasks):
            if task["id"] == task_id:
                removed = tasks.pop(i)
                # Re-index remaining tasks to keep IDs clean
                for index, t in enumerate(tasks):
                    t["id"] = index + 1
                save_tasks(tasks)
                print(f"🗑️ Removed task: '{removed['title']}'")
                return
        print("⚠️ Task ID not found.")
    except ValueError:
        print("⚠️ Please enter a valid number.")

def main():
    """Main application loop."""
    tasks = load_tasks()

    while True:
        print("\n=== Python Task Manager ===")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Mark Task Complete")
        print("4. Delete Task")
        print("5. Exit")
        
        choice = input("Choose an option (1-5): ").strip()

        if choice == "1":
            list_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            complete_task(tasks)
        elif choice == "4":
            delete_task(tasks)
        elif choice == "5":
            print("\nGoodbye! Thanks for using Task Manager.")
            break
        else:
            print("⚠️ Invalid choice. Please pick a number from 1 to 5.")

if __name__ == "__main__":
    main()

