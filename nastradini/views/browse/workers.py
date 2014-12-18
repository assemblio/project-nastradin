from flask import render_template
from flask.views import MethodView
from nastradini import mongo


class BrowseWorkers(MethodView):
    methods = ['GET']

    def get(self):
        # Render the templates.
        results = mongo.db.persons.aggregate([
            {
                "$group":{
                "_id":
                {
                    "doc_id":"$_id",
                    "city" : "$city",
                    "last_name": "$last_name",
                    "gender": "$gender",
                    "industry": "$industry",
                    "profession": "$profession",
                    "first_name": "$first_name",
                    "minimum_salary_requirement": "$minimum_salary_requirement",
                    "birth_date": "$birth_date",
                    "highest_level_of_education": "$highest_level_of_education"
                }
                }
            },
            {
                "$project":{
                    "doc_id":"$_id.doc_id",
                    "city" : "$_id.city",
                    "last_name": "$_id.last_name",
                    "gender": "$_id.gender",
                    "industry": "$_id.industry",
                    "profession": "$_id.profession",
                    "first_name": "$_id.first_name",
                    "minimum_salary_requirement": "$_id.minimum_salary_requirement",
                    "birth_date": "$_id.birth_date",
                    "highest_level_of_education": "$_id.highest_level_of_education"
                    }
            },
            {
                "$sort":{
                    "last_name":1,
                    "first_name":1
                }
            }

        ])

        return render_template('browse/workers.html',results=results[u'result'])
