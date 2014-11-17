from flask.views import View
from flask import render_template
from nastradini.utils.utils import Utils
from nastradini import mongo

utils = Utils()


class StudentAnalytics(View):

    def dispatch_request(self):

        viz_json_obj = utils.bulid_json_obj_for_visualisation()

        docs = mongo.db.developer.find({})
        #iterate through collection
        for doc in docs:
            languages = doc['programmerInfo']['languages']
            for lang in languages:
                if lang['language'] != []:
                    lang_level_key = lang['level'].lower()
                    lang_key = lang['language'][0].lower()

                    if lang_key == 'c++':
                        lang_key = 'cpp'
                    elif lang_key == 'c#':
                        lang_key = 'csharp'

                    if lang_level_key != '' and lang_key != '':

                        viz_json_obj[lang_level_key][lang_key] = viz_json_obj[lang_level_key][lang_key] + 1

        return render_template('analytics/student-analytics.html', result=viz_json_obj)
