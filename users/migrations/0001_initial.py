# Generated by Django 3.1.6 on 2021-06-25 04:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='NewUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='Email')),
                ('full_name', models.CharField(max_length=150, verbose_name='Full Name')),
                ('phone_number', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None, unique=True, verbose_name='Phone Number')),
                ('start_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('about', models.TextField(blank=True, null=True, verbose_name='About')),
                ('is_staff', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='student-image/', verbose_name='Your Image')),
                ('faculty', models.CharField(blank=True, choices=[('DIF', 'Dasturiy injiniring fakulteti'), ('KIF', 'Kompyuter injiniringi fakulteti'), ('TTF', 'Telekommunikatsiya texnologiyalari fakulteti'), ('AXF', 'Axborot xavfsizligi fakulteti'), ('TvTF', 'Televizion texnologiyalar fakulteti'), ('AKT_IM', 'AKT sohasida iqtisodiyot va menejment fakulteti'), ('AKT_KT', 'AKT sohasida Kasb ta`limi fakulteti')], max_length=300, null=True, verbose_name='Faculty')),
                ('group', models.CharField(blank=True, max_length=100, null=True, verbose_name='Group')),
                ('level', models.CharField(blank=True, choices=[('I', '1-kurs'), ('II', '2-kurs'), ('III', '3-kurs'), ('IV', '4-kurs')], max_length=50, null=True, verbose_name='Level')),
                ('student', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='student', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Student',
                'verbose_name_plural': 'Students',
            },
        ),
    ]