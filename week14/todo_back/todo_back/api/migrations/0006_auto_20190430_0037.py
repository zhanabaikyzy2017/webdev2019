# Generated by Django 2.2 on 2019-04-29 18:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_auto_20190429_2334'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='due_on',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
