import os
import django
import random
from faker import Faker

# Django Settings
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')
django.setup()

from tracker.models import User, Category, Transaction

fake = Faker()

# Create Fake Users
def create_fake_users(n):
    for _ in range(n):
        user = User.objects.create_user(
            username=fake.user_name(),
            email=fake.email(),
            password='password'
        )
        user.save()


#Create Fake Categories
def create_fake_categories():
    categories = ['Food', 'Travel', 'Health', 'Entertainment', 'Utilities']
    for category in categories:
        cat = Category(name=category)
        cat.save()


#Create Fake Transactions
def create_fake_transactions(n):
    users = User.objects.all()
    categories = Category.objects.all()
    for _ in range(n):
        user = random.choice(users)
        category = random.choice(categories)
        transaction_type = random.choice(['income', 'expense'])
        amount = round(random.uniform(10.0, 1000.0), 2)
        date = fake.date_this_year()

        transaction = Transaction(
            user=user,
            category=category,
            type=transaction_type,
            amount=amount,
            date=date
        )
        transaction.save()

if __name__ == "__main__":
    print("Creating fake users...")
    create_fake_users(10)
    print("Creating fake categories...")
    create_fake_categories()
    print("Creating fake transactions...")
    create_fake_transactions(50)
    print("Data seeding complete.")
