from flask import render_template
from flask.views import View
from mdr import mongo

class ShowApplicantRecord(View):

    methods = ['GET']

    def dispatch_request(self, doc_id):
        ''' View a applicant's record.
        '''
        doc = mongo.db.nastradini.find_one({'_id': doc_id})

        return render_template('applicant-record.html', applicant_doc=doc)
