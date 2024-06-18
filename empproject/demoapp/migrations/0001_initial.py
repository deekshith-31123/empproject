# Generated by Django 4.1.7 on 2024-06-08 14:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Admin',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=50, unique=True)),
                ('password', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'admin_table',
            },
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.PositiveIntegerField(primary_key=True, serialize=False, verbose_name='Department Id')),
                ('name', models.CharField(max_length=100, unique=True, verbose_name='Department Name')),
                ('location', models.CharField(max_length=100, verbose_name='Department Location')),
            ],
            options={
                'db_table': 'department_table',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('category', models.CharField(choices=[('Home', 'Home'), ('Jewelry', 'Jewelry'), ('Electronics', 'Electronics'), ('Clothes', 'Clothers'), ('Others', 'Others')], max_length=100)),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField(max_length=200)),
                ('price', models.PositiveIntegerField()),
                ('image', models.FileField(upload_to='productimages')),
            ],
            options={
                'db_table': 'product_table',
            },
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('fullname', models.CharField(max_length=100)),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female'), ('Others', 'Prefer not to say')], max_length=10)),
                ('dateofbirth', models.CharField(max_length=20)),
                ('salary', models.PositiveIntegerField()),
                ('email', models.EmailField(max_length=50, unique=True)),
                ('username', models.CharField(max_length=50, unique=True)),
                ('password', models.CharField(max_length=50)),
                ('location', models.CharField(max_length=50)),
                ('contact', models.BigIntegerField(unique=True)),
                ('registrationtime', models.DateTimeField(auto_now=True)),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='demoapp.department')),
            ],
            options={
                'db_table': 'employee_table',
            },
        ),
    ]
