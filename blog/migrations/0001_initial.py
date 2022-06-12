# Generated by Django 4.0.5 on 2022-06-12 16:28

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
                ('name', models.CharField(max_length=20, unique=True, verbose_name='카테고리 이름')),
                ('description', models.CharField(max_length=255, verbose_name='카테고리설명')),
            ],
        ),
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('writer', models.CharField(max_length=20, verbose_name='글작성자')),
                ('title', models.CharField(max_length=20, unique=True, verbose_name='글 제목')),
                ('description', models.CharField(max_length=255, verbose_name='글 설명')),
                ('category', models.ForeignKey(default='카테고리 없음', null=True, on_delete=django.db.models.deletion.SET_NULL, to='blog.category', verbose_name='카테고리')),
            ],
        ),
    ]
