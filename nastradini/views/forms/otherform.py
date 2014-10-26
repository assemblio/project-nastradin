from flask_wtf import Form
from wtforms import TextField, DateField, TextAreaField


class OtherForm(Form):
    name = TextField('High School')
    last_name = TextAreaField('University')
    trainings = TextField('Trainings')
    birth_date = DateField('Birth Date')
    birth_place = TextField('Birth Place')
    etnicity = TextField('Etnicity')
    address = TextField('Address')
    actual_profession = TextField('Actual Profession')
