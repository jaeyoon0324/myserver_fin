# Generated by Django 5.1.1 on 2024-10-02 01:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('test1', '0011_file_remove_post_image_alter_post_title_post_files'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='files',
        ),
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.FileField(blank=True, null=True, upload_to='uploads/'),
        ),
        migrations.DeleteModel(
            name='File',
        ),
    ]
