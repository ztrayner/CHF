# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1425798256.796525
_enable_loop = True
_template_filename = 'C:\\Users\\Zach\\PycharmProjects\\firstProject\\homepage\\templates/base.htm'
_template_uri = 'base.htm'
_source_encoding = 'ascii'
import os, os.path, re
_exports = ['right', 'header', 'content', 'left', 'footer']


from django_mako_plus.controller import static_files 

def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        user = context.get('user', UNDEFINED)
        def content():
            return render_content(context._locals(__M_locals))
        def header():
            return render_header(context._locals(__M_locals))
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        self = context.get('self', UNDEFINED)
        def left():
            return render_left(context._locals(__M_locals))
        request = context.get('request', UNDEFINED)
        def right():
            return render_right(context._locals(__M_locals))
        def footer():
            return render_footer(context._locals(__M_locals))
        __M_writer = context.writer()
        __M_writer('\r\n')
        __M_writer('\r\n')
        static_renderer = static_files.StaticRenderer(self) 
        
        __M_locals_builtin_stored = __M_locals_builtin()
        __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['static_renderer'] if __M_key in __M_locals_builtin_stored]))
        __M_writer('\r\n\r\n<!DOCTYPE html>\r\n<html>\r\n  <meta charset="UTF-8">\r\n  <head>\r\n    \r\n    <title>Colonial Heritage Foundation</title>\r\n    \r\n')
        __M_writer('    <script src="http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js"></script>\r\n    <script src="')
        __M_writer(str( STATIC_URL ))
        __M_writer('homepage/media/jquery.form.min.js"></script>\r\n    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.2/js/bootstrap.min.js"></script>\r\n    <script src="https://cdnjs.cloudflare.com/ajax/libs/bootstrap-formhelpers/2.3.0/js/bootstrap-formhelpers.min.js"></script>\r\n    <script src="')
        __M_writer(str( STATIC_URL ))
        __M_writer('homepage/scripts/login.js"></script>\r\n    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.1/css/bootstrap.min.css">\r\n    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.2/css/bootstrap-theme.min.css">\r\n    <link rel="stylesheet" href="//maxcdn.bootstrapcdn.com/font-awesome/4.3.0/css/font-awesome.min.css">\r\n    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/bootstrap-formhelpers/2.3.0/css/bootstrap-formhelpers.min.css">\r\n\r\n')
        __M_writer('    <link rel="stylesheet" href="')
        __M_writer(str( STATIC_URL ))
        __M_writer('homepage/styles/zachBootstrap.css">\r\n    <link rel="shortcut icon" href="')
        __M_writer(str( STATIC_URL ))
        __M_writer('homepage/media/favicon.ico" type="image/x-icon" />\r\n\r\n')
        __M_writer('    ')
        __M_writer(str( static_renderer.get_template_css(request, context)  ))
        __M_writer('\r\n  \r\n  </head>\r\n\r\n\r\n\r\n\r\n  <body>\r\n      <header class="col-md-12">\r\n        ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'header'):
            context['self'].header(**pageargs)
        

        __M_writer('\r\n        </header>\r\n\r\n      <div class="container-fluid">\r\n          <div class="row">\r\n              <div class="col-md-2">\r\n                  ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'left'):
            context['self'].left(**pageargs)
        

        __M_writer('\r\n              </div>\r\n\r\n\r\n              <div class="col-md-8">\r\n                  ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        __M_writer('\r\n              </div>\r\n\r\n              <div class="col-md-2">\r\n                  ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'right'):
            context['self'].right(**pageargs)
        

        __M_writer('\r\n              </div>\r\n          </div>\r\n          <div class="row">\r\n              <div class="col-md-2">\r\n                    <p></p>\r\n              </div>\r\n              <footer class="col-md-8 text-center center-block">\r\n                  ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'footer'):
            context['self'].footer(**pageargs)
        

        __M_writer('\r\n              </footer>\r\n              <div class="col-md-2">\r\n                  <p></p>\r\n              </div>\r\n          </div>\r\n\r\n\r\n\r\n')
        __M_writer('    ')
        __M_writer(str( static_renderer.get_template_js(request, context)  ))
        __M_writer('\r\n    </div>\r\n  </body>\r\n</html>')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_right(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def right():
            return render_right(context)
        __M_writer = context.writer()
        __M_writer('\r\n                      <!-- This right side has no template, but may be overwritten by using the right block on a page -->\r\n                  ')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_header(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def header():
            return render_header(context)
        __M_writer = context.writer()
        __M_writer('\r\n            <div class="jumbotron">\r\n                <h1>Colonial Heritage Foundation</h1>\r\n            </div>\r\n        <div class="modal fade bs-example-modal-sm" id="loginModal" tabindex="-1" role="dialog" aria-labelledby="mySmallModalLabel" aria-hidden="true">\r\n            <div class="modal-dialog modal-sm">\r\n                <div class="modal-content text-center block-center">\r\n                  ...\r\n                </div>\r\n            </div>\r\n        </div>\r\n        ')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def content():
            return render_content(context)
        __M_writer = context.writer()
        __M_writer('\r\n                      Site content goes here in sub-templates.\r\n                  ')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_left(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        user = context.get('user', UNDEFINED)
        def left():
            return render_left(context)
        __M_writer = context.writer()
        __M_writer('\r\n                      <ul class="nav nav-pills nav-stacked">\r\n                          <li role="presentation"><a href="/homepage/"><span class="glyphicon glyphicon-home"></span> Home </a></li>\r\n                          <li role="presentation"><a href="/homepage/about"><i class="fa fa-plus-circle"></i> About Us</a></li>\r\n                          <li role="presentation"><a href="/homepage/contact"><i class="fa fa-envelope-o"></i> Contact</a></li>\r\n                          <li role="presentation"><a href="/homepage/terms"><i class="fa fa-file-text-o"></i> Terms </a></li>\r\n                          <li role="presentation"><a href="/homepage/products"><i class="fa fa-tag"></i> Products </a></li>\r\n                          <li role="presentation"><a href="/homepage/cart"><i class="fa fa-shopping-cart"></i> Shopping Cart </a></li>\r\n                          <li role="presentation"><a href="/homepage/checkout"><i class="fa fa-shopping-cart"></i> Checkout </a></li>\r\n')
        if user and user.is_anonymous():
            __M_writer('                          <li role="presentation"><a href="#" id="showLoginModal" data-toggle="modal" data-target="#loginModal"><span class="fa fa-sign-in"></span> Login </a></li>\r\n                          <li role="presentation"><a href="signup.create"><span class="fa fa-user-plus"></span> Sign Up </a></li>\r\n')
        else:
            __M_writer('                              <li role="presentation"><a href="/homepage/myaccount/')
            __M_writer(str(user.id))
            __M_writer('"><i class="fa fa-user"></i> My Account </a></li>\r\n                              <li role="presentation"><a href="/homepage/logout"><span class="fa fa-sign-out"></span> Logout </a></li>\r\n')
        if user and not user.is_anonymous() and user.is_superuser is True:
            __M_writer('                          <li role="presentation">Admin Options</li>\r\n                            <ul class="nav nav-pills nav-stacked">\r\n                                <li role="presentation"><a href="users"><i class="fa fa-users"></i> Users </a></li>\r\n                                <li role="presentation"><a href="photograph"><i class="fa fa-picture-o"></i> Photos </a></li>\r\n                                <li role="presentation"><a href="events"><i class="fa fa-calendar-o"></i> Events </a></li>\r\n                                <li role="presentation"><a href="publicevents"><i class="fa fa-calendar-o"></i> Public Events </a></li>\r\n                            </ul>\r\n')
        __M_writer('                      </ul>\r\n                  ')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_footer(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def footer():
            return render_footer(context)
        __M_writer = context.writer()
        __M_writer('\r\n                      <p class="text-center"><br/><br/><i class="fa fa-copyright"></i>&nbsp;Zach Trayner | Colonial Heritage Foundation</p>\r\n                  ')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"uri": "base.htm", "line_map": {"133": 56, "134": 65, "135": 66, "136": 68, "137": 69, "138": 69, "139": 69, "140": 72, "141": 73, "142": 81, "16": 4, "18": 0, "148": 103, "154": 103, "160": 154, "37": 2, "38": 4, "39": 5, "43": 5, "44": 15, "45": 16, "46": 16, "47": 19, "48": 19, "49": 26, "50": 26, "51": 26, "52": 27, "53": 27, "54": 30, "55": 30, "56": 30, "61": 50, "66": 82, "71": 89, "76": 95, "81": 105, "82": 115, "83": 115, "84": 115, "90": 93, "96": 93, "102": 39, "108": 39, "114": 87, "120": 87, "126": 56}, "source_encoding": "ascii", "filename": "C:\\Users\\Zach\\PycharmProjects\\firstProject\\homepage\\templates/base.htm"}
__M_END_METADATA
"""
