tasks = []

def view_tasks():
    if len(tasks) == 0:
        print('Your task list is empty!')
        print('Choose "2" to add a task!')

    else:
        for number, task in enumerate(tasks, start=1):
            print(number, task)

def add_task():
    task = input('Enter task: ')
    tasks.append(task)
    print('Task added successfully\n')
    for number, task in enumerate(tasks, start=1):
        print(number, task)

def remove_task():
    if len(tasks) == 0:
        print('Your task list is empty!')
        print('Choose "2" to add a task')
    else:
        for number, task in enumerate(tasks, start=1):
            print(number, task)

        task = input('Enter the task number you desire to remove: ')

        try:
            task = int(task)
            tasks.pop(task - 1)
            print('Task removed successfully!\n')

        except ValueError:
            print('Enter a valid task number!')

        for number, task in enumerate(tasks, start=1):
            print(number, task)
        
def show_menu():
    return '''
1. View Tasks
2. Add a Task
3. Remove a Task
4. Exit'''

def start_task_manager():
    while True:
        menu = show_menu()
        print(menu)        
        choice = input('Enter your choice: ')
        
        try:
            choice = int(choice)

            if choice == 1:
                view_tasks()

            elif choice == 2:
                add_task()
            
            elif choice == 3:
                remove_task()

            else: # or elif choice == 4: 
                print('Goodbye!')
                break

        except ValueError:
            return 'Please enter a valid choice!'

def main():
    print('Welcome to Task Manager!')
    start_task_manager()

if __name__ == "__main__":
    main()
