from flask import Response, request
from flask.views import View
from bson import json_util
from nastradini import mongo


class SearchRequest(View):

    methods = ['GET']

    def dispatch_request(self):
        '''
        '''
        # TODO get URL search parameters
        # TODO build JSON query
        result = {}
        if(len(request.args) > 0):
            education = request.args.get('education')
            industry = request.args.get('industry')
            profession = request.args.get('profession')
            minimum_salary = request.args.get('minimum_salary')
            maximum_salary = request.args.get('maximum_salary')

        query = {}
        if education != "All":
            query["highest_level_of_education"] = education

        if industry != "All":
            query["industry"] = industry

        if profession:
            query["profession"] = profession

        if minimum_salary and maximum_salary:
            query["salary_range.max"] = {"$lte": int(maximum_salary)}
            query["salary_range.min"] = {"$gte": int(minimum_salary)}

        # Execute query
        result['table-key'] = mongo.db.persons.find(query)

        result['gender-distribution'] = {}

        male_query = query
        male_query['gender'] = "Male"
        male = mongo.db.persons.find(male_query).count()

        female_query = query
        female_query['gender'] = "Female"
        female = mongo.db.persons.find(female_query).count()

        result['gender-distribution']['male'] = male
        result['gender-distribution']['female'] = female

        result['salary'] = {}
        salary = mongo.db.persons.aggregate([
            {
                "$match": query
            },
            {
                "$group": {
                    "_id": {
                        "salary": "$minimum_salary_requirement"
                    },
                    "count": {
                        "$sum": 1
                    }
                }
            }
        ])
        result['salary'] = salary

        # Build response object.
        resp = Response(
            response=json_util.dumps(result), mimetype='application/json')

        # Return response.
        return resp
