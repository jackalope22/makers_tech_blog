# Generated by Django 3.0.4 on 2020-03-31 17:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='picture',
            field=models.ImageField(default='default.png', upload_to=''),
        ),
    ]
