from flask_wtf import Form
from wtforms import TextField, TextAreaField, SelectField


class ProjectForm(Form):

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

    position_1 = TextField('Positions')
    position_2 = TextField('')
    position_3 = TextField('')
    position_4 = TextField('')
    position_5 = TextField('')
