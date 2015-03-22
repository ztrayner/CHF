# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1423270293.416327
_enable_loop = True
_template_filename = 'C:\\Users\\Zach\\PycharmProjects\\firstProject\\homepage\\templates/publicevents.html'
_template_uri = 'publicevents.html'
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
        publicevents = context.get('publicevents', UNDEFINED)
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
        publicevents = context.get('publicevents', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n    <table class="table table-striped table-bordered">\r\n        <tr>\r\n            <td>ID</td>\r\n            <td>Name</td>\r\n            <td>Description</td>\r\n            <td>Event ID</td>\r\n            <td>Actions</td>\r\n        </tr>\r\n')
        if publicevents:
            for event in publicevents:
                __M_writer('                <tr>\r\n                    <td>')
                __M_writer(str( event.id ))
                __M_writer('</td>\r\n                    <td>')
                __M_writer(str( event.name ))
                __M_writer('</td>\r\n                    <td>')
                __M_writer(str( event.description ))
                __M_writer('</td>\r\n                    <td>')
                __M_writer(str( event.event_id ))
                __M_writer('</td>\r\n                    <td><a href="/homepage/publicevents.edit/')
                __M_writer(str( event.id ))
                __M_writer('">Edit</a> | <a href="/homepage/publicevents.delete/')
                __M_writer(str( event.id ))
                __M_writer('">Delete</a></td>\r\n                </tr>\r\n')
        __M_writer('    </table>\r\n    <div class = "text-right">\r\n        <a href="/homepage/publicevents.create" class="btn btn-success"><i class="fa fa-calendar-o"></i> Create New Public Event</a>\r\n    </div>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"line_map": {"64": 19, "65": 19, "66": 19, "35": 1, "68": 23, "74": 68, "45": 3, "27": 0, "67": 19, "52": 3, "53": 12, "54": 13, "55": 14, "56": 15, "57": 15, "58": 16, "59": 16, "60": 17, "61": 17, "62": 18, "63": 18}, "source_encoding": "ascii", "uri": "publicevents.html", "filename": "C:\\Users\\Zach\\PycharmProjects\\firstProject\\homepage\\templates/publicevents.html"}
__M_END_METADATA
"""
