# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1425799082.749509
_enable_loop = True
_template_filename = 'C:\\Users\\Zach\\PycharmProjects\\firstProject\\homepage\\templates/cart.html'
_template_uri = 'cart.html'
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
        def content():
            return render_content(context._locals(__M_locals))
        products = context.get('products', UNDEFINED)
        __M_writer = context.writer()
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
        def content():
            return render_content(context)
        products = context.get('products', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n\r\n<div>\r\n')
        if products:
            for product in products:
                __M_writer('            <h3>')
                __M_writer(str(product.name))
                __M_writer('</h3>\r\n            <div class="text-muted text-left">\r\n                Description: ')
                __M_writer(str(product.description))
                __M_writer('\r\n            </div>\r\n            <div class="text-muted text-left">\r\n                Category: ')
                __M_writer(str(product.category))
                __M_writer('\r\n            </div>\r\n            <div class="text-left">\r\n                Price: ')
                __M_writer(str(product.unitPrice))
                __M_writer('\r\n            </div>\r\n            <a type="button" data-pid="')
                __M_writer(str( product.id ))
                __M_writer('" href="/homepage/cart.delete/')
                __M_writer(str( product.id ))
                __M_writer('" class="delete_btn btn-warning btn-xs">Delete</a>\r\n')
        __M_writer('</div>\r\n<a type="button" href="/homepage/checkout/" class="btn btn-primary">Check Out</a>\r\n\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"line_map": {"64": 16, "65": 16, "66": 18, "67": 18, "68": 18, "69": 18, "70": 21, "76": 70, "27": 0, "35": 1, "40": 24, "41": 117, "47": 3, "54": 3, "55": 6, "56": 7, "57": 8, "58": 8, "59": 8, "60": 10, "61": 10, "62": 13, "63": 13}, "source_encoding": "ascii", "uri": "cart.html", "filename": "C:\\Users\\Zach\\PycharmProjects\\firstProject\\homepage\\templates/cart.html"}
__M_END_METADATA
"""
