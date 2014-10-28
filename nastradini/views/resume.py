import os
from flask import current_app
from flask.views import View
from nastradini import mongo
from nastradini import utils
from subprocess import call
import time


class Resume(View):
    method = ['GET']

    def dispatch_request(self, resume_id, template_id):
        resume = mongo.db.persons.find_one({"_id": resume_id})

        par_dir = os.path.join(__file__, os.pardir)
        par_dir_abs_path = os.path.abspath(par_dir)
        app_dir = os.path.dirname(par_dir_abs_path)

        token_value_pairs = {
            "TOKEN-FIRST-NAME": resume['first_name'],
            "TOKEN-LAST-NAME": resume['last_name'],
            "TOKEN-CITY": resume['city'],
            "TOKEN-INDUSTRY": resume['industry'],
            "TOKEN-PROFESSION": resume['profession'],
            "TOKEN-SUMMARY": resume['summary'],
            "TOKEN-SKILLS": resume['skills']
        }

        tex_template_filename = ""
        tex_filename = ""
        pdf_url = ""
        output_dir = "%s/static/resumes" % app_dir

        time_str = str(time.time()).replace('.','')

        if template_id == 1:
            tex_template_filename = "%s/static/resumes/templates/modern-cv/cv_7.tex.template" % app_dir
            tex_filename = "%s/static/resumes/templates/modern-cv/%s-%s-%s-%s.tex" % (app_dir, token_value_pairs["TOKEN-FIRST-NAME"], token_value_pairs["TOKEN-LAST-NAME"], resume_id, time_str)
            pdf_url = "%s/static/resumes/%s-%s-%s-%s.pdf" % (current_app.config['BASE_PATH'], token_value_pairs["TOKEN-FIRST-NAME"], token_value_pairs["TOKEN-LAST-NAME"], resume_id, time_str)
        else:
            tex_template_filename = "%s/static/resumes/templates/stylish-cv/cv_6.tex.template" % app_dir
            tex_filename = "%s/static/resumes/templates/stylish-cv/%s-%s-%s-%s.tex" % (app_dir, token_value_pairs["TOKEN-FIRST-NAME"], token_value_pairs["TOKEN-LAST-NAME"], resume_id, time_str)
            pdf_url = "%s/static/resumes/%s-%s-%s-%s.pdf" % (current_app.config['BASE_PATH'], token_value_pairs["TOKEN-FIRST-NAME"], token_value_pairs["TOKEN-LAST-NAME"], resume_id, time_str)

        print tex_template_filename

        # Create tex file for resume
        with open(tex_template_filename) as f:
            with open(tex_filename, "w") as output:

                for line in f:
                    for token in token_value_pairs:
                        if line != "":
                            line = line.replace(token, token_value_pairs[token])

                    output.write(line)

        arg_output_dir = "-output-directory=" + output_dir
        call(["xelatex", "-interaction=batchmode", arg_output_dir, tex_filename])

        return pdf_url