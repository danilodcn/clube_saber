# Generated by Django 4.2.3 on 2023-09-17 14:02

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0003_remove_pagesectioncontent_type_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='page',
            name='image',
            field=models.FileField(upload_to='upload/page', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=('png', 'jpeg', 'gif', 'jpg', 'webp', 'ico', 'svg', 'mp4', 'mov', 'wmv', 'webm'))], verbose_name='Arquivo do header'),
        ),
        migrations.AlterField(
            model_name='page',
            name='stamp',
            field=models.FileField(upload_to='upload/page', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=('png', 'jpeg', 'gif', 'jpg', 'webp', 'ico', 'svg'))], verbose_name='Arquivo do selo'),
        ),
    ]
