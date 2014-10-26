from flask_wtf import Form
from wtforms import TextField, RadioField, DateField, TextAreaField


class ExperienceForm(Form):

    experience1 = TextField('Experience #1')
    experience1_company = TextField('Company and Work Description')
    experience2 = TextField('Experience #2')
    experience2_company = TextAreaField('Company and Work Description')
    experience3 = TextField('Experience #3')
    experience3_company = TextAreaField('Company and Work Description')
    experience4 = TextField('Experience #4')
    experience4_company = TextAreaField('Company and Work Description')
