from flask import current_app, session, request, render_template
from flask.views import View
from nastradini import mongo, utils
from experienceform import ExperienceForm


class Experience(View):

    methods = ['POST']

    def dispatch_request(self):
        ''' Process inputted applicant info.
            Store applicant data.
            Load third form: Diagnosis.
        '''
        form = ExperienceForm()
        # Now we load the Experience form.
        return render_template('form/experience-information.html', form=form)
