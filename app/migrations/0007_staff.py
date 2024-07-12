# Generated by Django 5.0.3 on 2024-04-23 19:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_student_email_student_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='staff',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('staff_name', models.CharField(max_length=50)),
                ('staff_id', models.CharField(max_length=50)),
                ('staff_email', models.CharField(max_length=50)),
                ('staff_mobile', models.CharField(max_length=50)),
                ('gender', models.CharField(max_length=50)),
                ('qualification', models.CharField(max_length=50)),
                ('date_of_birth', models.DateField(auto_now_add=True)),
                ('experience', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=50)),
                ('city', models.CharField(max_length=50)),
                ('state', models.CharField(max_length=50)),
                ('zipcode', models.CharField(max_length=50)),
            ],
        ),
    ]