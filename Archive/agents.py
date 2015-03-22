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

    params['agents'] = hmod.Agent.objects.all().order_by('id')

    return templater.render_to_response(request, 'agents.html', params)

# create/edit
@view_function
@permission_required('is_superuser', login_url='/homepage/login', raise_exception=False)
def edit(request):
    params = {}

    try:
        agent = hmod.Agent.objects.get(id=request.urlparams[0])
    except hmod.Agent.DoesNotExist:
        return HttpResponseRedirect('/homepage/agents/')

    form = UserEditForm(initial={
        'appointment': agent.appointmentDate,
        })
    if request.method == 'POST':
        form = UserEditForm(request.POST)
        if form.is_valid():
            agent.appointmentDate = form.cleaned_data['appointmentDate']
            agent.save()
            return HttpResponseRedirect('/homepage/agents/')

    params['form'] = form
    params['agent'] = agent
    return templater.render_to_response(request, 'agents.edit.html', params)


class UserEditForm(forms.Form):
    appointmentDate = forms.DateField(label="Appointment Date", required=True)

@view_function
@permission_required('is_superuser', login_url='/homepage/login', raise_exception=False)
def create(request):
    agent = hmod.Agent()
    agent.appointmentDate = None
    agent.legalentity_ptr_id = '0'

    ''' OTHER FIELDS '''
    agent.save()

    return HttpResponseRedirect('/homepage/agents.edit/{}'.format(agent.id))

@view_function
@permission_required('is_superuser', login_url='/homepage/login', raise_exception=False)
def delete(request):

    try:
        agent = hmod.Agent.objects.get(id=request.urlparams[0])
    except hmod.Agent.DoesNotExist:
        return HttpResponseRedirect('/homepage/agents/')

    agent.delete()

    return HttpResponseRedirect('/homepage/agents')