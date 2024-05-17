from abc import ABC, abstractmethod
from ..models.task import Task

class TaskRepository(ABC):
    @abstractmethod
    def get_task(self, task_id: int) -> Task:
        pass

    @abstractmethod
    def update_task(self, task: Task) -> None:
        pass
