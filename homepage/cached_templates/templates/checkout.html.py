# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1425776037.105763
_enable_loop = True
_template_filename = 'C:\\Users\\Zach\\PycharmProjects\\firstProject\\homepage\\templates/checkout.html'
_template_uri = 'checkout.html'
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
        def content():
            return render_content(context)
        __M_writer = context.writer()
        __M_writer('\r\n  <div class="row">\r\n    <div class="col-md-4 col-md-offset-4">\r\n      <form class="form-horizontal" role="form">\r\n        <fieldset>\r\n\r\n          <!-- Form Name -->\r\n          <legend class="text-center">Checkout</legend>\r\n\r\n          <!-- Text input-->\r\n          <div class="form-group">\r\n            <label class="col-sm-2 control-label" for="textinput">Address</label>\r\n            <div class="col-sm-10">\r\n              <input type="text" placeholder="Address Line 1" class="form-control">\r\n            </div>\r\n          </div>\r\n\r\n          <!-- Text input-->\r\n          <div class="form-group">\r\n            <label class="col-sm-2 control-label" for="textinput"></label>\r\n            <div class="col-sm-10">\r\n              <input type="text" placeholder="Address Line 2" class="form-control">\r\n            </div>\r\n          </div>\r\n\r\n          <!-- Text input-->\r\n          <div class="form-group">\r\n            <label class="col-sm-2 control-label" for="textinput">City</label>\r\n            <div class="col-sm-10">\r\n              <input type="text" placeholder="City" class="form-control">\r\n            </div>\r\n          </div>\r\n\r\n          <!-- Text input-->\r\n          <div class="form-group">\r\n            <label class="col-sm-2 control-label" for="textinput">State</label>\r\n            <div class="col-sm-4">\r\n              <input type="text" placeholder="State" class="form-control">\r\n            </div>\r\n\r\n            <label class="col-sm-2 control-label" for="textinput">Zip Code</label>\r\n            <div class="col-sm-4">\r\n              <input type="text" placeholder="Zip Code" class="form-control">\r\n            </div>\r\n          </div>\r\n\r\n          <div class="form-group">\r\n            <label class="col-sm-3 control-label" for="textinput">\r\n              <span>Card Number</span>\r\n            </label>\r\n            <div class="col-sm-9">\r\n              <input type="text" placeholder="Card Number" class="form-control">\r\n            </div>\r\n          </div>\r\n\r\n          <div class="form-group">\r\n            <label class="col-sm-2 control-label" for="textinput">CVC</label>\r\n            <div class="col-sm-4">\r\n              <input type="text" placeholder="CVC" class="form-control">\r\n            </div>\r\n\r\n            <label class="col-sm-2 control-label" for="textinput">Expiration</label>\r\n            <div class="col-sm-4">\r\n              <input type="text" placeholder="MM/YYYY" class="form-control">\r\n            </div>\r\n          </div>\r\n\r\n          <!-- Text input -->\r\n          <div class="form-group">\r\n            <div class="col-sm-offset-2 col-sm-10">\r\n              <div class="pull-right">\r\n                <button type="submit" class="btn btn-default">Cancel</button>\r\n                <button type="submit" class="btn btn-primary">Confirm</button>\r\n              </div>\r\n            </div>\r\n          </div>\r\n\r\n        </fieldset>\r\n      </form>\r\n    </div><!-- /.col-lg-12 -->\r\n</div><!-- /.row -->\r\n\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"uri": "checkout.html", "source_encoding": "ascii", "filename": "C:\\Users\\Zach\\PycharmProjects\\firstProject\\homepage\\templates/checkout.html", "line_map": {"56": 50, "34": 1, "27": 0, "44": 3, "50": 3}}
__M_END_METADATA
"""
