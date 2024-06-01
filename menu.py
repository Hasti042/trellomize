# 0.1.0
# ****************************************************** all of this for menu becouse wo havent got any web page or app and we working in cmd 
import datetime
import loging as lo
import maneger as m
from trello import Project as pr
from trello import Task as ts
from trello import Priority, Status

projects = {}
current_user = None

while True:
    lo.clear()
    print('Haven\'t got an account? Register first by pressing R.')
    print('Press L to login.')
    print('Press C to change password or if you forgot your password.')
    print('Press S to set super user or create admin account.')
    print('Press Q to quit application.')
    print('Press T to see telegram support bot.')
    print('Press P to access the project section.')
    print('Press B to access the task section.')
    choice = input('Enter your choice: ').upper()
    lo.clear()
    
    if choice == 'L':
        current_user = lo.Loging_System.logging()
    elif choice == 'R':
        lo.Loging_System.Register()
    elif choice == 'C':
        lo.Loging_System.change_password()
    elif choice == 'T':
        print('If you want more support or to connect to our admin, please use this link: https://t.me/iust_BOT_bot')
    elif choice == 'S':
        m.SystemAdmin.create_admin()
    elif choice == 'Q':
        break
    elif choice == 'P':
        project_choice = input('Press M to make a project.\nPress A to add a member to a project.\nPress R to remove a member from a project.\nPress D to delete a project.\nEnter your choice: ').upper()
        if project_choice == 'M':
            id = input('Please enter the project ID: ')
            title = input('Please enter the project title: ')
            leader = current_user
            project = pr(id, title, leader)
            projects[id] = project
            print(f'Project {title} created.')
        elif project_choice == 'A':
            project_id = input('Please enter the project ID: ')
            username = input('Please enter the username: ')
            project = projects.get(project_id)
            if project:
                project.add_member(username)
                print(f'User {username} added to project {project_id}.')
            else:
                print('Project not found.')
        elif project_choice == 'R':
            project_id = input('Please enter the project ID: ')
            username = input('Please enter the username: ')
            project = projects.get(project_id)
            if project:
                project.remove_member(username)
                print(f'User {username} removed from project {project_id}.')
            else:
                print('Project not found.')
        elif project_choice == 'D':
            project_id = input('Please enter the project ID: ')
            project = projects.pop(project_id, None)
            if project:
                project.delete_project()
                print(f'Project {project_id} deleted.')
            else:
                print('Project not found.')
        else:
            print('Invalid choice.')
    elif choice == 'B':
        task_choice = input('Press M to make a task.\nPress A to assign a member to a task.\nPress R to unassign a member from a task.\nPress D to add a comment to a task.\nPress U to update a task.\nPress V to view task details.\nEnter your choice: ').upper()
        if task_choice == 'M':
            project_id = input('Please enter the project ID: ')
            project = projects.get(project_id)
            if project and current_user == project.leader:
                title = input('Please enter the task title: ')
                description = input('Please enter the task description: ')
                priority = input('Please enter the task priority (CRITICAL/HIGH/MEDIUM/LOW): ').upper()
                status = input('Please enter the task status (BACKLOG/TODO/DOING/DONE/ARCHIVED): ').upper()
                task = ts(title, description, priority=Priority[priority], status=Status[status])
                print(f'{task.uuid_getter()} is your task ID.')
                project.add_task(task)
                print(f'Task {title} created.')
            else:
                print('Only the project leader can create tasks or project not found.')
        elif task_choice == 'A':
            project_id = input('Please enter the project ID: ')
            project = projects.get(project_id)
            if project and current_user == project.leader:
                task_id = input('Please enter the task ID: ')
                username = input('Please enter the username: ')
                task = next((task for task in project.tasks if task.task_id == task_id), None)
                if task and username in project.members:
                    task.assign_member(username)
                    print(f'User {username} assigned to task {task_id}.')
                else:
                    print('Task not found or user not a member of the project.')
            else:
                print('Only the project leader can assign members or project not found.')
        elif task_choice == 'R':
            project_id = input('Please enter the project ID: ')
            project = projects.get(project_id)
            if project and current_user == project.leader:
                task_id = input('Please enter the task ID: ')
                username = input('Please enter the username: ')
                task = next((task for task in project.tasks if task.task_id == task_id), None)
                if task and username in task.assigned_to:
                    task.unassign_member(username)
                    print(f'User {username} unassigned from task {task_id}.')
                else:
                    print('Task not found or user not assigned to the task.')
            else:
                print('Only the project leader can unassign members or project not found.')
        elif task_choice == 'D':
            project_id = input('Please enter the project ID: ')
            project = projects.get(project_id)
            if project:
                task_id = input('Please enter the task ID: ')
                task = next((task for task in project.tasks if task.task_id == task_id), None)
                if task:
                    comment = input('Please enter your comment: ')
                    task.add_comment(current_user, comment)
                    print('Comment added to task.')
                else:
                    print('Task not found.')
            else:
                print('Project not found.')
        elif task_choice == 'U':
            project_id = input('Please enter the project ID: ')
            project = projects.get(project_id)
            if project:
                task_id = input('Please enter the task ID: ')
                task = next((task for task in project.tasks if task.task_id == task_id), None)
                if task:
                    title = input('Enter new title (leave blank to keep current): ')
                    description = input('Enter new description (leave blank to keep current): ')
                    end_time_str = input('Enter new end time (YYYY-MM-DD HH:MM:SS, leave blank to keep current): ')
                    end_time = datetime.strptime(end_time_str, '%Y-%m-%d %H:%M:%S') if end_time_str else None
                    priority_str = input('Enter new priority (CRITICAL/HIGH/MEDIUM/LOW, leave blank to keep current): ').upper()
                    priority = Priority[priority_str] if priority_str else None
                    status_str = input('Enter new status (BACKLOG/TODO/DOING/DONE/ARCHIVED, leave blank to keep current): ').upper()
                    status = Status[status_str] if status_str else None
                    task.update_task(current_user, title, description, end_time, priority, status, project.leader)
                    print('Task updated.')
                else:
                    print('Task not found.')
            else:
                print('Project not found.')
        elif task_choice == 'V':
            project_id = input('Please enter the project ID: ')
            project = projects.get(project_id)
            if project:
                task_id = input('Please enter the task ID: ')
                task = next((task for task in project.tasks if task.task_id == task_id), None)
                if task:
                    task.view_task_details()
                else:
                    print('Task not found.')
            else:
                print('Project not found.')
        else:
            print('Invalid choice.')
    else:
        print('Invalid choice.')

    input('Press any key to continue...')
