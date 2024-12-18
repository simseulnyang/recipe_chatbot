# Generated by Django 5.1.3 on 2024-11-24 17:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(max_length=255, unique=True, verbose_name='이메일주소')),
                ('nickname', models.CharField(blank=True, max_length=50, null=True, verbose_name='닉네임')),
                ('is_staff', models.BooleanField(default=False, verbose_name='관리자권한')),
                ('is_superuser', models.BooleanField(default=False, verbose_name='관리자')),
                ('is_active', models.BooleanField(default=True, verbose_name='계정활성화')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='마지막 로그인 시간')),
                ('date_joined', models.DateTimeField(auto_now_add=True, verbose_name='가입일')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
        ),
    ]
