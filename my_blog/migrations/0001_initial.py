# Generated by Django 4.0.3 on 2022-03-26 15:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text_massegge', models.CharField(max_length=300)),
                ('image', models.ImageField(upload_to='blog_images')),
                ('date_time', models.DateTimeField()),
                ('title', models.CharField(max_length=20)),
            ],
        ),
    ]
