from flask import render_template
from flask.views import MethodView
from nastradini import mongo


class Index(MethodView):
    methods = ['GET']

    def get(self):
        return render_template('index.html')
