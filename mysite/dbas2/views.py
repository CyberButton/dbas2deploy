from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.

from .models import User, Caregiver, Member, Job, Appointment, JobApplication, Address  # Import your User model
from .forms import UserForm, CaregiverForm, MemberForm, JobForm, \
    AppointmentForm, JobApplicationForm, AddressForm  # You'll need to create a UserForm using Django's forms

import logging

logger = logging.getLogger(__name__)


def ping():
    logger.info("Ping! App is alive.")


def user_list(request):
    users = User.objects.all()
    return render(request, 'dbas2/user_list.html', {'users': users})


def user_create(request):
    form = UserForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('user_list')
    return render(request, 'dbas2/user_form.html', {'form': form})


def user_update(request, id):
    user = get_object_or_404(User, pk=id)
    form = UserForm(request.POST or None, instance=user)
    if form.is_valid():
        form.save()
        return redirect('user_list')
    return render(request, 'dbas2/user_form.html', {'form': form})


def user_delete(request, id):
    user = get_object_or_404(User, pk=id)
    if request.method == 'POST':
        user.delete()
        return redirect('user_list')
    return render(request, 'dbas2/user_confirm_delete.html', {'user': user})


# Caregiver Views
def caregiver_list(request):
    caregivers = Caregiver.objects.all()
    return render(request, 'dbas2/caregiver_list.html', {'caregivers': caregivers})


def caregiver_create(request):
    if request.method == 'POST':
        form = CaregiverForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('caregiver_list')
    else:
        form = CaregiverForm()
    return render(request, 'dbas2/caregiver_form.html', {'form': form})


def caregiver_update(request, id):
    caregiver = get_object_or_404(Caregiver, pk=id)
    if request.method == 'POST':
        form = CaregiverForm(request.POST, instance=caregiver)
        if form.is_valid():
            form.save()
            return redirect('caregiver_list')
    else:
        form = CaregiverForm(instance=caregiver)
    return render(request, 'dbas2/caregiver_form.html', {'form': form, 'caregiver': caregiver})


def caregiver_delete(request, id):
    caregiver = get_object_or_404(Caregiver, pk=id)
    if request.method == 'POST':
        caregiver.delete()
        return redirect('caregiver_list')
    return render(request, 'dbas2/caregiver_confirm_delete.html', {'caregiver': caregiver})


# Member Views
def member_list(request):
    members = Member.objects.all()
    return render(request, 'dbas2/member_list.html', {'members': members})


def member_create(request):
    if request.method == 'POST':
        form = MemberForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('member_list')
    else:
        form = MemberForm()
    return render(request, 'dbas2/member_form.html', {'form': form})


def member_update(request, id):
    member = get_object_or_404(Member, pk=id)
    if request.method == 'POST':
        form = MemberForm(request.POST, instance=member)
        if form.is_valid():
            form.save()
            return redirect('member_list')
    else:
        form = MemberForm(instance=member)
    return render(request, 'dbas2/member_form.html', {'form': form, 'member': member})


def member_delete(request, id):
    member = get_object_or_404(Member, pk=id)
    if request.method == 'POST':
        member.delete()
        return redirect('member_list')
    return render(request, 'dbas2/member_confirm_delete.html', {'member': member})


# Job Views
def job_list(request):
    jobs = Job.objects.all()
    return render(request, 'dbas2/job_list.html', {'jobs': jobs})


def job_create(request):
    if request.method == 'POST':
        form = JobForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('job_list')
    else:
        form = JobForm()
    return render(request, 'dbas2/job_form.html', {'form': form})


def job_update(request, id):
    job = get_object_or_404(Job, pk=id)
    if request.method == 'POST':
        form = JobForm(request.POST, instance=job)
        if form.is_valid():
            form.save()
            return redirect('job_list')
    else:
        form = JobForm(instance=job)
    return render(request, 'dbas2/job_form.html', {'form': form, 'job': job})


def job_delete(request, id):
    job = get_object_or_404(Job, pk=id)
    if request.method == 'POST':
        job.delete()
        return redirect('job_list')
    return render(request, 'dbas2/job_confirm_delete.html', {'job': job})


# Appointment Views
def appointment_list(request):
    appointments = Appointment.objects.all()
    return render(request, 'dbas2/appointment_list.html', {'appointments': appointments})


def appointment_create(request):
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('appointment_list')
    else:
        form = AppointmentForm()
    return render(request, 'dbas2/appointment_form.html', {'form': form})


def appointment_update(request, id):
    appointment = get_object_or_404(Appointment, pk=id)
    if request.method == 'POST':
        form = AppointmentForm(request.POST, instance=appointment)
        if form.is_valid():
            form.save()
            return redirect('appointment_list')
    else:
        form = AppointmentForm(instance=appointment)
    return render(request, 'dbas2/appointment_form.html', {'form': form, 'appointment': appointment})


def appointment_delete(request, id):
    appointment = get_object_or_404(Appointment, pk=id)
    if request.method == 'POST':
        appointment.delete()
        return redirect('appointment_list')
    return render(request, 'dbas2/appointment_confirm_delete.html', {'appointment': appointment})


# JobApplication Views
def jobapplication_list(request):
    jobapplications = JobApplication.objects.all()
    return render(request, 'dbas2/jobapplication_list.html', {'jobapplications': jobapplications})


def jobapplication_create(request):
    if request.method == 'POST':
        form = JobApplicationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('jobapplication_list')
    else:
        form = JobApplicationForm()
    return render(request, 'dbas2/jobapplication_form.html', {'form': form})


def jobapplication_update(request, id):
    jobapplication = get_object_or_404(JobApplication, pk=id)
    if request.method == 'POST':
        form = JobApplicationForm(request.POST, instance=jobapplication)
        if form.is_valid():
            form.save()
            return redirect('jobapplication_list')
    else:
        form = JobApplicationForm(instance=jobapplication)
    return render(request, 'dbas2/jobapplication_form.html', {'form': form, 'jobapplication': jobapplication})


def jobapplication_delete(request, id):
    jobapplication = get_object_or_404(JobApplication, pk=id)
    if request.method == 'POST':
        jobapplication.delete()
        return redirect('jobapplication_list')
    return render(request, 'dbas2/jobapplication_confirm_delete.html', {'jobapplication': jobapplication})


def cruds(request):
    return render(request, 'dbas2/cruds.html')


# List Addresses
def address_list(request):
    addresses = Address.objects.all()
    return render(request, 'dbas2/address_list.html', {'addresses': addresses})


# Create Address
def address_create(request):
    if request.method == 'POST':
        form = AddressForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('address_list')
    else:
        form = AddressForm()
    return render(request, 'dbas2/address_form.html', {'form': form})


# Update Address
def address_update(request, id):
    address = get_object_or_404(Address, pk=id)
    if request.method == 'POST':
        form = AddressForm(request.POST, instance=address)
        if form.is_valid():
            form.save()
            return redirect('address_list')
    else:
        form = AddressForm(instance=address)
    return render(request, 'dbas2/address_form.html', {'form': form})


# Delete Address
def address_delete(request, id):
    address = get_object_or_404(Address, pk=id)
    if request.method == 'POST':
        address.delete()
        return redirect('address_list')
    return render(request, 'dbas2/address_confirm_delete.html', {'address': address})
