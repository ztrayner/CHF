# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1423335463.207791
_enable_loop = True
_template_filename = 'C:\\Users\\Zach\\PycharmProjects\\firstProject\\homepage\\templates/legalentities.html'
_template_uri = 'legalentities.html'
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
        legalentities = context.get('legalentities', UNDEFINED)
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
        legalentities = context.get('legalentities', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n    <table class="table table-striped table-bordered">\r\n        <tr>\r\n            <td>ID</td>\r\n            <td>Given Name</td>\r\n            <td>Family Name</td>\r\n            <td>Creation Date</td>\r\n            <td>Email</td>\r\n            <td>Actions</td>\r\n        </tr>\r\n')
        if legalentities:
            for legalentity in legalentities:
                __M_writer('                <tr>\r\n                    <td>')
                __M_writer(str( legalentity.id ))
                __M_writer('</td>\r\n                    <td>')
                __M_writer(str( legalentity.givenName ))
                __M_writer('</td>\r\n                    <td>')
                __M_writer(str( legalentity.familyName ))
                __M_writer('</td>\r\n                    <td>')
                __M_writer(str( legalentity.creationDate ))
                __M_writer('</td>\r\n                    <td>')
                __M_writer(str( legalentity.email ))
                __M_writer('</td>\r\n                    <td><a href="/homepage/legalentities.edit/')
                __M_writer(str( legalentity.id ))
                __M_writer('/">Edit</a> | <a href="/homepage/legalentities.delete/')
                __M_writer(str( legalentity.id ))
                __M_writer('">Delete</a></td>\r\n                </tr>\r\n')
        __M_writer('    </table>\r\n    <div class = "text-right">\r\n        <a href="/homepage/legalentities.create" class="btn btn-success"><i class="fa fa-user-plus"></i> New Legal Entity</a>\r\n    </div>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"line_map": {"64": 20, "65": 20, "66": 21, "67": 21, "68": 21, "69": 21, "70": 25, "76": 70, "27": 0, "35": 1, "45": 3, "52": 3, "53": 13, "54": 14, "55": 15, "56": 16, "57": 16, "58": 17, "59": 17, "60": 18, "61": 18, "62": 19, "63": 19}, "source_encoding": "ascii", "uri": "legalentities.html", "filename": "C:\\Users\\Zach\\PycharmProjects\\firstProject\\homepage\\templates/legalentities.html"}
__M_END_METADATA
"""
