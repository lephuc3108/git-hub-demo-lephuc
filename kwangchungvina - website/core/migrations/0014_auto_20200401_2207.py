# Generated by Django 2.2.7 on 2020-04-01 15:07

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0013_item_categories'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='description',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True),
        ),
    ]
