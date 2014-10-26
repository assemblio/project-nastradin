from flask import render_template, request
from flask.views import MethodView
from nastradini import mongo, utils
from personform import PersonForm


class Person(MethodView):

    methods = ['GET', 'POST']

    coordinates = {
        "Prishtina": {
            "lat": 42.6662068,
            "lon": 21.1599254
        },
        "Ferizaj": {
            "lat": 42.3719071,
            "lon": 21.1511922
        },
        "Gjakova": {
            "lat": 42.3911916,
            "lon": 20.4279613
        },
        "Gjilan": {
            "lat": 42.4589712,
            "lon": 21.4661479
        },
        "Prizren": {
            "lat": 42.2181194,
            "lon": 20.7407284
        }
    }

    def get(self):
        form = PersonForm()
        return render_template('person.html', form=form)

    def post(self):
        # First, let's get the doc id.
        doc_id = utils.get_doc_id()

        # Create patient info object.
        person_form = PersonForm(request.form)
        person_json = person_form.data

        # Set coordinates
        city = person_json['city']
        person_json['coordinates'] = self.coordinates[city]

        # Store the document.
        mongo.db.persons.update({'_id': doc_id}, person_json, True)

        return render_template('index.html')
