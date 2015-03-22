# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1423271255.840896
_enable_loop = True
_template_filename = 'C:\\Users\\Zach\\PycharmProjects\\firstProject\\homepage\\templates/agents.html'
_template_uri = 'agents.html'
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
        agents = context.get('agents', UNDEFINED)
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
        agents = context.get('agents', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n    <table class="table table-striped table-bordered">\r\n        <tr>\r\n            <td>Legal Entity ID</td>\r\n            <td>Appointment Date</td>\r\n            <td>Actions</td>\r\n        </tr>\r\n')
        if agents:
            for agent in agents:
                __M_writer('                <tr>\r\n                    <td>')
                __M_writer(str( agent.legalentity_ptr_id ))
                __M_writer('</td>\r\n                    <td>')
                __M_writer(str( agent.appointmentDate ))
                __M_writer('</td>\r\n                    <td><a href="/homepage/agents.edit/')
                __M_writer(str( agent.id ))
                __M_writer('">Edit</a> | <a href="/homepage/agents.delete/')
                __M_writer(str( agent.id ))
                __M_writer('">Delete</a></td>\r\n                </tr>\r\n')
        __M_writer('    </table>\r\n    <div class = "text-right">\r\n        <a href="/homepage/agents.create" class="btn btn-success"><i class="fa fa-user-plus"></i> Add New Agent</a>\r\n    </div>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"uri": "agents.html", "line_map": {"64": 19, "35": 1, "70": 64, "45": 3, "27": 0, "52": 3, "53": 10, "54": 11, "55": 12, "56": 13, "57": 13, "58": 14, "59": 14, "60": 15, "61": 15, "62": 15, "63": 15}, "filename": "C:\\Users\\Zach\\PycharmProjects\\firstProject\\homepage\\templates/agents.html", "source_encoding": "ascii"}
__M_END_METADATA
"""
