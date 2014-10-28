from flask_wtf import Form
from wtforms import SelectField


class SearchForm(Form):

    highest_level_of_education = SelectField(
        'Highest Level of Education',
        choices=[
            ("All", "All"),
            ("High School", "High School"),
            ("Undergraduate", "Undergraduate"),
            ("Graduate", "Graduate"),
            ("Doctoral", "Doctoral")
        ]
    )

    industry = SelectField(
        'Industry',
        choices=[
            ("All", "All"),
            ('Construction', 'Construction'),
            ('Education', 'Education'),
            ('Government', 'Government'),
            ('ICT', 'ICT')
        ]
    )

    profession = SelectField(
        'Profession',
        choices=[
            ('Electrician', 'Electrician'),
            ('Teacher', 'Teacher'),
            ('Manager', 'Manager'),
            ('Engineer', 'Engineer')
        ]
    )

    minimum_salary = SelectField(
        'Minimum Salary (Monthly)',
        choices=[
            ('200', '200'),
            ('300', '300'),
            ('400', '400'),
            ('500', '500'),
            ('600', '600'),
            ('700', '700'),
            ('800', '800'),
            ('900', '900')
        ]
    )

    maximum_salary = SelectField(
        'Maximum Salary (Monthly)',
        choices=[
            ('300', '300'),
            ('400', '400'),
            ('500', '500'),
            ('600', '600'),
            ('700', '700'),
            ('800', '800'),
            ('900', '900'),
            ('1000+', '1000+'),
        ]
    )
