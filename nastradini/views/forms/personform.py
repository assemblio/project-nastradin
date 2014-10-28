from flask_wtf import Form
from wtforms import TextField, TextAreaField, RadioField, DateField, SelectField


class PersonForm(Form):

    cities_list = [
        'Prishtina', 'Ferizaj',
        'Gjakova', 'Gjilan',
        'Prizren'
    ]

    cities_tuple = [
        (x, x) for x in cities_list
    ]

    first_name = TextField('First Name')
    last_name = TextField('Last Name')
    birth_date = TextField('Birth Date')
    gender = RadioField('Gender', choices=[('Male', 'Male'), ('Female', 'Female')], default='Male')
    city = SelectField('City', choices=cities_tuple)

    highest_level_of_education = SelectField('Highest Level of Education',
        choices=[
        ('High School','High School'),
        ('Undergraduate','Undergraduate'),
        ('Graduate','Graduate'),
        ('Doctoral','Doctoral')
        ]
    )

    industry = SelectField('Industry',
        choices=[
        ('Construction','Construction'),
        ('Education','Education'),
        ('Government','Government'),
        ('ICT','ICT')
        ]
    )

    profession = SelectField('Profession',
        choices=[
        ('Electrician','Electrician'),
        ('Teacher','Teacher'),
        ('Manager','Manager'),
        ('Engineer','Engineer')
        ]
    )

    summary = TextAreaField('Summary')
    skills = TextAreaField('Skills (Comma Separated)')


    minimum_salary_requirement = SelectField('Minimum Salary Requirement (Monthly)',
        choices=[
        ('200-299','200-299'),
        ('300-399','300-399'),
        ('400-499','400-499'),
        ('500-599','500-599'),
        ('600-699','600-699'),
        ('700-799','700-799'),
        ('800-899','800-899'),
        ('900-999','900-999'),
        ('1000+','1000+')
        ]
    )
