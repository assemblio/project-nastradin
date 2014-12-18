from flask import render_template, redirect, url_for, request
from flask.views import MethodView
from nastradini import mongo, utils
from positionform import PositionForm


class Position(MethodView):
    methods = ['GET', 'POST']

    def get(self):
        form = PositionForm()
        return render_template('position.html', form=form)

    def post(self):
        # First, let's get the doc id.
        doc_id = utils.get_doc_id()

        # Create position info object.
        form = PositionForm(request.form)
        json = form.data

        # Store the document.
        mongo.db.positions.update({'_id': doc_id}, json, True)

        return redirect(url_for('browse_internal_positions'))
