from project.task import Task


class Section:
    def __init__(self, name: str):
        self.name = name
        self.tasks = []

    def add_task(self, new_task: 'Task'):
        if new_task in self.tasks:
            return f"Task is already in the section {self.name}"
        self.tasks.append(new_task)
        return f"Task {new_task.details()} is added to the section"

    def complete_task(self, task_name: str):
        for task in self.tasks:
            if task.name == task_name:
                task.completed = True
                return f"Completed task {task_name}"
        return f"Could not find task with the name {task_name}"

    def clean_section(self):
        removed_tasks = [task for task in self.tasks if task.completed]
        self.tasks = [task for task in self.tasks if not task.completed]
        return f"Cleared {len(removed_tasks)} tasks."

    def view_section(self):
        section_info = f"Section {self.name}:\n"
        tasks_info = "\n".join(task.details() for task in self.tasks)
        return section_info + tasks_info