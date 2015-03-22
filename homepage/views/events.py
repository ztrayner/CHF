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


templater = get_renderer('homepage')

@view_function
@permission_required('is_superuser', login_url='/homepage/login', raise_exception=False)
def process_request(request):
    params = {}

    params['events'] = hmod.Event.objects.all().order_by('id')

    return templater.render_to_response(request, 'events.html', params)

# create/edit
@view_function
@permission_required('is_superuser', login_url='/homepage/login', raise_exception=False)
def edit(request):
    params = {}

    try:
        event = hmod.Event.objects.get(id=request.urlparams[0])
    except hmod.Event.DoesNotExist:
        return HttpResponseRedirect('/homepage/events/')

    form = UserEditForm(initial={
        'startDate': event.startDate,
        'endDate': event.endDate,
        'mapName': event.mapName,
        })
    if request.method == 'POST':
        form = UserEditForm(request.POST)
        if form.is_valid():
            event.startDate = form.cleaned_data['startDate']
            event.endDate = form.cleaned_data['endDate']
            event.mapName = form.cleaned_data['mapName']
            event.save()
            return HttpResponseRedirect('/homepage/events/')

    params['form'] = form
    params['event'] = event
    return templater.render_to_response(request, 'events.edit.html', params)


class UserEditForm(forms.Form):
    startDate = forms.DateField(label="Start Date", required=True)
    endDate = forms.DateField(label="End Date", required=True)
    mapName = forms.CharField(label="Map Name", required=True, max_length=100)

@view_function
@permission_required('is_superuser', login_url='/homepage/login', raise_exception=False)
def create(request):
    event = hmod.Event()
    event.startDate = None
    event.endDate = None
    event.mapName = ''

    ''' OTHER FIELDS '''
    event.save()

    return HttpResponseRedirect('/homepage/events.edit/{}'.format(event.id))

@view_function
def delete(request):

    try:
        event = hmod.Event.objects.get(id=request.urlparams[0])
    except hmod.Event.DoesNotExist:
        return HttpResponseRedirect('/homepage/events/')

    event.delete()

    return HttpResponseRedirect('/homepage/events')