from flask import render_template
from flask.views import View
from personalform import PersonalInformationForm


class Personal(View):

    methods = ['POST']

    def dispatch_request(self):
        '''
            Start the form workflow to register a applicant resume.
            Load first form: Personal Info.
        '''
        form = PersonalInformationForm()

        return render_template(
            'form/personal-information.html',
            form=form)
