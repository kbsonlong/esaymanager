# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-03 14:34
from __future__ import unicode_literals

import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0008_alter_user_username_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=30, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=30, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('name', models.CharField(blank=True, max_length=32, null=True, verbose_name='姓名')),
                ('qq', models.CharField(blank=True, max_length=16, null=True, verbose_name='QQ')),
                ('wechat', models.CharField(blank=True, max_length=32, null=True, verbose_name='微信')),
                ('phone', models.CharField(blank=True, max_length=32, null=True, verbose_name='联系电话')),
            ],
            options={
                'verbose_name_plural': '用户管理',
                'default_permissions': (),
                'permissions': (('view_user', '查看用户'), ('edit_user', '管理用户')),
                'verbose_name': '用户',
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='LoginRecord',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=32, verbose_name='用户')),
                ('date', models.DateTimeField(auto_now_add=True, verbose_name='时间')),
                ('type', models.CharField(max_length=32, verbose_name='类型')),
                ('action', models.CharField(max_length=32, verbose_name='动作')),
                ('ip', models.CharField(max_length=15, verbose_name='用户IP')),
                ('content', models.TextField(verbose_name='内容')),
            ],
            options={
                'verbose_name_plural': '登录信息管理',
                'default_permissions': (),
                'permissions': (('view_loginrecord', '查看登录记录'), ('edit_loginrecord', '管理登录记录')),
                'ordering': ['-date'],
                'verbose_name': '登录信息',
            },
        ),
        migrations.CreateModel(
            name='UserGroup',
            fields=[
                ('group_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='auth.Group')),
                ('group_name', models.CharField(max_length=32, unique=True, verbose_name='用户组')),
                ('comment', models.TextField(blank=True, null=True, verbose_name='备注')),
            ],
            options={
                'verbose_name_plural': '用户管理',
                'default_permissions': (),
                'permissions': (('view_usergroup', '查看用户组'), ('edit_usergroup', '管理用户组')),
                'verbose_name': '用户',
            },
            bases=('auth.group',),
        ),
        migrations.AddField(
            model_name='userinfo',
            name='groups',
            field=models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups'),
        ),
        migrations.AddField(
            model_name='userinfo',
            name='user_permissions',
            field=models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions'),
        ),
    ]