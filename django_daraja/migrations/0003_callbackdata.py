# Generated by Django 5.1.5 on 2025-01-22 07:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('django_daraja', '0002_auto_20181108_1219'),
    ]

    operations = [
        migrations.CreateModel(
            name='CallbackData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('data', models.JSONField()),
            ],
        ),
    ]
