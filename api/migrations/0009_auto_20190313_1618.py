# Generated by Django 2.1.5 on 2019-03-13 16:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0008_user_info'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user_info',
            name='user',
        ),
        migrations.DeleteModel(
            name='User_info',
        ),
    ]
