# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1425799046.550786
_enable_loop = True
_template_filename = 'C:\\Users\\Zach\\PycharmProjects\\firstProject\\homepage\\templates/products.viewDetails.html'
_template_uri = 'products.viewDetails.html'
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
        product = context.get('product', UNDEFINED)
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        def content():
            return render_content(context._locals(__M_locals))
        __M_writer = context.writer()
        __M_writer('\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        product = context.get('product', UNDEFINED)
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        def content():
            return render_content(context)
        __M_writer = context.writer()
        __M_writer('\r\n    <table class="table table-striped table-bordered">\r\n        <tr>\r\n            <td>Name</td>\r\n            <td>Description</td>\r\n            <td>Category</td>\r\n            <td>Price per Unit</td>\r\n            <td>Quantity on Hand</td>\r\n        </tr>\r\n')
        if product:
            __M_writer('            <div class="col-xs-18 col-sm-4 col-md-2 col-md-offset-5">\r\n                <div class="productbox">\r\n                    <div class="imgthumb img-responsive">\r\n                        <img src="')
            __M_writer(str( STATIC_URL ))
            __M_writer('homepage/media/products/')
            __M_writer(str( product.pictureFileName ))
            __M_writer('">\r\n                    </div>\r\n                </div>\r\n            </div>\r\n            </div>\r\n            <div class="col-xs-18 col-sm-4 col-md-2 col-md-offset-5">\r\n                <tr>\r\n                    <td>')
            __M_writer(str( product.name ))
            __M_writer('</td>\r\n                    <td>')
            __M_writer(str( product.description ))
            __M_writer('</td>\r\n                    <td>')
            __M_writer(str( product.category ))
            __M_writer('</td>\r\n                    <td>')
            __M_writer(str( product.unitPrice ))
            __M_writer('</td>\r\n                    <td>')
            __M_writer(str( product.qtyOnHand ))
            __M_writer('</td>\r\n                </tr>\r\n            </div>\r\n')
        __M_writer('    </table>\r\n    <form class="form-horizontal" role="form">\r\n        <fieldset>\r\n\r\n\r\n\r\n          <!-- Text input-->\r\n            <div class="form-group col-md-12">\r\n                          <!-- Form Name -->\r\n                <!-- <legend class="text-center">Add to Cart <i class="fa fa-shopping-cart"></i></legend> -->\r\n                <label class="col-md-10 control-label" for="textinput">Quantity</label>\r\n                <div class="col-md-2">\r\n                    <input type="text" class="form-control bfh-number" data-min="1" data-max="')
        __M_writer(str( product.qtyOnHand ))
        __M_writer('" value="1">\r\n                </div>\r\n\r\n                <div class="form-group">\r\n                    <div class="col-sm-offset-2 col-sm-10">\r\n                      <div class="pull-right">\r\n                        <button type="submit" class="btn btn-warning btn-lg add_to_cart" data-pid="')
        __M_writer(str(product.id))
        __M_writer('">Add to Cart <i class="fa fa-cart-plus"></i></button>\r\n                      </div>\r\n                    </div>\r\n                </div>\r\n\r\n            </div>\r\n\r\n        </fieldset>\r\n    </form>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"line_map": {"64": 24, "65": 25, "66": 25, "67": 26, "68": 26, "69": 27, "70": 27, "71": 31, "72": 43, "73": 43, "74": 49, "75": 49, "81": 75, "27": 0, "36": 1, "46": 3, "54": 3, "55": 12, "56": 13, "57": 16, "58": 16, "59": 16, "60": 16, "61": 23, "62": 23, "63": 24}, "source_encoding": "ascii", "uri": "products.viewDetails.html", "filename": "C:\\Users\\Zach\\PycharmProjects\\firstProject\\homepage\\templates/products.viewDetails.html"}
__M_END_METADATA
"""
