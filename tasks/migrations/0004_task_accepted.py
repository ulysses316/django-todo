# Generated by Django 4.2.2 on 2023-07-03 01:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0003_alter_task_state'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='accepted',
            field=models.BooleanField(default=True),
        ),
    ]