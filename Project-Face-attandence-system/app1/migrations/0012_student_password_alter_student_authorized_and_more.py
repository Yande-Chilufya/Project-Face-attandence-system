# Generated by Django 5.0.7 on 2024-11-25 19:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0011_student_computer_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='password',
            field=models.CharField(default=123, max_length=128),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='student',
            name='authorized',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='computer_number',
            field=models.CharField(max_length=50, unique=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='email',
            field=models.EmailField(max_length=254, unique=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='media/students'),
        ),
        migrations.AlterField(
            model_name='student',
            name='name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='student',
            name='student_class',
            field=models.CharField(max_length=50),
        ),
    ]
