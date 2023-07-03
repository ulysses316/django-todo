from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()

# Create your models here.
class Task(models.Model):
    title = models.CharField(max_length=50)
    deadline = models.DateField(auto_now=False, auto_now_add=False)
    description = models.TextField()
    creation = models.DateField(auto_now=False, auto_now_add=True)
    modified = models.DateField(auto_now=True, auto_now_add=False)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='owned_tasks')
    supervisor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='supervised_tasks')
    accepted = models.BooleanField(default=False)
    state = models.CharField(max_length=15, null=False, choices=(
            ("pending", "Pending"),
            ("overdue", "Overdue"),
            ("inProgress", "In progress"),
            ("awaiting", "Awaiting review"),
            ("approved", "Approved"),
            ("rejected", "Rejected"),
        )
    )

    def __str__(self):
        return self.title