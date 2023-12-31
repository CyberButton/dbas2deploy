# Generated by Django 4.2.7 on 2023-11-21 21:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Job',
            fields=[
                ('job_id', models.AutoField(primary_key=True, serialize=False)),
                ('required_caregiving_type', models.CharField(choices=[('babysitter', 'Babysitter'), ('caregiver for elderly', 'Caregiver for Elderly'), ('playmate for children', 'Playmate for Children')], max_length=60)),
                ('other_requirements', models.TextField()),
                ('date_posted', models.DateField(auto_now_add=True)),
            ],
            options={
                'db_table': 'job',
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('user_id', models.AutoField(primary_key=True, serialize=False)),
                ('email', models.EmailField(max_length=320, unique=True)),
                ('given_name', models.CharField(max_length=255)),
                ('surname', models.CharField(max_length=255)),
                ('city', models.CharField(max_length=255)),
                ('phone_number', models.CharField(max_length=25, unique=True)),
                ('profile_description', models.TextField()),
                ('password', models.CharField(max_length=255)),
            ],
            options={
                'db_table': '"USER"',
            },
        ),
        migrations.CreateModel(
            name='Caregiver',
            fields=[
                ('caregiver_user_id', models.OneToOneField(db_column='caregiver_user_id', on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='dbas2.user')),
                ('photo', models.BinaryField()),
                ('gender', models.CharField(choices=[('male', 'Male'), ('female', 'Female')], max_length=60)),
                ('caregiving_type', models.CharField(choices=[('babysitter', 'Babysitter'), ('caregiver for elderly', 'Caregiver for Elderly'), ('playmate for children', 'Playmate for Children')], max_length=60)),
                ('hourly_rate', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
            options={
                'db_table': 'caregiver',
            },
        ),
        migrations.CreateModel(
            name='Member',
            fields=[
                ('user', models.OneToOneField(db_column='member_user_id', on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='dbas2.user')),
                ('house_rules', models.TextField()),
            ],
            options={
                'db_table': 'member',
            },
        ),
        migrations.CreateModel(
            name='JobApplication',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('date_applied', models.DateField(auto_now_add=True)),
                ('job', models.ForeignKey(db_column='job_id', on_delete=django.db.models.deletion.CASCADE, to='dbas2.job')),
                ('caregiver', models.ForeignKey(db_column='caregiver_user_id', on_delete=django.db.models.deletion.CASCADE, to='dbas2.caregiver')),
            ],
            options={
                'db_table': 'job_application',
            },
        ),
        migrations.AddField(
            model_name='job',
            name='member',
            field=models.ForeignKey(db_column='member_user_id', on_delete=django.db.models.deletion.CASCADE, to='dbas2.member'),
        ),
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.AutoField(db_column='appointment_id', primary_key=True, serialize=False)),
                ('appointment_date', models.DateField()),
                ('appointment_time', models.TextField()),
                ('work_hours', models.IntegerField()),
                ('status', models.CharField(choices=[('confirmed', 'Confirmed'), ('declined', 'Declined'), ('waiting', 'Waiting')], max_length=60)),
                ('caregiver', models.ForeignKey(db_column='caregiver_user_id', on_delete=django.db.models.deletion.CASCADE, to='dbas2.caregiver')),
                ('member', models.ForeignKey(db_column='member_user_id', on_delete=django.db.models.deletion.CASCADE, to='dbas2.member')),
            ],
            options={
                'db_table': 'appointment',
            },
        ),
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('house_number', models.IntegerField()),
                ('street', models.TextField()),
                ('town', models.TextField()),
                ('member_user_id', models.ForeignKey(db_column='member_user_id', on_delete=django.db.models.deletion.CASCADE, to='dbas2.member')),
            ],
            options={
                'db_table': 'address',
            },
        ),
    ]
