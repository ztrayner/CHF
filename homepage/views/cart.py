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
    # get the items in the shopping cart in an ajax ($.loadmodal) dialog

    return templater.render_to_response(request, 'cart.html', params)


@view_function
def add(request):
    params = {}
    if 'shopping_cart' not in request.session:
        request.session['shopping_cart'] = {}
    pid = request.urlparams[0]
    qty = request.urlparams[1]

    if pid in request.session['shopping_cart']:
        request.session['shopping_cart'][pid] += 1
        request.session.modified = True
    else:
        request.session['shopping_cart'][pid] = 1

        request.session.modified = True

        products = hmod.Product.objects.filter(id__in=request.session['shopping_cart'].keys)

        params['products'] = products
        params['shopping_cart'] = request.session['shopping_cart']
    return templater.render_to_response(request, 'cart.html', params)