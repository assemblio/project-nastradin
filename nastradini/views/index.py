from flask import render_template
from flask.views import MethodView
from nastradini import mongo

class Index(MethodView):
    methods = ['GET']

    def get(self):
        # Render the templates.
        results = mongo.db.persons.find({})

        return render_template('index.html',results=results)
