# Generated by Django 5.0.6 on 2024-06-30 18:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('res_man', '0002_remove_student_roll_no_alter_student_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='id',
            field=models.CharField(max_length=100, primary_key=True, serialize=False),
        ),
    ]
