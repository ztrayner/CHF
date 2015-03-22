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


templater = get_renderer('homepage')


@view_function
def process_request(request):
    params = {}

    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password'])
            login(request, user)
            return HttpResponseRedirect('/homepage/index')

    params['form'] = form
    return templater.render_to_response(request, 'login.html', params)


class LoginForm(forms.Form):
    username = forms.CharField(label="", required=True,
                               widget=forms.TextInput(attrs={'placeholder': 'Username', 'class': "input-lg"}))
    password = forms.CharField(required=True, widget=forms.PasswordInput(attrs={'placeholder': 'Password',
                                                                                'class': "input-lg"}), label="")

    def clean(self):
        user = authenticate(username=self.cleaned_data['username'], password=self.cleaned_data['password'])
        if user is None:
            raise forms.ValidationError('Invalid username or password. Please try again.')
        return self.cleaned_data


@view_function
def check_username(request):
    username = request.REQUEST.get('u')
    try:
        user = hmod.User.objects.get(username=username)
    except hmod.User.DoesNotExist:
        return HttpResponse('0')  # username is available, not in DB
    return HttpResponse('1')  # username is not available, in DB

@view_function
def loginform(request):
    params = {}

    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password'])
            login(request, user)
            return HttpResponse('''
                                <script>
                                console.log('httpResponse working');
                                    window.location.href = "/homepage/"
                                </script>
                                ''')

    params['form'] = form
    return templater.render_to_response(request, 'login.loginform.html', params)