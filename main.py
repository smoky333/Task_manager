
class Task:
    def __init__(self):
        self.tasks = []

    def add_task(self, description, deadline):
        task = {"description": description, "deadline": deadline, "status": "Uncompleted"}
        self.tasks.append(task)

    def delete_task(self, description):
        for task in self.tasks:
            if task["description"] == description:
                self.tasks.remove(task)


    def complete_task(self, description):
        for task in self.tasks:
            if task["description"] == description:
                task["status"] = "completed"
                print(f"Task {task['description']} is completed")
            else:
                print(f"Task {task['description']} is not completed")

    def print_tasks(self):
        for task in self.tasks:
            if task["status"] == "Uncompleted":
                print(f"Task: {task['description']}, Deadline: {task['deadline']}")


tasks = Task()
tasks.add_task("Go shoping", "2024-08-31")
tasks.add_task("Go fishing", "2024-08-25")
tasks.add_task("Play football", "2024-1-31")
tasks.print_tasks()

tasks.complete_task("Go fishing")
tasks.print_tasks()

tasks.delete_task("Play football")
tasks.print_tasks()

