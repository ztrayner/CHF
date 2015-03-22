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

    params['legalentities'] = hmod.LegalEntity.objects.all().order_by('id')

    return templater.render_to_response(request, 'legalentities.html', params)

# create/edit
@view_function
@permission_required('is_superuser', login_url='/homepage/login', raise_exception=False)
def edit(request):
    params = {}

    try:
        legalentity = hmod.LegalEntity.objects.get(id=request.urlparams[0])
    except hmod.LegalEntity.DoesNotExist:
        return HttpResponseRedirect('/homepage/legalentities/')

    form = LegalEntityEditForm(initial={
        'givenName': legalentity.givenName,
        'creationDate': legalentity.creationDate,
        'address1': legalentity.address1,
        'address2': legalentity.address2,
        'city': legalentity.city,
        'state': legalentity.state,
        'Zip': legalentity.Zip,
        'email': legalentity.email,
        'phone': legalentity.phone,
        'user_id': legalentity.user_id,
        'familyName': legalentity.familyName,
        'organizationType': legalentity.organizationType,
        })
    if request.method == 'POST':
        form = LegalEntityEditForm(request.POST)
        if form.is_valid():
            legalentity.givenName = form.cleaned_data['givenName']
            legalentity.creationDate = form.cleaned_data['creationDate']
            legalentity.address1 = form.cleaned_data['address1']
            legalentity.address2 = form.cleaned_data['address2']
            legalentity.city = form.cleaned_data['city']
            legalentity.state = form.cleaned_data['state']
            legalentity.Zip = form.cleaned_data['Zip']
            legalentity.email = form.cleaned_data['email']
            legalentity.phone = form.cleaned_data['phone']
            legalentity.user_id = form.cleaned_data['user_id']
            legalentity.familyName = form.cleaned_data['familyName']
            legalentity.organizationType = form.cleaned_data['organizationType']
            legalentity.save()
            return HttpResponseRedirect('/homepage/legalentities/')

    params['form'] = form
    params['legalentity'] = legalentity
    return templater.render_to_response(request, 'legalentities.edit.html', params)


class LegalEntityEditForm(forms.Form):
    givenName = forms.CharField(label="Given Name", required=True, max_length=100)
    creationDate = forms.DateField(label="Creation Date", required=True)
    address1 = forms.CharField(label="Address 1", required=True, max_length=100)
    address2 = forms.CharField(label="Address 2", required=False, max_length=100)
    city = forms.CharField(label="City", required=True, max_length=100)
    state = forms.CharField(label="State", required=True)
    Zip = forms.CharField(label="ZIP", required=True, max_length=100)
    email = forms.CharField(label='Email', required=True, max_length=100)
    phone = forms.CharField(label='Phone', required=True, max_length=100)
    user_id = forms.ModelChoiceField(label='User ID', queryset=hmod.User.objects.all())
    familyName = forms.CharField(label='Family Name', required=True, max_length=100)
    organizationType = forms.CharField(label='Organization Type', required=True, max_length=100)


@view_function
@permission_required('is_superuser', login_url='/homepage/login', raise_exception=False)
def create(request):
    legalentity = hmod.LegalEntity()
    legalentity.givenName = ''
    legalentity.creationDate = None
    legalentity.address1 = ''
    legalentity.address2 = ''
    legalentity.city = ''
    legalentity.state = ''
    legalentity.Zip = ''
    legalentity.email = ''
    legalentity.phone = ''
    legalentity.user_id = '0'
    legalentity.familyName = ''
    legalentity.organizationType = ''

    ''' OTHER FIELDS '''
    legalentity.save()

    return HttpResponseRedirect('/homepage/legalentities.edit/{}'.format(legalentity.id))

@view_function
@permission_required('is_superuser', login_url='/homepage/login', raise_exception=False)
def delete(request):

    try:
        legalentity = hmod.LegalEntity.objects.get(id=request.urlparams[0])
    except hmod.LegalEntity.DoesNotExist:
        return HttpResponseRedirect('/homepage/legalentities/')

    legalentity.delete()

    return HttpResponseRedirect('/homepage/legalentities')