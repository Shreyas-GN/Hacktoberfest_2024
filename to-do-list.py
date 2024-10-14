def todo_list():
    tasks = []  # Initialize an empty list to store tasks

    while True:
        print("\nTo-Do List")
        print("1. Add Task")
        print("2. Remove Task")
        print("3. View Tasks")
        print("4. Exit")

        choice = input("Choose an option (1-4): ")

        if choice == '1':
            task = input("Enter the task: ")
            tasks.append(task)  # Add the task to the list
            print(f"Added task: {task}")
        
        elif choice == '2':
            task = input("Enter the task to remove: ")
            if task in tasks:
                tasks.remove(task)  # Remove the task from the list
                print(f"Removed task: {task}")
            else:
                print("Task not found.")
        
        elif choice == '3':
            print("Tasks:")
            for i, task in enumerate(tasks, start=1):
                print(f"{i}. {task}")  # Display tasks with their index
        
        elif choice == '4':
            print("Exiting the To-Do List application.")
            break  # Exit the loop
        
        else:
            print("Invalid choice. Please choose a valid option.")

# Call the function to start the To-Do List application
todo_list()
