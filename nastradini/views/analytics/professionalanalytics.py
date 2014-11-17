from flask.views import View
from flask import render_template
from nastradini import mongo


class ProfessionalAnalytics(View):
    def dispatch_request(self):

        # Get the collection from the database
        industry_result = mongo.db.persons.aggregate([
            {
                "$group": {
                    "_id": {
                        "industry": "$industry"
                    },
                    "shuma": {
                        "$sum":1
                    }
                }
            }
        ])

        # Build JSON to return to the template
        gender_result = mongo.db.persons.aggregate([
            {
                "$group": {
                    "_id": {
                        "gender": "$gender"
                    },
                    "shuma": {
                        "$sum":1
                    }
                }
            }
        ])

        # Create the Gender Results
        gender = {}
        gender['male'] = gender_result['result'][1]['shuma']
        gender['female'] = gender_result['result'][0]['shuma']

        #Create industry array with the results
        industry = []
        for industry_type in industry_result['result']:
            industry.append({'industry': industry_type['_id']['industry'], 'shuma': industry_type['shuma']})

        return render_template('analytics/professional.html', industry=industry, gender=gender)