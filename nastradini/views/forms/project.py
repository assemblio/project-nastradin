from flask import render_template, redirect, request, url_for
from flask.views import MethodView
from nastradini import mongo, utils
from projectform import ProjectForm


class Project(MethodView):
    methods = ['GET', 'POST']

    def get(self):
        form = ProjectForm()
        return render_template('project.html', form=form)

    def post(self):
        # First, let's get the doc id.
        doc_id = utils.get_doc_id()

        # Create project info object.
        form = ProjectForm(request.form)
        json = form.data

        # Store the document.
        mongo.db.projects.update({'_id': doc_id}, json, True)

        return redirect(url_for('browse_projects'))
