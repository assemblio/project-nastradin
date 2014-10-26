from flask import render_template
from flask.views import MethodView


class Index(MethodView):
    methods = ['GET']

    def get(self):
        # Render the templates.
        return render_template('index.html')
