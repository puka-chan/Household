# Generated by Django 3.1.3 on 2021-04-21 11:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='IncomeCategory',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=30, unique=True, verbose_name='カテゴリ名')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='登録日時')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='ユーザー')),
            ],
        ),
        migrations.CreateModel(
            name='SpendingCategory',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=30, unique=True, verbose_name='カテゴリ名')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='登録日時')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='ユーザー')),
            ],
        ),
        migrations.CreateModel(
            name='SpendingSubCategory',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=30, unique=True, verbose_name='サブカテゴリ名')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='登録日時')),
                ('category', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.PROTECT, to='AccountBookapp.spendingcategory', verbose_name='カテゴリ')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='ユーザー')),
            ],
        ),
        migrations.CreateModel(
            name='Spending',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('User_date', models.DateField(verbose_name='会計日')),
                ('amount', models.IntegerField(verbose_name='金額')),
                ('comment', models.CharField(blank=True, max_length=200, null=True, verbose_name='コメント')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='登録日時')),
                ('category', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.PROTECT, to='AccountBookapp.spendingcategory', verbose_name='カテゴリ')),
                ('subcategory', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='AccountBookapp.spendingsubcategory', verbose_name='サブカテゴリ')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='ユーザー')),
            ],
        ),
        migrations.CreateModel(
            name='IncomeSubCategory',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=30, unique=True, verbose_name='サブカテゴリ名')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='登録日時')),
                ('category', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.PROTECT, to='AccountBookapp.incomecategory', verbose_name='カテゴリ')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='ユーザー')),
            ],
        ),
        migrations.CreateModel(
            name='Income',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('User_date', models.DateField(verbose_name='会計日')),
                ('amount', models.IntegerField(verbose_name='金額')),
                ('comment', models.CharField(blank=True, max_length=200, null=True, verbose_name='コメント')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='登録日時')),
                ('category', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.PROTECT, to='AccountBookapp.incomecategory', verbose_name='カテゴリ')),
                ('subcategory', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='AccountBookapp.incomesubcategory', verbose_name='サブカテゴリ')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='ユーザー')),
            ],
        ),
    ]
