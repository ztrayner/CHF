# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1425790751.284264
_enable_loop = True
_template_filename = 'C:\\Users\\Zach\\PycharmProjects\\firstProject\\homepage\\templates/products.html'
_template_uri = 'products.html'
_source_encoding = 'ascii'
import os, os.path, re
_exports = ['content']


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    pass
def _mako_inherit(template, context):
    _mako_generate_namespaces(context)
    return runtime._inherit_from(context, 'base.htm', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        user = context.get('user', UNDEFINED)
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        def content():
            return render_content(context._locals(__M_locals))
        products = context.get('products', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n\r\n')
        __M_writer('\r\n\r\n')
        __M_writer('\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        __M_writer('\r\n\r\n')
        __M_writer('\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        user = context.get('user', UNDEFINED)
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        def content():
            return render_content(context)
        products = context.get('products', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n')
        if products:
            __M_writer('        <div class="container">\r\n            <div class="row">\r\n')
            for product in products:
                __M_writer('                            <div class="col-xs-18 col-sm-4 col-md-3">\r\n                                <div class="productbox">\r\n                                    <div class="imgthumb img-responsive">\r\n                                        <img src="')
                __M_writer(str( STATIC_URL ))
                __M_writer('homepage/media/products/')
                __M_writer(str( product.pictureFileName ))
                __M_writer('">\r\n                                    </div>\r\n                                    <div class="caption">\r\n                                        <h5>')
                __M_writer(str( product.name ))
                __M_writer('<br/>&#36;')
                __M_writer(str( product.unitPrice ))
                __M_writer('</h5>\r\n')
                if user and user.is_superuser is True:
                    __M_writer('                                            <a href="#" class="btn btn-default btn-xs pull-right" role="button"><i class="glyphicon glyphicon-edit"></i></a>\r\n')
                __M_writer('                                        <a href="#" class="btn btn-warning btn-xs add_to_cart" data-pid="')
                __M_writer(str( product.id ))
                __M_writer('" role="button">Add to Cart</a>\r\n                                        <a href="/homepage/products.viewDetails/')
                __M_writer(str( product.id ))
                __M_writer('" class="btn btn-default btn-xs" role="button">Details</a>\r\n                                    </div>\r\n                                </div>\r\n                            </div>\r\n')
            __M_writer('            </div>\r\n        </div>\r\n')
        else:
            __M_writer('        <p>There are no products to show</p>\r\n')
        __M_writer('\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"uri": "products.html", "filename": "C:\\Users\\Zach\\PycharmProjects\\firstProject\\homepage\\templates/products.html", "line_map": {"64": 20, "65": 23, "66": 23, "67": 23, "68": 23, "69": 26, "70": 26, "71": 26, "72": 26, "73": 27, "74": 28, "75": 30, "76": 30, "77": 30, "78": 31, "79": 31, "80": 36, "81": 38, "82": 39, "83": 41, "89": 83, "27": 0, "37": 1, "38": 7, "39": 13, "44": 42, "45": 48, "51": 15, "60": 15, "61": 16, "62": 17, "63": 19}, "source_encoding": "ascii"}
__M_END_METADATA
"""
