# Generated by Django 4.1.4 on 2023-05-09 06:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_alter_contact_message_alter_contact_name_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contact',
            old_name='name',
            new_name='username',
        ),
    ]
