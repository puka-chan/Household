# Generated by Django 3.1.3 on 2021-04-22 10:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AccountBookapp', '0004_auto_20210421_2307'),
    ]

    operations = [
        migrations.AlterField(
            model_name='income',
            name='user',
            field=models.CharField(max_length=50, verbose_name='ユーザーID'),
        ),
        migrations.AlterField(
            model_name='incomecategory',
            name='user',
            field=models.CharField(max_length=50, verbose_name='ユーザーID'),
        ),
        migrations.AlterField(
            model_name='incomesubcategory',
            name='user',
            field=models.CharField(max_length=50, verbose_name='ユーザーID'),
        ),
        migrations.AlterField(
            model_name='spending',
            name='user',
            field=models.CharField(max_length=50, verbose_name='ユーザーID'),
        ),
        migrations.AlterField(
            model_name='spendingcategory',
            name='user',
            field=models.CharField(max_length=50, verbose_name='ユーザーID'),
        ),
        migrations.AlterField(
            model_name='spendingsubcategory',
            name='user',
            field=models.CharField(max_length=50, verbose_name='ユーザーID'),
        ),
    ]
