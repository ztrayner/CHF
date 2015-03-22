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

templater = get_renderer('homepage')

@view_function
@permission_required('is_superuser', login_url='/homepage/login', raise_exception=False)
def process_request(request):
    params = {}

    params['users'] = hmod.User.objects.all().order_by('username')

    return templater.render_to_response(request, 'users.html', params)

# create/edit
@view_function
@permission_required('is_superuser', login_url='/homepage/login', raise_exception=False)
def edit(request):
    params = {}

    try:
        user = hmod.User.objects.get(id=request.urlparams[0])
    except hmod.User.DoesNotExist:
        return HttpResponseRedirect('/homepage/users/')

    form = UserEditForm(initial={
        'firstName': user.first_name,
        'lastName': user.last_name,
        'email': user.email,
        'security_question': user.security_question,
        'security_answer': user.security_answer,
        'username': user.username,
        'password': user.password,
        'last_login': user.last_login,
        'is_staff': user.is_staff,
        'is_active': user.is_active,
        'date_joined': user.date_joined,
        'is_superuser': user.is_superuser,
        'is_agent': user.is_agent,
        })
    if request.method == 'POST':
        form = UserEditForm(request.POST)
        form.userid = user.id
        if form.is_valid():
            user.first_name = form.cleaned_data['firstName']
            user.last_name = form.cleaned_data['lastName']
            user.username = form.cleaned_data['username']
            user.email = form.cleaned_data['email']
            user.set_password(form.cleaned_data['password'])
            user.last_login = form.cleaned_data['last_login']
            user.is_superuser = form.cleaned_data['is_superuser']
            user.is_staff = form.cleaned_data['is_staff']
            user.date_joined = form.cleaned_data['date_joined']
            user.is_active = form.cleaned_data['is_active']
            user.security_question = form.cleaned_data['security_question']
            user.security_answer = form.cleaned_data['security_answer']
            user.is_agent = form.cleaned_data['is_agent']
            user.save()
            return HttpResponseRedirect('/homepage/users/')

    params['form'] = form
    params['user'] = user
    return templater.render_to_response(request, 'users.edit.html', params)


class UserEditForm(forms.Form):
    firstName = forms.CharField(label="First Name", required=True, max_length=100)
    lastName = forms.CharField(label="Last Name", required=True, max_length=100)
    email = forms.EmailField(label="Email", required=True, max_length=100)
    username = forms.CharField(label="Username", required=True, max_length=100)
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    security_question = forms.CharField(label="Security question", required=False, max_length=100)
    security_answer = forms.CharField(label="Security answer", required=False, max_length=100)
    date_joined = forms.DateField()
    last_login = forms.DateField()
    is_active = forms.BooleanField(required=False)
    is_superuser = forms.BooleanField(required=False)
    is_staff = forms.BooleanField(required=False)
    is_agent = forms.BooleanField(required=False)

    def clean_username(self):
        users = hmod.User.objects.filter(username=self.cleaned_data['username']).exclude(id=self.userid).count()
        if users >= 1:
            raise forms.ValidationError("This username is already taken.")
        return self.cleaned_data['username']

@view_function
@permission_required('is_superuser', login_url='/homepage/login', raise_exception=False)
def create(request):
    user = hmod.User()
    user.first_name = ''
    user.last_name = ''
    user.email = ''
    user.security_answer = ''
    user.security_question = ''
    user.is_active = ''
    user.username = ''
    user.date_joined = datetime.datetime.now()
    user.password = ''
    user.is_staff = ''
    user.is_superuser = ''
    user.is_agent = ''
    user.last_login = datetime.datetime.now()

    ''' OTHER FIELDS '''
    user.save()

    return HttpResponseRedirect('/homepage/users.edit/{}'.format(user.id))

@view_function
@permission_required('is_superuser', login_url='/homepage/login', raise_exception=False)
def delete(request):

    try:
        user = hmod.User.objects.get(id=request.urlparams[0])
    except hmod.User.DoesNotExist:
        return HttpResponseRedirect('/homepage/users/')

    user.delete()

    return HttpResponseRedirect('/homepage/users')