# Generated by Django 3.2.7 on 2021-10-19 14:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('robocjk', '0012_auto_20211019_1307'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='repo_branch',
            field=models.CharField(default='master', max_length=50, verbose_name='Repo branch'),
        ),
    ]
