from flask import Response
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

        # Execute query
        result = mongo.db.persons.find({})

        # Build response object.
        resp = Response(
            response=json_util.dumps(result), mimetype='application/json')

        # Return response.
        return resp
