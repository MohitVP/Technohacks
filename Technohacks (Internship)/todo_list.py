class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)
        print("Task added: {}".format(task))

    def remove_task(self, task):
        if task in self.tasks:
            self.tasks.remove(task)
            print("Task removed: {}".format(task))
        else:
            print("Task not found: {}".format(task))

    def display_tasks(self):
        if self.tasks:
            print("Tasks:")
            for index, task in enumerate(self.tasks, start=1):
                print("{}. {}".format(index, task))
        else:
            print("No tasks found.")

def main():
    todo_list = ToDoList()
    while True:
        print("\n==== To-Do List ====")
        print("1. Add Task")
        print("2. Remove Task")
        print("3. Display Tasks")
        print("4. Exit")
        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            task = input("Enter the task: ")
            todo_list.add_task(task)
        elif choice == "2":
            task = input("Enter the task to remove: ")
            todo_list.remove_task(task)
        elif choice == "3":
            todo_list.display_tasks()
        elif choice == "4":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
