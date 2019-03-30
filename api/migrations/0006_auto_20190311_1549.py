# Generated by Django 2.1.5 on 2019-03-11 15:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_roomavailability_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='roomavailability',
            name='status',
            field=models.CharField(choices=[('bk', 'Booked'), ('pr', 'Processing')], help_text='Status', max_length=2),
        ),
    ]
