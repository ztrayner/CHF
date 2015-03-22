# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1425793987.929119
_enable_loop = True
_template_filename = 'C:\\Users\\Zach\\PycharmProjects\\firstProject\\homepage\\templates/myaccount.html'
_template_uri = 'myaccount.html'
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
        users = context.get('users', UNDEFINED)
        user = context.get('user', UNDEFINED)
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
        users = context.get('users', UNDEFINED)
        user = context.get('user', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n    <table class="table table-striped table-bordered">\r\n        <tr>\r\n            <td>ID</td>\r\n            <td>Username</td>\r\n            <td>First name</td>\r\n            <td>Last Name</td>\r\n            <td>Email</td>\r\n            <td>Actions</td>\r\n        </tr>\r\n')
        if users:
            __M_writer('            <tr>\r\n                <td>')
            __M_writer(str( user.id ))
            __M_writer('</td>\r\n                <td>')
            __M_writer(str( user.username ))
            __M_writer('</td>\r\n                <td>')
            __M_writer(str( user.first_name ))
            __M_writer('</td>\r\n                <td>')
            __M_writer(str( user.last_name ))
            __M_writer('</td>\r\n                <td>')
            __M_writer(str( user.email ))
            __M_writer('</td>\r\n                <td><a href="/homepage/myaccount.edit/')
            __M_writer(str( user.id ))
            __M_writer('/">Edit</a> | <a href="/homepage/myaccount.changepassword/')
            __M_writer(str( user.id ))
            __M_writer('/">Change Password</a>\r\n            </tr>\r\n')
        __M_writer('    </table>\r\n')
        if user and user.is_superuser is True:
            __M_writer('        <a role="button" class="btn btn-primary pull-right" id="check_overdue_items" href="myaccount.lateitemsemail">Send Overdue Items Email</a>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "ascii", "filename": "C:\\Users\\Zach\\PycharmProjects\\firstProject\\homepage\\templates/myaccount.html", "line_map": {"64": 18, "65": 19, "66": 19, "67": 20, "68": 20, "69": 20, "70": 20, "71": 23, "72": 24, "73": 25, "79": 73, "27": 0, "36": 1, "46": 3, "54": 3, "55": 13, "56": 14, "57": 15, "58": 15, "59": 16, "60": 16, "61": 17, "62": 17, "63": 18}, "uri": "myaccount.html"}
__M_END_METADATA
"""
