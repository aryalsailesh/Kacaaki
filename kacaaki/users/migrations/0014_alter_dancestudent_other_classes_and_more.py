# Generated by Django 4.1.6 on 2023-11-24 16:42

from django.db import migrations
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0013_remove_dancestudent_is_dance_student_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dancestudent',
            name='other_classes',
            field=multiselectfield.db.fields.MultiSelectField(blank=True, choices=[('Nepali Classes', 'Nepali Classes'), ('Music Classes', 'Music Classes')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='nepalistudent',
            name='other_classes',
            field=multiselectfield.db.fields.MultiSelectField(blank=True, choices=[('Dance Classes', 'Dance Classes'), ('Music Classes', 'Music Classes')], max_length=50, null=True),
        ),
    ]
