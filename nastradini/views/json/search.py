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
            query["highest_level_of_education"] = str(education)

        if industry != "All":
            query["industry"] = str(industry)

        if profession:
            query["profession"] = str(profession)

        if minimum_salary and maximum_salary:
            query["salary_range.max"] = {"$lte": int(maximum_salary)}
            query["salary_range.min"] = {"$gte": int(minimum_salary)}

        # Execute query
        result['table-key'] = mongo.db.persons.find(query)

        result['gender-distribution'] = {}

        # Get the gender count from the Database
        gender = mongo.db.persons.aggregate([
            {
                "$match": query,
            },
            {
                "$group": {
                    "_id": "$gender",
                    "count": {
                        "$sum": 1
                    }
                }
            }
        ])

        if gender['result'][0]['count']:
            female = gender['result'][0]['count']
            result['gender-distribution']['male'] = female
        if gender['result'][1]['count']:
            male = gender['result'][1]['count']
            result['gender-distribution']['female'] = male

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
