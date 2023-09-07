# Generated by Django 4.2.3 on 2023-09-07 13:35

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250, null=True, verbose_name='Nome')),
                ('description', models.TextField(verbose_name='Descrição')),
                ('enabled', models.BooleanField(db_index=True, default=True, verbose_name='Habilitado')),
                ('order', models.PositiveSmallIntegerField(db_index=True, null=True, verbose_name='ordem')),
                ('price', models.DecimalField(decimal_places=2, max_digits=12, null=True, verbose_name='Preço')),
                ('number_of_installments', models.PositiveSmallIntegerField(null=True, verbose_name='Número de parcelas')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Data de Criação')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Atualizado em')),
                ('sku', models.UUIDField(default=uuid.uuid4)),
            ],
            options={
                'verbose_name': 'Produto',
                'verbose_name_plural': 'Produtos',
                'ordering': ['order', 'pk'],
            },
        ),
        migrations.CreateModel(
            name='ProductTag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250, null=True, verbose_name='Nome')),
                ('order', models.PositiveSmallIntegerField(db_index=True, null=True, verbose_name='ordem')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Data de Criação')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Atualizado em')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tags', to='product.product')),
            ],
            options={
                'verbose_name': 'Tag do produto',
                'verbose_name_plural': 'Tags dos produtos',
                'ordering': ('order', 'name', 'pk'),
            },
        ),
        migrations.CreateModel(
            name='ProductFile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order', models.PositiveSmallIntegerField(db_index=True, null=True, verbose_name='ordem')),
                ('name', models.CharField(max_length=250, null=True, verbose_name='Nome')),
                ('file', models.FileField(upload_to='upload/product', verbose_name='Arquivo')),
                ('type', models.CharField(choices=[('IMAGE', 'imagem'), ('VIDEO', 'video')], db_index=True, max_length=20, verbose_name='Tipo')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Data de Criação')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Atualizado em')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='files', to='product.product')),
            ],
            options={
                'verbose_name': 'Arquivo do produto',
                'verbose_name_plural': 'Arquivos dos produtos',
                'ordering': ('order', 'name', 'pk'),
            },
        ),
    ]
