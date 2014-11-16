from flask import render_template, redirect, url_for, request
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

        # Create person info object.
        person_form = PersonForm(request.form)
        person_json = person_form.data

        # Set coordinates
        city = person_json['city']
        person_json['coordinates'] = self.coordinates[city]




        salary_range = person_json['minimum_salary_requirement']
        if salary_range == '1000+':
            person_json['salary_range'] = {
                'min': 1000
            }
        else:
            salary_range_array = salary_range.split('-')
            person_json['salary_range'] = {
                'min': int(salary_range_array[0]),
                'max': int(salary_range_array[1])
            }

        print person_json
        # Store the document.
        mongo.db.persons.update({'_id': doc_id}, person_json, True)

        return redirect(url_for('index'))
