__author__ = 'Zach'
from django import forms
from django.conf import settings
from django_mako_plus.controller import view_function
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.http import HttpRequest
import homepage.models as hmod
import datetime
import django.forms.widgets
from django.shortcuts import render
from django_mako_plus.controller.router import get_renderer
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import permission_required
from django.contrib.auth.views import login


templater = get_renderer('homepage')

@view_function
def process_request(request):
    params = {}

    return templater.render_to_response(request, 'signup.create.html', params)

# create/edit
@view_function
def edit(request):
    params = {}

    try:
        user = hmod.User.objects.get(id=request.urlparams[0])
    except hmod.User.DoesNotExist:
        return HttpResponseRedirect('/homepage/users/')

    form = UserEditForm(initial={
        'firstName': user.first_name,
        'lastName': user.last_name,
        'username': user.username,
        'password': user.password,
        'email': user.email,
        'security_question': user.security_question,
        'security_answer': user.security_answer,
        })
    if request.method == 'POST':
        form = UserEditForm(request.POST)
        form.userid = user.id
        form.password = user.password
        if form.is_valid():
            user.first_name = form.cleaned_data['firstName']
            user.last_name = form.cleaned_data['lastName']
            user.username = form.cleaned_data['username']
            user.email = form.cleaned_data['email']
            user.set_password(form.cleaned_data['password'])
            user.security_question = form.cleaned_data['security_question']
            user.security_answer = form.cleaned_data['security_answer']
            user.save()
            return HttpResponseRedirect('/homepage/login/')

    params['form'] = form
    params['user'] = user
    return templater.render_to_response(request, 'signup.edit.html', params)


class UserEditForm(forms.Form):
    firstName = forms.CharField(label="First Name", required=True, max_length=100)
    lastName = forms.CharField(label="Last Name", required=True, max_length=100)
    username = forms.CharField(label="Username", required=True, max_length=100)
    email = forms.EmailField(label="Email", required=True, max_length=100)
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    security_question = forms.CharField(label="Security question", required=False, max_length=100)
    security_answer = forms.CharField(label="Security answer", required=False, max_length=100)
    def clean_username(self):
        users = hmod.User.objects.filter(username=self.cleaned_data['username']).exclude(id=self.userid).count()
        if users >= 1:
            raise forms.ValidationError("This username is already taken.")
        return self.cleaned_data['username']

@view_function
def create(request):
    user = hmod.User()
    user.first_name = ''
    user.last_name = ''
    user.email = ''
    user.security_answer = ''
    user.security_question = ''
    user.is_active = True
    user.username = ''
    user.date_joined = datetime.datetime.now()
    user.password = ''
    user.is_staff = False
    user.is_superuser = False
    user.is_agent = False
    user.last_login = datetime.datetime.now()

    ''' OTHER FIELDS '''
    user.save()

    return HttpResponseRedirect('/homepage/signup.edit/{}'.format(user.id))

# function to check if UN is available
@view_function
def check_username(request):

    username = request.REQUEST.get('u')
    try:
        user = hmod.User.objects.get(username=username)
    except hmod.User.DoesNotExist:
        return HttpResponse('0')  # username is available
    return HttpResponse('1')  # username is not available