# Generated by Django 5.1.1 on 2024-09-17 03:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0005_intermidiate_skill_model_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='intermidiate_interest_model',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('interest_name', models.CharField(max_length=100, null=True)),
            ],
        ),
    ]
