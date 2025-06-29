# Generated by Django 5.0.4 on 2024-06-23 21:32

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_alter_order_product_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='product_id',
        ),
        migrations.AddField(
            model_name='order',
            name='product',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='main.products'),
        ),
        migrations.AlterField(
            model_name='order',
            name='inscription',
            field=models.CharField(default='Congratulation!', help_text='*The text on the postcard', max_length=1000),
        ),
    ]
