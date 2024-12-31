from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.ImageField(blank=True, null=True, upload_to='Client')),
                ('is_favorite', models.BooleanField(default=False)),
                ('can_be_downloaded', models.BooleanField(default=False)),
                ('thumbnail', models.FileField(blank=True, null=True, upload_to='Client/thumbnails')),
            ],
        ),
        migrations.CreateModel(
            name='UserClient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('email', models.EmailField(default='', help_text='A valid email address, please', max_length=255, unique=True)),
                ('first_name', models.CharField(default=None, max_length=255)),
                ('last_name', models.CharField(blank=True, default=None, max_length=255, null=True)),
                ('phone_number', models.CharField(blank=True, default='', help_text='Phone number must not contain spaces, letters, parentheses or dashes. It must contain 15 digits.', max_length=18, null=True)),
                ('address', models.CharField(blank=True, default='', help_text='Does not have to be specific, just the city and the state', max_length=255, null=True)),
                ('is_active', models.BooleanField(default=True)),
                ('admin', models.BooleanField(default=False)),
                ('staff', models.BooleanField(default=False)),
                ('start_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('first_login', models.BooleanField(default=False)),
                ('profile_photo', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='user_clients', to='client.photo')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
