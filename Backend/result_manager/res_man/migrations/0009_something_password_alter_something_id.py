# Generated by Django 5.0.6 on 2024-07-01 20:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('res_man', '0008_rename_name2_something_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='something',
            name='password',
            field=models.CharField(default=' ', max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='something',
            name='id',
            field=models.CharField(max_length=100, primary_key=True, serialize=False),
        ),
    ]
