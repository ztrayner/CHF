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

    params['publicevents'] = hmod.PublicEvent.objects.all().order_by('id')

    return templater.render_to_response(request, 'publicevents.html', params)

# create/edit
@view_function
@permission_required('is_superuser', login_url='/homepage/login', raise_exception=False)
def edit(request):
    params = {}

    try:
        publicevent = hmod.PublicEvent.objects.get(id=request.urlparams[0])
    except hmod.PublicEvent.DoesNotExist:
        return HttpResponseRedirect('/homepage/publicevents/')

    form = PublicEventEditForm(initial={
        'name': publicevent.name,
        'description': publicevent.description,
        'event_id': publicevent.event_id,
        })
    if request.method == 'POST':
        form = PublicEventEditForm(request.POST)
        if form.is_valid():
            publicevent.name = form.cleaned_data['name']
            publicevent.description = form.cleaned_data['description']
            publicevent.event_id = form.cleaned_data['event_id']
            publicevent.save()
            return HttpResponseRedirect('/homepage/publicevents/')

    params['form'] = form
    params['publicevent'] = publicevent
    return templater.render_to_response(request, 'publicevents.edit.html', params)


class PublicEventEditForm(forms.Form):
    name = forms.CharField(label="Name", required=True)
    description = forms.CharField(label="Description", required=True)
    event_id = forms.IntegerField(label="Event ID", required=True)

@view_function
@permission_required('is_superuser', login_url='/homepage/login', raise_exception=False)
def create(request):
    publicevent = hmod.PublicEvent()
    publicevent.name = ''
    publicevent.description = ''
    publicevent.event_id = ''

    ''' OTHER FIELDS '''
    publicevent.save()

    return HttpResponseRedirect('/homepage/publicevents.edit/{}'.format(publicevent.id))

@view_function
@permission_required('is_superuser', login_url='/homepage/login', raise_exception=False)
def delete(request):

    try:
        publicevent = hmod.PublicEvent.objects.get(id=request.urlparams[0])
    except hmod.PublicEvent.DoesNotExist:
        return HttpResponseRedirect('/homepage/publicevents/')

    publicevent.delete()

    return HttpResponseRedirect('/homepage/publicevents')