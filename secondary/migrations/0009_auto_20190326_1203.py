# Generated by Django 2.2 on 2019-03-26 11:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('secondary', '0008_remove_class_number_of_students_that_have_paid_fees'),
    ]

    operations = [
        migrations.RenameField(
            model_name='class',
            old_name='Number_Of_Students_In_Class',
            new_name='Number_Of_Students_That_Have_Paid_Fees',
        ),
    ]
