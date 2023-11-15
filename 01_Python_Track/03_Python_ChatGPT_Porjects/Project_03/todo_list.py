# Link for Planing : https://miro.com/app/board/uXjVNPgia48=/?moveToWidget=3458764569746121723&cot=14
# Project_03 Todo List

# Initialize the list of tasks
task_list = []

while True:
    # Get user input for the command
    user_command = input("Enter a command (add, remove, view, exit): ")
    valid_commands = ["add", "remove", "view", "exit"]

    # Check if the user command is not in the valid choices
    if user_command not in valid_commands:
        print("Please enter a valid command.")
        continue  # Restart the loop

    # Add a new task
    if user_command == "add":
        new_task = input("Enter the task you want to add: ")
        task_list.append(new_task)
        print(f"Task '{new_task}' has been added successfully.")

    # View tasks
    elif user_command == "view":
        if task_list:
            print("Your tasks are: ")
            # Display the items in the task list
            for idx, task in enumerate(task_list, start=1):
                print(f"{idx}. {task}")
        else:
            print("There are no tasks. Feel free to add some!")

    # Remove a task
    elif user_command == "remove":
        if task_list:
            print("Current tasks: ")
            for idx, task in enumerate(task_list, start=1):
                print(f"{idx}. {task}")

            while True:
                task_index = input("Enter the number of the task you want to remove or 0 to remove the last task: ")

                try:
                    task_index = int(task_index)
                    removed_task = task_list.pop(task_index - 1)
                    print(f"Task '{removed_task}' has been removed.")
                    break  # Exit the loop if removal is successful
                except (ValueError, IndexError):
                    print("Invalid input. Please enter a valid task number.")
        else:
            print("There are no tasks to remove.")

    # Exit the program
    else:
        print("Thank you! Have a productive day.")
        break  # Use 'break' to exit the loop

# End of the program