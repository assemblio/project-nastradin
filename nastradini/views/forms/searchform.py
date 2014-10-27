from flask_wtf import Form
from wtforms import TextField


class SearchForm(Form):

    highest_level_of_education = TextField('Highest Level of Education') #TODO: This needs to be select list: ["All", High School", "Undergraduate", "Graduate", "Doctoral"]
    industry = TextField('Industry') #TODO: This needs to be select list: [All, Construction, Education, Government, Technology]
    profession = TextField('Profession')  #TODO: This needs to be select list: [Electrician, Teacher, Project Manager, Software Engineer]
    minimum_salary = TextField(
        'Minimum Salary (Monthly)') #TODO: this is list: [200, 300, 400, 500, 600, 700, 800, 900]
    maximum_salary = TextField(
        'Maximum Salary (Monthly)') #TODO: this is list: [300, 400, 500, 600, 700, 800, 900, 1000+]
