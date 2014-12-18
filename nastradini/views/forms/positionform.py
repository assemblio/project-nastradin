from flask_wtf import Form
from wtforms import TextField, TextAreaField, SelectField


class PositionForm(Form):

    title = TextField('Title')
    industry = SelectField('Industry',
        choices=[
           ('Construction', 'Construction'),
           ('Education', 'Education'),
           ('Government', 'Government'),
           ('ICT', 'ICT')
        ]
    )

    start_date = TextField('Start Date')
    end_date = TextField('End Date')

    description = TextAreaField('Description')

    requirement_1 = TextField('Requirements')
    requirement_2 = TextField('')
    requirement_3 = TextField('')
    requirement_4 = TextField('')
    requirement_5 = TextField('')
