# Improved Todo List Program (Project_03) after enhancements with ChatGPT

def get_valid_command():
    """
    Get a valid user command.
    """
    valid_commands = ["add", "remove", "view", "exit"]
    while True:
        user_command = input("Enter a command (add, remove, view, exit): ").lower()
        if user_command in valid_commands:
            return user_command
        else:
            print("Please enter a valid command.")

def add_task(task_list):
    """
    Add a new task to the task list.
    """
    new_task = input("Enter the task you want to add: ")
    task_list.append(new_task)
    print(f"Task '{new_task}' has been added successfully.")

def view_tasks(task_list):
    """
    View the current tasks in the task list.
    """
    if task_list:
        print("Your tasks are: ")
        for idx, task in enumerate(task_list, start=1):
            print(f"{idx}. {task}")
    else:
        print("There are no tasks. Feel free to add some!")

def remove_task(task_list):
    """
    Remove a task from the task list.
    """
    if task_list:
        print("Current tasks: ")
        for idx, task in enumerate(task_list, start=1):
            print(f"{idx}. {task}")

        while True:
            task_index = input("Enter the number of the task you want to remove: ")

            try:
                task_index = int(task_index)
                removed_task = task_list.pop(task_index - 1)
                print(f"Task '{removed_task}' has been removed.")
                break  # Exit the loop if removal is successful
            except (ValueError, IndexError):
                print("Invalid input. Please enter a valid task number.")
    else:
        print("There are no tasks to remove.")

def main():
    """
    Main function to run the todo list program.
    """
    task_list = []

    while True:
        user_command = get_valid_command()

        if user_command == "add":
            add_task(task_list)
        elif user_command == "view":
            view_tasks(task_list)
        elif user_command == "remove":
            remove_task(task_list)
        else:
            print("Thank you! Have a productive day.")
            break  # Use 'break' to exit the loop

if __name__ == "__main__":
    main()
