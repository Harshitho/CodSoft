tasks = []

def add_task(task):
    tasks.append(task)
    print(f'Task "{task}" added successfully!')

def view_tasks():
    if not tasks:
        print('No tasks found.')
    else:
        print('To-Do List:')
        for i, task in enumerate(tasks, start=1):
            print(f'{i}. {task}')

def remove_task(task_number):
    try:
        task_number = int(task_number)
        if task_number <= 0 or task_number > len(tasks):
            print('Invalid task number. Please enter a valid task number.')
        else:
            removed_task = tasks.pop(task_number - 1)
            print(f'Task "{removed_task}" removed successfully!')
    except ValueError:
        print('Invalid input. Please enter a valid task number.')

while True:
    print('\nOptions:')
    print('1. Add a task')
    print('2. View tasks')
    print('3. Remove a task')
    print('4. Quit')
    
    choice = input('Enter your choice: ')
    
    if choice == '1':
        task = input('Enter the task: ')
        add_task(task)
    elif choice == '2':
        view_tasks()
    elif choice == '3':
        task_number = input('Enter the task number to remove: ')
        remove_task(task_number)
    elif choice == '4':
        print('Goodbye!')
        break
    else:
        print('Invalid choice. Please choose a valid option.')
