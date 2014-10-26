from flask_wtf import Form
from wtforms import TextField, TextAreaField, RadioField, DateField


class PersonForm(Form):

    first_name = TextField('First Name')
    last_name = TextField('Last Name')
    birth_date = DateField('Birth Date')
    gender = RadioField(
        'Gender',
        choices=[
            ('Male', 'Male'),
            ('Female', 'Female')
        ])
    city = TextField('City')
    highest_level_of_education = TextField('Highest Level of Education')
    industry = TextField('Industry')
    profession = TextField('Profession')
    skills = TextAreaField('Skills (Comma Separated)')
    minimum_salary_requirement = TextField(
        'Minimum Salary Requirement (Monthly)')
