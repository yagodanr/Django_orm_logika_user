# Generated by Django 5.0.1 on 2024-01-27 17:10

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project2', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=127)),
                ('description', models.TextField()),
                ('status', models.CharField(choices=[('IP', 'in progress'), ('D', 'done'), ('A', 'assigned')], max_length=31)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tasks', to='project2.user')),
            ],
        ),
    ]