# Generated by Django 4.2.3 on 2023-09-17 14:07

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0004_alter_page_image_alter_page_stamp'),
    ]

    operations = [
        migrations.RenameField(
            model_name='page',
            old_name='image',
            new_name='header_file',
        ),
        migrations.RenameField(
            model_name='page',
            old_name='stamp',
            new_name='stamp_file',
        ),
        migrations.AlterField(
            model_name='page',
            name='product',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='web.product'),
        ),
    ]
