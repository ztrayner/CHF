# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1423344185.038814
_enable_loop = True
_template_filename = 'C:\\Users\\Zach\\PycharmProjects\\firstProject\\homepage\\templates/users.html'
_template_uri = 'users.html'
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
        __M_writer = context.writer()
        __M_writer('\r\n    <table class="table table-striped table-bordered">\r\n        <tr>\r\n            <td>ID</td>\r\n            <td>Username</td>\r\n            <td>First name</td>\r\n            <td>Last Name</td>\r\n            <td>Email</td>\r\n            <td>Actions</td>\r\n        </tr>\r\n')
        if users:
            for user in users:
                __M_writer('                <tr>\r\n                    <td>')
                __M_writer(str( user.id ))
                __M_writer('</td>\r\n                    <td>')
                __M_writer(str( user.username ))
                __M_writer('</td>\r\n                    <td>')
                __M_writer(str( user.first_name ))
                __M_writer('</td>\r\n                    <td>')
                __M_writer(str( user.last_name ))
                __M_writer('</td>\r\n                    <td>')
                __M_writer(str( user.email ))
                __M_writer('</td>\r\n                    <td><a href="/homepage/users.edit/')
                __M_writer(str( user.id ))
                __M_writer('/">Edit</a> | <a href="/homepage/users.delete/')
                __M_writer(str( user.id ))
                __M_writer('">Delete</a></td>\r\n                </tr>\r\n')
        __M_writer('    </table>\r\n    <div class = "text-right">\r\n        <a href="/homepage/users.create" class="btn btn-success"><i class="fa fa-user-plus"></i> New User</a>\r\n    </div>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"line_map": {"64": 20, "65": 20, "66": 21, "67": 21, "68": 21, "69": 21, "70": 25, "76": 70, "27": 0, "35": 1, "45": 3, "52": 3, "53": 13, "54": 14, "55": 15, "56": 16, "57": 16, "58": 17, "59": 17, "60": 18, "61": 18, "62": 19, "63": 19}, "source_encoding": "ascii", "filename": "C:\\Users\\Zach\\PycharmProjects\\firstProject\\homepage\\templates/users.html", "uri": "users.html"}
__M_END_METADATA
"""
