from flask import current_app, request, render_template, redirect, url_for
from flask.views import MethodView
from studentform import StudentForm
from nastradini.utils.utils import Utils
from nastradini import mongo

utils = Utils()


class Student(MethodView):
    methods = ['GET', 'POST']

    def get(self):
        ''' Dispatch the request.
        '''

        form = StudentForm()
        return render_template('student.html', form=form)

    def post(self):
        ''' Store skills form.
            Return to student page.
        '''
        #let's get the doc id from utils.
        doc_id = utils.get_doc_id()
        # Log progress.
        current_app.logger.info('Processed skills form for case %s', doc_id)
        current_app.logger.info('Completed registration of case %s', doc_id)

        self.save_skills_form(doc_id)

        return redirect(url_for('index'))

    def save_skills_form(self, doc_id):

        # Update the patient doc with treatment.
        skills_form = StudentForm(request.form)
        programmer_info = utils.get_structured_skills_form(skills_form)

        mongo.db.developer.update(
            {'_id': doc_id},
            {'$set': {'programmerInfo': programmer_info}},
            True
        )
