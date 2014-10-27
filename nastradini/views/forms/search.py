from flask import render_template, request
from flask.views import MethodView
from searchform import SearchForm


class Search(MethodView):

    methods = ['GET', 'POST']

    def get(self):

        form = SearchForm()
        return render_template('search.html', form=form)
