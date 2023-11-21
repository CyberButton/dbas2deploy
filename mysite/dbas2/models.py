from django.db import models

# Create your models here.
from django.db import models


# Create your models here.
class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    email = models.EmailField(max_length=320, unique=True)
    given_name = models.CharField(max_length=255)
    surname = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=25, unique=True)
    profile_description = models.TextField()
    password = models.CharField(
        max_length=255)  # Consider using Django's built-in User model for secure password handling

    class Meta:
        db_table = '"USER"'


class Caregiver(models.Model):
    caregiver_user_id = models.OneToOneField(User, on_delete=models.CASCADE, db_column='caregiver_user_id',
                                             primary_key=True)
    photo = models.BinaryField()  # Represents BYTEA
    gender = models.CharField(choices=[('male', 'Male'), ('female', 'Female')])
    caregiving_type = models.CharField(choices=[('babysitter', 'Babysitter'),
                                                ('caregiver for elderly', 'Caregiver for Elderly'),
                                                ('playmate for children', 'Playmate for Children')])
    hourly_rate = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        db_table = 'caregiver'


class Member(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True, db_column='member_user_id')
    house_rules = models.TextField()

    class Meta:
        db_table = 'member'


class Job(models.Model):
    job_id = models.AutoField(primary_key=True)
    member = models.ForeignKey(Member, on_delete=models.CASCADE, db_column='member_user_id')
    required_caregiving_type = models.CharField(choices=[('babysitter', 'Babysitter'),
                                                         ('caregiver for elderly', 'Caregiver for Elderly'),
                                                         ('playmate for children', 'Playmate for Children')])
    other_requirements = models.TextField()
    date_posted = models.DateField(auto_now_add=True)

    class Meta:
        db_table = 'job'


class JobApplication(models.Model):
    id = models.AutoField(primary_key=True)
    caregiver = models.ForeignKey(Caregiver, on_delete=models.CASCADE, db_column='caregiver_user_id')
    job = models.ForeignKey(Job, on_delete=models.CASCADE, db_column='job_id')
    date_applied = models.DateField(auto_now_add=True)

    class Meta:
        db_table = 'job_application'


class Appointment(models.Model):
    id = models.AutoField(primary_key=True, db_column='appointment_id')
    caregiver = models.ForeignKey(Caregiver, on_delete=models.CASCADE, db_column='caregiver_user_id')
    member = models.ForeignKey(Member, on_delete=models.CASCADE, db_column='member_user_id')
    appointment_date = models.DateField()
    appointment_time = models.TextField()
    work_hours = models.IntegerField()
    status = models.CharField(choices=[('confirmed', 'Confirmed'), ('declined', 'Declined'), ('waiting', 'Waiting')])

    class Meta:
        db_table = 'appointment'


class Address(models.Model):
    id = models.AutoField(primary_key=True)
    member_user_id = models.ForeignKey(Member, on_delete=models.CASCADE, db_column="member_user_id")
    house_number = models.IntegerField()
    street = models.TextField()
    town = models.TextField()

    class Meta:
        db_table = 'address'
