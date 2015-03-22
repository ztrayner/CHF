__author__ = 'Zach'
from django import forms
from django.conf import settings
from django.conf import settings
from django_mako_plus.controller import view_function
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.http import HttpRequest
import homepage.models as hmod
from django.shortcuts import render
from django_mako_plus.controller.router import get_renderer
from django.contrib.auth.decorators import permission_required


templater = get_renderer('homepage')

@view_function
@permission_required('is_superuser', login_url='/homepage/login', raise_exception=False)
def process_request(request):
    params = {}

    params['photographs'] = hmod.Photograph.objects.all().order_by('dateTaken', 'placeTaken')

    return templater.render_to_response(request, 'photograph.html', params)

# create/edit
@view_function
@permission_required('is_superuser', login_url='/homepage/login', raise_exception=False)
def edit(request):
    params = {}

    try:
        photographs = hmod.Photograph.objects.get(id=request.urlparams[0])
    except hmod.Photograph.DoesNotExist:
        return HttpResponseRedirect('/homepage/photograph/')

    form = PhotographEditForm(initial={
        'dateTaken': photographs.dateTaken,
        'placeTaken': photographs.placeTaken,
        'image': photographs.image,
        'photographer_id': photographs.photographer_id,
        })
    if request.method == 'POST':
        form = PhotographEditForm(request.POST)
        if form.is_valid():
            photographs.dateTaken = form.cleaned_data['dateTaken']
            photographs.placeTaken = form.cleaned_data['placeTaken']
            photographs.image = form.cleaned_data['image']
            photographs.photographer_id = form.cleaned_data['photographer_id']
            photographs.save()
            return HttpResponseRedirect('/homepage/photograph/')


    params['form'] = form
    return templater.render_to_response(request, 'photograph.edit.html', params)


class PhotographEditForm(forms.Form):
    dateTaken = forms.DateField(label="Date Taken", required=True)
    placeTaken = forms.CharField(label="Place Taken", required=True, max_length=100)
    image = forms.CharField(label="image", required=True, max_length=100)
    photographer_id = forms.CharField(label="Photographer ID", required=True, max_length=100)

@view_function
@permission_required('is_superuser', login_url='/homepage/login', raise_exception=False)
def create(request):
    photograph = hmod.Photograph()
    photograph.dateTaken = None
    photograph.placeTaken = ''
    photograph.image = ''
    photograph.photographer_id = ''

    ''' OTHER FIELDS '''
    photograph.save()

    return HttpResponseRedirect('/homepage/photograph.edit/{}'.format(photograph.id))

@view_function
@permission_required('is_superuser', login_url='/homepage/login', raise_exception=False)
def delete(request):

    try:
        photograph = hmod.Photograph.objects.get(id=request.urlparams[0])
    except hmod.Photograph.DoesNotExist:
        return HttpResponseRedirect('/homepage/photograph/')

    photograph.delete()

    return HttpResponseRedirect('/homepage/photograph')