# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1421117152.837983
_enable_loop = True
_template_filename = 'C:\\Users\\Zach\\PycharmProjects\\firstProject\\homepage\\templates/terms.html'
_template_uri = 'terms.html'
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
        __M_writer('\r\n        <h3>This is the terms page</h3>\r\n        <p>These are the terms... The name "Colonial Heritage Foundation" is another name for the Society for the Preservation of America\'s Founding Values, Inc., which is a 501(3)(c) public charity...etc.\r\n            <br/><br/>Do you accept these terms?</p>\r\n        <div class="btn-group" role="group">\r\n            <button type="button" class="btn btn-danger">Decline</button>\r\n            <button type="button" class="btn btn-success">Accept</button>\r\n        </div>\r\n\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"line_map": {"56": 50, "34": 1, "27": 0, "44": 3, "50": 3}, "uri": "terms.html", "filename": "C:\\Users\\Zach\\PycharmProjects\\firstProject\\homepage\\templates/terms.html", "source_encoding": "ascii"}
__M_END_METADATA
"""
