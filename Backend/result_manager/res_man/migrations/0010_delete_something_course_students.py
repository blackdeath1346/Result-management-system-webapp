# Generated by Django 5.0.6 on 2024-07-01 20:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('res_man', '0009_something_password_alter_something_id'),
    ]

    operations = [
        migrations.DeleteModel(
            name='something',
        ),
        migrations.AddField(
            model_name='course',
            name='students',
            field=models.ManyToManyField(to='res_man.student'),
        ),
    ]
