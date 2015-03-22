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
from django.contrib.auth import authenticate, logout


templater = get_renderer('homepage')

@view_function
def process_request(request):
    params = {}

    logout(request)
    return HttpResponseRedirect('/homepage/logoutsuccess')
