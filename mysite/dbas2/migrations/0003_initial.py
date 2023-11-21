# Generated by Django 4.2.7 on 2023-11-21 12:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('dbas2', '0002_auto_20231121_1523'),
    ]

    operations = [
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('required_caregiving_type', models.CharField(verbose_name=['Babysitter', 'Caregiver for Elderly', 'Playmate for Children'])),
                ('other_requirements', models.TextField()),
                ('date_posted', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=320, unique=True)),
                ('given_name', models.CharField(max_length=255)),
                ('surname', models.CharField(max_length=255)),
                ('city', models.CharField(max_length=255)),
                ('phone_number', models.CharField(max_length=25, unique=True)),
                ('profile_description', models.TextField()),
                ('password', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Caregiver',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='dbas2.user')),
                ('photo', models.BinaryField()),
                ('gender', models.CharField(verbose_name=['Male', 'Female'])),
                ('caregiving_type', models.CharField(verbose_name=['Babysitter', 'Caregiver for Elderly', 'Playmate for Children'])),
                ('hourly_rate', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name='Member',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='dbas2.user')),
                ('house_rules', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='JobApplication',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_applied', models.DateField(auto_now_add=True)),
                ('job', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dbas2.job')),
                ('caregiver', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dbas2.caregiver')),
            ],
        ),
        migrations.AddField(
            model_name='job',
            name='member',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dbas2.member'),
        ),
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('appointment_date', models.DateField()),
                ('appointment_time', models.TextField()),
                ('work_hours', models.IntegerField()),
                ('status', models.CharField(verbose_name=['Confirmed', 'Declined', 'Waiting'])),
                ('caregiver', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dbas2.caregiver')),
                ('member', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dbas2.member')),
            ],
        ),
    ]