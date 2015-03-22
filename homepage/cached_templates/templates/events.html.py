# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1423268345.665855
_enable_loop = True
_template_filename = 'C:\\Users\\Zach\\PycharmProjects\\firstProject\\homepage\\templates/events.html'
_template_uri = 'events.html'
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
        events = context.get('events', UNDEFINED)
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
        events = context.get('events', UNDEFINED)
        def content():
            return render_content(context)
        __M_writer = context.writer()
        __M_writer('\r\n    <table class="table table-striped table-bordered">\r\n        <tr>\r\n            <td>ID</td>\r\n            <td>Start Date</td>\r\n            <td>End Date</td>\r\n            <td>Map Name</td>\r\n            <td>Actions</td>\r\n        </tr>\r\n')
        if events:
            for event in events:
                __M_writer('                <tr>\r\n                    <td>')
                __M_writer(str( event.id ))
                __M_writer('</td>\r\n                    <td>')
                __M_writer(str( event.startDate ))
                __M_writer('</td>\r\n                    <td>')
                __M_writer(str( event.endDate ))
                __M_writer('</td>\r\n                    <td>')
                __M_writer(str( event.mapName ))
                __M_writer('</td>\r\n                    <td><a href="/homepage/events.edit/')
                __M_writer(str( event.id ))
                __M_writer('">Edit</a> | <a href="/homepage/events.delete/')
                __M_writer(str( event.id ))
                __M_writer('">Delete</a></td>\r\n                </tr>\r\n')
        __M_writer('    </table>\r\n    <div class = "text-right">\r\n        <a href="/homepage/events.create" class="btn btn-success"><i class="fa fa-calendar-o"></i> Create New Event</a>\r\n    </div>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"uri": "events.html", "line_map": {"64": 19, "65": 19, "66": 19, "35": 1, "68": 23, "74": 68, "45": 3, "27": 0, "67": 19, "52": 3, "53": 12, "54": 13, "55": 14, "56": 15, "57": 15, "58": 16, "59": 16, "60": 17, "61": 17, "62": 18, "63": 18}, "source_encoding": "ascii", "filename": "C:\\Users\\Zach\\PycharmProjects\\firstProject\\homepage\\templates/events.html"}
__M_END_METADATA
"""
