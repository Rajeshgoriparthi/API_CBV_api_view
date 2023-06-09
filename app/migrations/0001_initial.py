# Generated by Django 4.2.2 on 2023-06-08 13:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product_catagiry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pc_id', models.IntegerField()),
                ('pc_name', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('p_id', models.IntegerField()),
                ('p_name', models.CharField(max_length=100)),
                ('p_price', models.IntegerField()),
                ('p_description', models.CharField(max_length=400)),
                ('p_date', models.DateField()),
                ('pc_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.product_catagiry')),
            ],
        ),
    ]
