# Generated by Django 3.2.7 on 2021-09-10 10:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0008_alter_contact_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='image',
            field=models.ImageField(default='download.png', upload_to=''),
        ),
    ]
