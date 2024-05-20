import uuid
from datetime import datetime,timedelta
from enum import Enum

class Priority(Enum):
    CRITICAL = 1
    HIGH = 2
    MEDIUM = 3
    LOW = 4

class Status(Enum):
    BACKLOG = 1
    TODO = 2
    DOING = 3
    DONE = 4
    ARCHIVED = 5
class Task:
    def __init__(self, title='', description='', assigned_to=None, priority=Priority.LOW, status=Status.BACKLOG):
        self.task_id = str(uuid.uuid4())
        self.title = title
        self.description = description
        self.start_time = datetime.now()
        self.end_time = self.start_time + timedelta(hours=24)
        self.assigned_to = assigned_to if assigned_to is not None else []
        self.priority = priority
        self.status = status
        self.history = []
        self.comments = [] 
        
    def assign_member(self, username):
        if username not in self.assigned_to:
            self.assigned_to.append(username)
            self.history.append(username, datetime.now())

    def unassign_member(self, username):
        if username in self.assigned_to:
            self.assigned_to.remove(username)
            self.history.append(username, datetime.now())
