# Generated by Django 2.1.7 on 2019-03-18 17:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Post', '0006_auto_20190318_1858'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='img',
            field=models.ImageField(default='post_img/default.jpg', upload_to='post_img/'),
        ),
    ]
