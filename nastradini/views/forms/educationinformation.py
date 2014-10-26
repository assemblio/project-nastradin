from flask import render_template
from flask.views import View
from educationform import EducationForm


class Education(View):

    methods = ['POST']

    def dispatch_request(self):
        ''' First we process inputted applicant info.
            Store applicant data.
            Then we load second form: Applicant Info.
        '''

        form = EducationForm()

        return render_template('form/education-information.html', form=form)
