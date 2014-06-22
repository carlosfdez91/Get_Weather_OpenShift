from bottle import route, get, post, run, template, request, static_file, default_app, error
from busqueda import buscar
import os

@route('/')
def entrada():
    return template("busqueda.html")

@route('/static/images/<filename>')
def server_static(filename):
    return static_file(filename, root='./static/images/')

@route('/static/css/<filename>')
def server_static(filename):
    return static_file(filename, root='./static/css/')

@post('/resultado')
def busqueda():
    try:
        text = request.forms.get('text')
        if text == "":
            return template ("campo_vacio.html")
        else:
            prevision = buscar(text)
            return template("resultado.html",datos=prevision)
    except:
        return template("error.html")         

@route('/about')
def sobre():
    return template("about.html")

@route('/contacto')
def contacto():
    return template("contacto.html")

import os
from bottle import TEMPLATE_PATH

ON_OPENSHIFT = False
if os.environ.has_key('OPENSHIFT_REPO_DIR'):
    ON_OPENSHIFT = True

if ON_OPENSHIFT:
    TEMPLATE_PATH.append(os.path.join(os.environ['OPENSHIFT_HOMEDIR'], 
                                      'app-root/repo/wsgi/views/'))
    application=default_app()
else:
    run(host='localhost', port=8080)
