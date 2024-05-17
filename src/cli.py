import click
from .infrastructure.mysql_user_repository import MySQLUserRepository
from .infrastructure.mysql_task_repository import MySQLTaskRepository
from .application.update_user_service import UpdateUserService
from .application.update_task_service import UpdateTaskService

@click.group()
def cli():
    pass

@click.command()
@click.argument('user_id', type=int)
@click.argument('new_email', type=str)
def update_user(user_id, new_email):
    user_repo = MySQLUserRepository()
    service = UpdateUserService(user_repo)
    service.update_user_email(user_id, new_email)
    click.echo(f"Updated user {user_id}'s email to {new_email}")

@click.command()
@click.argument('task_id', type=int)
@click.argument('new_status', type=str)
def update_task(task_id, new_status):
    task_repo = MySQLTaskRepository()
    service = UpdateTaskService(task_repo)
    service.update_task_status(task_id, new_status)
    click.echo(f"Updated task {task_id}'s status to {new_status}")

cli.add_command(update_user)
cli.add_command(update_task)

if __name__ == '__main__':
    cli()
