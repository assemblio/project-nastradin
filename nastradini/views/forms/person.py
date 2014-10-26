from flask import render_template, request
from flask.views import MethodView
from nastradini import mongo, utils
from personform import PersonForm


class Person(MethodView):

    methods = ['GET', 'POST']

    def get(self):
        form = PersonForm()
        return render_template('person.html', form=form)

    def post(self):
        # First, let's get the doc id.
        doc_id = utils.get_doc_id()

        # Create patient info object.
        person_form = PersonForm(request.form)
        person_json = person_form.data

        # Store the document.
        mongo.db.persons.update({'_id': doc_id}, person_json, True)

        return render_template('index.html')
