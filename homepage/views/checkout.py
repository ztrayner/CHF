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
from django.contrib.auth.decorators import permission_required
from django.contrib.auth.decorators import login_required


templater = get_renderer('homepage')


@view_function
@login_required(login_url='/homepage/login/')
def process_request(request):
    params = {}
    return templater.render_to_response(request, 'checkout.html', params)
