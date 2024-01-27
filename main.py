import django_setup
from project2.models import User, Task


def inserts_users():
    user = User(
        login="user1",
        email="user1@gmail.com",
        role="user",
    )
    user.save()
    
    
    admin = User(
        login="admin",
        email="admin@gmail.com",
        role="admin"
    )
    admin.save()

def inserts_tasks():
    user = User.objects.get(id=1)
    
    u_task = Task(
        name="Buy chocolate",
        description="For a cake",
        status="assigned",
        user_id=user
    )
    u_task.save()
    
    admin = User.objects.get(id=2)
    
    a_task = Task(
        name="Programming lesson",
        description="Logika",
        status="in progress",
        user_id=admin
    )
    a_task.save()    
    
    
    
def main():
    inserts_tasks()

if __name__ == "__main__":
    main()