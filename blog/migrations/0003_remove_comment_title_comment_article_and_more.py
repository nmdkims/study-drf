# Generated by Django 4.0.5 on 2022-06-27 09:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0002_comment'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='title',
        ),
        migrations.AddField(
            model_name='comment',
            name='article',
            field=models.ForeignKey(default=1, max_length=20, on_delete=django.db.models.deletion.CASCADE, to='blog.article', verbose_name='게시글'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='comment',
            name='writer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='사용자'),
        ),
    ]
