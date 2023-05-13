# Generated by Django 4.1.3 on 2023-05-13 20:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='Place',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('image', models.ImageField(upload_to='places/')),
            ],
        ),
        migrations.CreateModel(
            name='property',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='Property/')),
                ('price', models.IntegerField(default=0)),
                ('description', models.TextField(max_length=10000)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='property_category', to='property.category')),
                ('places', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='property_place', to='property.place')),
            ],
        ),
        migrations.CreateModel(
            name='PropertyImages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='propertyimages/')),
                ('property', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='property_image', to='property.property')),
            ],
        ),
    ]
