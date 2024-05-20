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

    def add_comment(self, username, comment):
        self.comments.append((username, comment, datetime.now()))
    
    def update_task(self, user, title=None, description=None, end_time=None, priority=None, status=None):
        if user in self.assigned_to or user == self.leader:
            if title:
                self.title = title
            if description:
                self.description = description
            if end_time:
                self.end_time = end_time
            if priority:
                self.priority = priority
            if status:
                self.status = status
            self.history.append((user, datetime.now(), "Updated task details"))
        else:
            print("Only assigned members or the project leader can update the task.")

    def view_task_details(self):
        print(f"Task ID: {self.task_id}")
        print(f"Title: {self.title}")
        print(f"Description: {self.description}")
        print(f"Start Time: {self.start_time}")
        print(f"End Time: {self.end_time}")
        print(f"Assigned To: {', '.join(self.assigned_to)}")
        print(f"Priority: {self.priority.value}")
        print(f"Status: {self.status.value}")
        print("History:")
        for record in self.history:
            print(f"- {record}")
        print("Comments:")
        for comment in self.comments:
            print(f"- {comment}")

class Project:
    def __init__(self, project_id, title, leader):
        self.project_id = project_id
        self.title = title
        self.leader = leader
        self.members = []

    def add_member(self, username):
        if username != self.leader and username not in self.members:
            self.members.append(username)


    def remove_member(self, username):
        if username in self.members:
            self.members.remove(username)
        else:
            print(f"User {username} is not a member of this project.")

    def delete_project(self):
        print(f"Project '{self.title}' has been deleted.")
        del self


class Users:
    def __init__(self, username):
        self.username = username

    def create_project(self, project_id, title):
        new_project = Project(project_id, title, self.username)
        print(f"Project '{title}' created by {self.username}.")
        return new_project

    def create_task(self, project, title='', description='', priority=Priority.LOW, status=Status.BACKLOG):
        if self.username == project.leader:
            new_task = Task(title, description, priority=priority, status=status)
            project.add_task(new_task)
            return new_task
        else:
            print("Only the leader can create tasks.")

    def assign_task_member(self, project, task_id, username):
        task = next((task for task in project.tasks if task.task_id == task_id), None)
        if task and self.username == project.leader:
            if username in project.members:
                task.assign_member(username)
            else:
                print(f"User {username} is not a member of the project.")
        else:
            print("Only the leader can assign members to tasks.")

    def unassign_task_member(self, project, task_id, username, username1):
        task = next((task for task in project.tasks if task.task_id == task_id), None)
        if task and self.username == project.leader:
            if username1 in project.members:
                task.unassign_member(username1)
            else:
                print(f"User {username1} is not a member of the project.")
        else:
            print("Only the leader can unassign members from tasks.")

    def view_leader_projects(self, projects):
        leader_projects = [proj for proj in projects if proj.leader == self.username]
        print("Leader`s Projects:")
        for proj in leader_projects:
            print(f"- {proj.title}")

    def view_member_projects(self, projects):
        member_projects = [proj for proj in projects if self.username in proj.members]
        print("Member`s Projects:")
        for proj in member_projects:
            print(f"- {proj.title}")

    def view_project_details(self, project):
        print(f"Project ID: {project.project_id}")
        print(f"Title: {project.title}")
        print(f"Leader: {project.leader}")
        print("Members:")
        for member in project.members:
            print(f"- {member}")
        print("Tasks:")
        for task in project.tasks:
            print(f"- {task.title} [{task.status.value}]")

    def view_task_details(self, project, task_id):
        task = next((task for task in project.tasks if task.task_id == task_id), None)
        if task:
            task.view_task_details()
        else:
            print(f"Task with ID {task_id} not found.")

    def update_task(self, project, task_id, title=None, description=None, end_time=None, priority=None, status=None):
        task = next((task for task in project.tasks if task.task_id == task_id), None)
        if task:
            task.update_task(self.username, title, description, end_time, priority, status)
        else:
            print(f"Task with ID {task_id} not found.")


