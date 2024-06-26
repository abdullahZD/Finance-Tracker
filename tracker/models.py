from django.db import models
from django.contrib.auth.models import AbstractUser

# User Model
class User(AbstractUser):
    pass

# Category Model
class Category(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True) 
    name = models.CharField(max_length=50)
    default = models.BooleanField(default=False)  

    class Meta:
        verbose_name_plural = 'Categories'
        unique_together = ('user', 'name')  
    def __str__(self):
        return self.name

# Transaction Model
class Transaction(models.Model):
    TRANSACTION_CHOICES_TYPE = (
        ('income', 'Income'),
        ('expense', 'Expense'),
    )
    
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    type = models.CharField(max_length=7, choices=TRANSACTION_CHOICES_TYPE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField()

    def __str__(self):
        return f"{self.type} of {self.amount} on {self.date} by {self.user}"
