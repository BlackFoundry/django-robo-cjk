# Generated by Django 3.1.7 on 2021-03-01 17:20

from django.db import migrations, models
import robocjk.validators


class Migration(migrations.Migration):

    dependencies = [
        ('robocjk', '0005_font_designspace'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='repo_url',
            field=models.CharField(help_text='The .git repository SSH URL, eg. git@github.com:username/repository.git', max_length=200, unique=True, validators=[robocjk.validators.GitSSHRepositoryURLValidator()], verbose_name='Repo URL'),
        ),
    ]