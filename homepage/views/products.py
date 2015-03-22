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
def process_request(request):
    params = {}

    params['products'] = hmod.Product.objects.all()

    return templater.render_to_response(request, 'products.html', params)

@view_function
def viewDetails(request):
    params = {}

    try:
        params['product'] = hmod.Product.objects.get(id=request.urlparams[0])
    except hmod.Product.DoesNotExist:
        return HttpResponseRedirect('/homepage/')

    return templater.render_to_response(request, 'products.viewDetails.html', params)



# # create/edit all products
# @view_function
# @permission_required('is_superuser', login_url='/homepage/login', raise_exception=False)
# def edit(request):
#     params = {}
#
#     try:
#         products = hmod.Product.objects.get(id=request.urlparams[0])
#     except hmod.Product.DoesNotExist:
#         return HttpResponseRedirect('/homepage/product/')
#
#     form = ProductEditForm(initial={
#         'dateTaken': products.dateTaken,
#         'placeTaken': products.placeTaken,
#         'image': products.image,
#         'producter_id': products.producter_id,
#         })
#     if request.method == 'POST':
#         form = ProductEditForm(request.POST)
#         if form.is_valid():
#             products.dateTaken = form.cleaned_data['dateTaken']
#             products.placeTaken = form.cleaned_data['placeTaken']
#             products.image = form.cleaned_data['image']
#             products.producter_id = form.cleaned_data['producter_id']
#             products.save()
#             return HttpResponseRedirect('/homepage/product/')
#
#
#     params['form'] = form
#     return templater.render_to_response(request, 'product.edit.html', params)
#
#
# class ProductEditForm(forms.Form):
#     dateTaken = forms.DateField(label="Date Taken", required=True)
#     placeTaken = forms.CharField(label="Place Taken", required=True, max_length=100)
#     image = forms.CharField(label="image", required=True, max_length=100)
#     producter_id = forms.CharField(label="Producter ID", required=True, max_length=100)
#
# @view_function
# @permission_required('is_superuser', login_url='/homepage/login', raise_exception=False)
# def create(request):
#     product = hmod.Product()
#     product.dateTaken = None
#     product.placeTaken = ''
#     product.image = ''
#
#     ''' OTHER FIELDS '''
#     product.save()
#
#     return HttpResponseRedirect('/homepage/product.edit/{}'.format(product.id))
#
# @view_function
# @permission_required('is_superuser', login_url='/homepage/login', raise_exception=False)
# def delete(request):
#
#     try:
#         product = hmod.Product.objects.get(id=request.urlparams[0])
#     except hmod.Product.DoesNotExist:
#         return HttpResponseRedirect('/homepage/product/')
#
#     product.delete()
#
#     return HttpResponseRedirect('/homepage/product')