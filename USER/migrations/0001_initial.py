# Generated by Django 5.0.7 on 2024-07-29 15:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='user',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Username', models.CharField(max_length=20, verbose_name='Имя пользователя')),
                ('User_password', models.CharField(max_length=20, verbose_name='Пароль пользователя')),
            ],
        ),
    ]
