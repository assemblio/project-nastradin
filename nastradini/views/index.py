from flask import current_app, session, request, render_template, redirect, url_for
from flask.views import MethodView
from nastradini import mongo, utils


class Index(MethodView):
    methods = ['GET', 'POST']

    def get(self):
        ''' Dispatch the request.
        '''
        # First, let's clear the session of variables associated to previous applicant registration.
        self.clear_session_variables()

        # Now let's retrieve our list of patients.
        applicant_docs = mongo.db.nastradini.find({}).sort([("_id", -1)])

        # Render the templates.
        return render_template('index.html', applicant_docs=applicant_docs)


    #FIXME: It's a bit confusing to have this logic here. Maybe put it in its own class.
    def post(self):
        ''' Process inputted treatment.
            Store treatment data.
            Return to index page.
        '''

        # Get doc id from session.
        doc_id = utils.get_doc_id()

        # Update the applicant doc with treatment.
        treatment = utils.convert_form_to_json_object(request.form)

        mongo.db.nastradini.update(
            { '_id': doc_id },
            { '$set': { 'applicant': applicant }}
        )

        # Log progress.
        current_app.logger.info('Processed treatment for case %s', doc_id)
        current_app.logger.info('Completed registration of case %s', doc_id)

        # We use redirect instead of render_template so that we can run the logic in this view's get() method.
        return redirect(url_for('index'))


    def clear_session_variables(self):
        ''' Clear variables we've stored in session.
        '''
        session.pop('doc_id', None)
        session.pop('applicant', None)
