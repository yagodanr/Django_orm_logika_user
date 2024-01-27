import django_setup
from project2.models import User


def inserts():
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


def main():
    inserts()

if __name__ == "__main__":
    main()