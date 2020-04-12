# Generated by Django 2.2.7 on 2020-03-31 15:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0011_auto_20200331_2240'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='categories',
        ),
        migrations.AddField(
            model_name='item',
            name='category',
            field=models.CharField(choices=[('chung', 'CHUNG'), ('inox tấm', 'INOX TẤM'), ('inox cuộn', 'INOX CUỘN')], default='chung', max_length=355),
        ),
    ]
