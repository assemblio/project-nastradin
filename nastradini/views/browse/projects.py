from flask import render_template
from flask.views import MethodView
from nastradini import mongo


class BrowseProjects(MethodView):
    methods = ['GET']

    def get(self):
        # Render the templates.
        results = mongo.db.projects.find()

        return render_template('browse/projects.html',results=results)
