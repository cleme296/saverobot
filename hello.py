#! /usr/bin/python
# -*- coding:utf-8 -*-

from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def index():
  return render_template('templates.html')

@app.route('/bonjour/<name>')
def hello(name):
  return render_template('templates.html', name=name)

@app.route('/led/on')
def on():
  return 

@app.route('/led/off')


@app.route('/bye/')
def aurevoir():
  return 'Au revoir'

if __name__ == '__main__':
  app.run(debug=True, host='0.0.0.0')
