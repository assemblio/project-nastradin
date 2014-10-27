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
        result = mongo.db.persons.find(query)

        # Build response object.
        resp = Response(
            response=json_util.dumps(result), mimetype='application/json')

        # Return response.
        return resp
