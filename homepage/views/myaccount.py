__author__ = 'Zach'
from django import forms
from django.conf import settings
from django.conf import settings
from django_mako_plus.controller import view_function
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.http import HttpRequest
import homepage.models as hmod
import datetime
import django.forms.widgets
from django.shortcuts import render
from django_mako_plus.controller.router import get_renderer
from django.contrib.auth.decorators import permission_required
import smtplib

templater = get_renderer('homepage')

@view_function
def process_request(request):
    params = {}

    params['users'] = hmod.User.objects.get(id=request.urlparams[0])

    return templater.render_to_response(request, 'myaccount.html', params)

# edit
@view_function
def edit(request):
    params = {}

    try:
        user = hmod.User.objects.get(id=request.urlparams[0])
    except hmod.User.DoesNotExist:
        return HttpResponseRedirect('/homepage/')

    form = UserEditForm(initial={
        'firstName': user.first_name,
        'lastName': user.last_name,
        'email': user.email,
        'security_question': user.security_question,
        'security_answer': user.security_answer,
        'is_active': user.is_active,
        'username': user.username,
        })
    if request.method == 'POST':
        form = UserEditForm(request.POST)
        form.userid = user.id
        if form.is_valid():
            user.first_name = form.cleaned_data['firstName']
            user.last_name = form.cleaned_data['lastName']
            user.username = form.cleaned_data['username']
            user.email = form.cleaned_data['email']
            user.is_active = form.cleaned_data['is_active']
            user.security_question = form.cleaned_data['security_question']
            user.security_answer = form.cleaned_data['security_answer']
            user.save()
            return HttpResponseRedirect('/homepage/myaccount/' + str(user.id))

    params['form'] = form
    params['user'] = user
    return templater.render_to_response(request, 'myaccount.edit.html', params)


class UserEditForm(forms.Form):
    firstName = forms.CharField(label="First Name", required=True, max_length=100)
    lastName = forms.CharField(label="Last Name", required=True, max_length=100)
    email = forms.EmailField(label="Email", required=True, max_length=100)
    username = forms.CharField(label="Username", required=True, max_length=100)
    security_question = forms.CharField(label="Security question", required=False, max_length=100)
    security_answer = forms.CharField(label="Security answer", required=False, max_length=100)
    is_active = forms.BooleanField(required=False)

    def clean_username(self):
        users = hmod.User.objects.filter(username=self.cleaned_data['username']).exclude(id=self.userid).count()
        if users >= 1:
            raise forms.ValidationError("This username is already taken.")
        return self.cleaned_data['username']


# change password
@view_function
def changepassword(request):
    params = {}

    try:
        user = hmod.User.objects.get(id=request.urlparams[0])
    except hmod.User.DoesNotExist:
        return HttpResponseRedirect('/homepage/')

    form = PasswordEditForm(initial={
        'password': user.password,
        })
    if request.method == 'POST':
        form = PasswordEditForm(request.POST)
        if form.is_valid():
            user.set_password(form.cleaned_data['password'])
            user.save()
            return HttpResponseRedirect('/homepage/')

    params['form'] = form
    params['user'] = user
    return templater.render_to_response(request, 'myaccount.edit.html', params)


class PasswordEditForm(forms.Form):
    password = forms.CharField(label='Password', widget=forms.PasswordInput)

# late items email button click
@view_function
def lateitemsemail(request):
    params = {}

    try:
        laterentals = hmod.Rental.objects.all().filter(dueDate < + datetime.date.today().strftime("%B %d, %Y")).filter(returned=False)
        # email code
        fromaddr = 'test@zachtrayner.com'
        toaddrs = 'me@zachtrayner.com'

        # Body of the email
        # Iterate through list of overdue products

        msg = 'These products are overdue: </br>'  # + laterentals

        # Credentials

        username = 'test@zachtrayner.com'
        password = 'password'

        # Sending the mail

        session = smtplib.SMTP('smptp.domain.com', 465)
        session.ehlo()
        session.starttls()
        session.login(username, password)
        session.sendmail(fromaddr, toaddrs, msg)
        session.quit()

    except hmod.Rental.DoesNotExist:
        return HttpResponse('1')  # query failed

    params['laterentals'] = laterentals
    return HttpResponse('0')  # query pulled results
