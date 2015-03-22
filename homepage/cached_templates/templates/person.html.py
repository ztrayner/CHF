# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1422742328.614418
_enable_loop = True
_template_filename = 'C:\\Users\\Zach\\PycharmProjects\\firstProject\\homepage\\templates/person.html'
_template_uri = 'person.html'
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
        persons = context.get('persons', UNDEFINED)
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
        persons = context.get('persons', UNDEFINED)
        def content():
            return render_content(context)
        __M_writer = context.writer()
        __M_writer('\r\n    <table class="table table-striped table-bordered">\r\n        <tr>\r\n            <td>ID</td>\r\n            <td>First name</td>\r\n            <td>Last Name</td>\r\n            <td>Actions</td>\r\n        </tr>\r\n')
        for person in persons:
            __M_writer('            <tr>\r\n                <td>')
            __M_writer(str( person.id ))
            __M_writer('</td>\r\n                <td>')
            __M_writer(str( person.givenName ))
            __M_writer('</td>\r\n                <td>')
            __M_writer(str( person.familyName ))
            __M_writer('</td>\r\n                <td><a href="/homepage/person.edit/')
            __M_writer(str( person.id ))
            __M_writer('/">Edit</a></td>\r\n            </tr>\r\n')
        __M_writer('    </table>\r\n    <div class = "text-right">\r\n        <a href="/homepage/person.create/" class="btn btn-success"><i class="fa fa-user-plus"></i> Create New User</a>\r\n    </div>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "C:\\Users\\Zach\\PycharmProjects\\firstProject\\homepage\\templates/person.html", "uri": "person.html", "source_encoding": "ascii", "line_map": {"35": 1, "69": 63, "45": 3, "27": 0, "52": 3, "53": 11, "54": 12, "55": 13, "56": 13, "57": 14, "58": 14, "59": 15, "60": 15, "61": 16, "62": 16, "63": 19}}
__M_END_METADATA
"""
