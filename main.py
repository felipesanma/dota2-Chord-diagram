# -*- coding: utf-8 -*-
"""
Created on Fri Aug 13 14:58:21 2021

@author: Pipe San Martín
"""

from flask import Flask

app = Flask(__name__, static_url_path='')


@app.route('/dota')
def dota2chord_serve_static():
    return app.send_static_file('Dota 2 Heroes.html')


if __name__ == '__main__':
    app.run(threaded=True, port=5000, debug=True)
