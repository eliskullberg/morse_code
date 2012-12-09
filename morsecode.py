#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
morsecode.py: Simple flask-based web app

'''
__author__ = "Elis Kullberg"
__copyright__ = "Copyright 2012, Morse Code translator"
__credits__ = ["None"]
__license__ = "GPL"
__version__ = "0.1"
__maintainer__ = "Elis Kullberg"
__email__ = "elis@eliskullberg.com"
__status__ = "Testing"


import os

from flask import *

from mc_lookup import string_to_morse, morse_to_string, LookupWhoops


#
# Flask condfig
#

DEBUG = False
SECRET_KEY = 'set it yourself!'

#
# Flask app instantiation
#
app = Flask(__name__)
app.config.from_object(__name__)


#
# Routing rules
#

@app.route('/')
def index():
    return render_template('splash.html')


@app.route('/translate/<fromlang>')
def translate(fromlang):
    return render_template('translate.html', from_lang = fromlang)


@app.route('/output/<lang>', methods=['GET'])
def output(lang):
    if request.method == 'GET':
        indata = request.args.get('translateString').upper()
        try:
            if lang == "en":
                backdata = string_to_morse(indata)
            elif lang == "mo":
                backdata = morse_to_string(indata)
            else:
                backcdata = "Oops"
            return render_template('output.html', translation = backdata)
        except LookupWhoops:
            return render_template('output.html', 
                translation = "Bad input. Read syntax notes, sucker!")
    else:
        return render_template('output.html', translation = "Ooops")

#
# App script
#

if __name__ == '__main__':
    app.config['TRAP_BAD_REQUEST_ERRORS'] = True
    app.debug = False
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
