# Generated by Django 4.0.3 on 2022-04-11 07:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('awardx', '0011_alter_profile_options_alter_project_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='image2',
            field=models.ImageField(null=True, upload_to='projects/'),
        ),
    ]