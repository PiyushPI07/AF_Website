from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from .forms import *
from .templates import *
from .models import RecruitmentApplicant, MyAccountManager, Account
from django.http import HttpResponseRedirect
def application_status_view(request):
    applicant = RecruitmentApplicant.objects.get(email=request.user.email)
    return render(request, 'application_status.html', context={'applicant': applicant})

def registration_view(request):
    context = {}
    if request.method == 'POST':
        registration_form = RegistrationForm(request.POST)
        recruitment_form = RecruitmentForm(request.POST)
        if registration_form.is_valid() and recruitment_form.is_valid():
            account = registration_form.save()
            recruitment_details = recruitment_form.save(commit=False)
            recruitment_details.applicant = account
            recruitment_details.name = account.username
            recruitment_details.email = account.email
            user = Account.objects.get(email=account.email)
            user.is_recruitment_applicant = True
            user.save()
            recruitment_details.save()
            login(request, account)
            return redirect('application status')
        else:
            context['registration_form'] = registration_form
            context['recruitment_form'] = recruitment_form
    else:
        registration_form = RegistrationForm()
        recruitment_form = RecruitmentForm()
        context['registration_form'] = registration_form
        context['recruitment_form'] = recruitment_form

    return render(request, 'register.html', context)



def login_view(request):
    if request.user.is_authenticated:
        return redirect('application status')
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = MyAccountManager.normalize_email(form.cleaned_data['email'])
            password = request.POST['password']
            user = authenticate(email = email, password = password)
            if user:
                login(request, user)
                return redirect('application status')
    else:
        form = LoginForm()
    return render(request, 'login.html', context={'login_form':form})


def logout_view(request):
    logout(request)
    return redirect('index')

def volunteer_form_view(request):
    context = {}
    if request.POST:
        form = VolunteerForm(request.POST)
        if form.is_valid():
            form_details = form.save(commit=False)
            form_details.event = 'Engineer'
            form_details.save()
            return redirect('thank_you')
        else:
            context['form'] = form
    else:
        form = VolunteerForm()
        context['form'] = form
    return render(request, 'volunteer_form.html', context=context)