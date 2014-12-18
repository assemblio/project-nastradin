from flask import render_template
from flask.views import MethodView
from nastradini import mongo


class BrowseInternalPositions(MethodView):
    methods = ['GET']

    def get(self):
        # Render the templates.
        results = mongo.db.positions.find()

        return render_template('browse/internal-positions.html', results=results)
