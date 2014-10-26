from flask import render_template
from flask.views import View

class EditApplicantRecord(View):

    methods = ['POST']

    def dispatch_request(self):
        pass
