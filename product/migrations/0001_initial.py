# Generated by Django 4.0.5 on 2022-06-17 04:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20, verbose_name='제목')),
                ('thumbnail', models.ImageField(upload_to='%Y/%m/%d')),
                ('description', models.CharField(max_length=255, verbose_name='설명')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='등록일자')),
                ('expose_startdate', models.DateTimeField(verbose_name='노출 시작 일')),
                ('expose_enddate', models.DateTimeField(verbose_name='노출 종료 일')),
                ('is_active', models.BooleanField(default=False)),
            ],
        ),
    ]