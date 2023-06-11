# Generated by Django 4.1.6 on 2023-06-07 11:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
        ('classes', '0002_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='danceclass',
            name='teacher',
            field=models.ForeignKey(limit_choices_to={'teacher_type': 'Dance Teacher'}, on_delete=django.db.models.deletion.CASCADE, to='users.teacher'),
        ),
        migrations.AlterField(
            model_name='nepaliclass',
            name='teacher',
            field=models.ForeignKey(limit_choices_to={'teacher_type': 'Nepali Teacher'}, on_delete=django.db.models.deletion.CASCADE, to='users.teacher'),
        ),
    ]
