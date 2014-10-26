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
        ]) #TODO: Make this a radio button in the HTML form.
    city = TextField('City') #TODO: This needs to be select list: [Prishtina, Ferizaj, Gjakova, Gjilan, Prizren]
    highest_level_of_education = TextField('Highest Level of Education') #TODO: This needs to be select list: ["High School", "Undergraduate", "Graduate", "Doctoral"]
    industry = TextField('Industry') #TODO: This needs to be select list: [Construction, Education, Government, Technology]
    profession = TextField('Profession')  #TODO: This needs to be select list: [Electrician, Teacher, Project Manager, Software Engineer]
    skills = TextAreaField('Skills (Comma Separated)')
    minimum_salary_requirement = TextField(
        'Minimum Salary Requirement (Monthly)')  #TODO: This needs to be select list: [200-299, 300-399, 400-499, 500-599, 600-699, 700-799, 800-899, 900-999, 1000+]
