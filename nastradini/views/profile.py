from flask import render_template
from flask.views import View
from nastradini import mongo
from bson import json_util
from bson.objectid import ObjectId


class Profile(View):
    method = ['GET']

    def dispatch_request(self,id):

        results = mongo.db.persons.find({"_id":id})

        return render_template('profile.html',results=results)
