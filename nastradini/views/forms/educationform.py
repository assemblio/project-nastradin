# -*- coding: utf-8 -*-
from flask_wtf import Form
from wtforms import TextField, RadioField, DateField, TextAreaField


class EducationForm(Form):
    high_school = TextField('Education (High School)')
    high_school_department = TextAreaField('Department')
    trainings = TextAreaField('Trainings')
    university = TextField('University')
    university_department = TextField('Department')
