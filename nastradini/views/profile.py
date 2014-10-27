from flask import render_template
from flask.views import View
from nastradini import mongo


class Profile(View):
    method = ['GET']

    def dispatch_request(self, id):
        person = mongo.db.persons.find_one({"_id": id})
        return render_template('profile.html', person=person)
