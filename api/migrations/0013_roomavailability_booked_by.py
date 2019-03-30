# Generated by Django 2.1.5 on 2019-03-17 10:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('api', '0012_auto_20190316_1940'),
    ]

    operations = [
        migrations.AddField(
            model_name='roomavailability',
            name='booked_by',
            field=models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
