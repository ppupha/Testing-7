# Generated by Django 2.2 on 2021-09-24 22:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_fullname', models.CharField(max_length=30, null=True)),
                ('user_description', models.TextField(max_length=218, null=True)),
                ('user_avatar', models.ImageField(blank=True, default='user_avatar/default-avatar.png', null=True, upload_to='user_avatar')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='Info', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
