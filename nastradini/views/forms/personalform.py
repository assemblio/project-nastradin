# -*- coding: utf-8 -*-
from flask_wtf import Form
from wtforms import TextField, TextAreaField, RadioField


class PersonalInformationForm(Form):

    name = TextField('Name')
    last_name = TextField('Last Name')
    gender = RadioField('Gender', choices=[('Male','Male'),('Female','Female')])
    personal_id = TextField('Personal Id')
    birth_date = TextField('Birth Date')
    birth_place = TextField('Birth Place')
    etnicity = TextField('Etnicity')
    address = TextField('Address')
    actual_profession = TextAreaField('Actual Profession')
