# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1425609911.097193
_enable_loop = True
_template_filename = 'C:\\Users\\Zach\\PycharmProjects\\firstProject\\homepage\\templates/photograph.html'
_template_uri = 'photograph.html'
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
        photographs = context.get('photographs', UNDEFINED)
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
        photographs = context.get('photographs', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n    <table class="table table-striped table-bordered">\r\n        <tr>\r\n            <td>ID</td>\r\n            <td>Date Taken</td>\r\n            <td>Place Taken</td>\r\n            <td>Photographer\r\n            <td>Actions</td>\r\n        </tr>\r\n')
        for photograph in photographs:
            __M_writer('            <tr>\r\n                <td>')
            __M_writer(str( photograph.id ))
            __M_writer('</td>\r\n                <td>')
            __M_writer(str( photograph.dateTaken ))
            __M_writer('</td>\r\n                <td>')
            __M_writer(str( photograph.placeTaken ))
            __M_writer('</td>\r\n                <td>')
            __M_writer(str( photograph.photographer.first_name + ' ' + photograph.photographer.last_name ))
            __M_writer('</td>\r\n                <td><a href="/homepage/photograph.edit/')
            __M_writer(str( photograph.id ))
            __M_writer('/">Edit</a> | <a href="/homepage/users.delete/')
            __M_writer(str( photograph.id ))
            __M_writer('">Delete</a></td>\r\n            </tr>\r\n')
        __M_writer('    </table>\r\n    <div class = "text-right">\r\n        <a href="/homepage/photograph.create" class="btn btn-success"><i class="fa fa-user-plus"></i> Create New Photo</a>\r\n    </div>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "ascii", "line_map": {"64": 18, "65": 18, "66": 18, "35": 1, "73": 67, "45": 3, "27": 0, "67": 21, "52": 3, "53": 12, "54": 13, "55": 14, "56": 14, "57": 15, "58": 15, "59": 16, "60": 16, "61": 17, "62": 17, "63": 18}, "filename": "C:\\Users\\Zach\\PycharmProjects\\firstProject\\homepage\\templates/photograph.html", "uri": "photograph.html"}
__M_END_METADATA
"""
