class Task:
    def __init__(self, task_id: int, description: str, status: str):
        self.task_id = task_id
        self.description = description
        self.status = status

    def update_status(self, new_status: str):
        self.status = new_status
