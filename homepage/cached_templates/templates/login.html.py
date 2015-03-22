# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1425784585.838845
_enable_loop = True
_template_filename = 'C:\\Users\\Zach\\PycharmProjects\\firstProject\\homepage\\templates/login.html'
_template_uri = 'login.html'
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
        user = context.get('user', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        __M_writer('\r\n\r\n\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def content():
            return render_content(context)
        user = context.get('user', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n\r\n    <div class="col-8">\r\n')
        if user and user.is_anonymous():
            __M_writer('            <btn class="btn btn-default btn-lrg" id="showLoginModal" data-toggle="modal" data-target="#loginModal"><span class="fa fa-sign-in"></span> Login </btn>\r\n            <div class="modal fade bs-example-modal-sm" id="loginModal" tabindex="-1" role="dialog" aria-labelledby="mySmallModalLabel" aria-hidden="true">\r\n                <div class="modal-dialog modal-sm">\r\n                    <div class="modal-content text-center block-center">\r\n                    ...\r\n                    </div>\r\n                </div>\r\n            </div>\r\n')
        else:
            __M_writer("            <h3>You're already logged in!</h3>\r\n")
        __M_writer('    </div>\r\n\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"uri": "login.html", "source_encoding": "ascii", "filename": "C:\\Users\\Zach\\PycharmProjects\\firstProject\\homepage\\templates/login.html", "line_map": {"64": 58, "56": 15, "35": 1, "53": 3, "54": 6, "55": 7, "40": 20, "57": 16, "58": 18, "27": 0, "46": 3}}
__M_END_METADATA
"""
