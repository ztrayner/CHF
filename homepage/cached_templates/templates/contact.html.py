# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1421124877.570967
_enable_loop = True
_template_filename = 'C:\\Users\\Zach\\PycharmProjects\\firstProject\\homepage\\templates/contact.html'
_template_uri = 'contact.html'
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
        __M_writer('\r\n        <h3>Feel free to reach out to us with any questions you may have</h3>\r\n<div class="container">\r\n    <div class="row">\r\n      <div class="col-md-12">\r\n        <div class="alert alert-success"><span class="glyphicon glyphicon-send"></span><strong> Success! Message sent.</strong></div>\r\n        <div class="alert alert-danger"><span class="glyphicon glyphicon-alert"></span><strong> Error! Please complete required fields.</strong></div>\r\n    </div>\r\n    <form role="form" action="" method="post" >\r\n        <div class="col-lg-6">\r\n          <div class="well well-sm"><i class="glyphicon glyphicon-ok"></i><strong> Required Field </strong></div>\r\n          <div class="form-group">\r\n            <label for="InputName">Your Name</label>\r\n            <div class="input-group">\r\n              <input type="text" class="form-control" name="InputName" id="InputName" placeholder="Enter Name" required>\r\n              <span class="input-group-addon"><i class="glyphicon glyphicon-ok form-control-feedback"></i></span></div>\r\n          </div>\r\n          <div class="form-group">\r\n            <label for="InputEmail">Your Email</label>\r\n            <div class="input-group">\r\n              <input type="email" class="form-control" id="InputEmail" name="InputEmail" placeholder="Enter Email" required>\r\n              <span class="input-group-addon"><i class="glyphicon glyphicon-ok form-control-feedback"></i></span></div>\r\n          </div>\r\n          <div class="form-group">\r\n            <label for="InputMessage">Message</label>\r\n            <div class="input-group">\r\n              <textarea name="InputMessage" id="InputMessage" class="form-control" rows="5" required></textarea>\r\n              <span class="input-group-addon"><i class="glyphicon glyphicon-ok form-control-feedback"></i></span></div>\r\n          </div>\r\n          <input type="submit" name="submit" id="submit" value="Submit" class="btn btn-info pull-right">\r\n        </div>\r\n      </form>\r\n      <hr class="featurette-divider hidden-lg">\r\n    </div>\r\n\r\n</div>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "ascii", "line_map": {"56": 50, "34": 1, "27": 0, "44": 3, "50": 3}, "uri": "contact.html", "filename": "C:\\Users\\Zach\\PycharmProjects\\firstProject\\homepage\\templates/contact.html"}
__M_END_METADATA
"""
