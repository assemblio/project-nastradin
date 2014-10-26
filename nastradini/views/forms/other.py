from flask import current_app, session, request, render_template
from flask.views import View
from nastradini import mongo, utils
from otherform import OtherForm


class Other(View):

    methods = ['POST']

    def dispatch_request(self):

        form = OtherForm()
        return render_template('form/other-information.html', form=form)
