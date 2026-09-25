tasks = []
 
while 'true':
    print("\n---MY TO-DO LIST ---")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Remove Task")
    print("4. Exit")

    choice = input("Choose 1-4:")

    if choice == "1": 
         task = input("Enter your task:")
         tasks.append(task)
         print(f"Added:{task}")
     
    elif choice =="2":
        if len(tasks) ==0:
            print("No tasks yet! Add one.")
        else:
            print("\nYour Tasks:")
            for i, t in enumerate(tasks,1):
                print(f"{i}. {t}")

    elif choice == "3":
         if len(tasks) ==0:
            print("No tasks to remove.")
         else:
            num=int(input("Enter task number to remove:"))
            removed = tasks.pop(num-1)
            print(f"Removed: {removed}")

    elif choice == "4":
        print("Bye! Your tasks are saved for this session.")
        break

    else:
        print("Wrong choice! Choose 1-4.")


