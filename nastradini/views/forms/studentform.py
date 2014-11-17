from flask_wtf import Form
from wtforms import TextField, TextAreaField, SelectField, RadioField
from checkboxwidgets import MultiCheckboxField


class StudentForm(Form):

    emri = TextField('Emri:')
    mbiemri = TextField('Mbiemri:')

    gjinia = RadioField(
        'Gjinia:',
        choices=[('Mashkull', 'Mashkull'), ('Femer', 'Femer')],
        default='Mashkull')

    qyteti = TextField('Vendbanimi:')
    e_mail = TextField('E-mail:')
    universiteti = SelectField(
        'Universiteti:',
        choices=[('Universiteti Prishtines', 'Universiteti Prishtines'),
        ('UBT', 'UBT'),
        ])
    departamenti = TextAreaField('Departamenti:')

    viti_studimit = SelectField(
        'Viti studimit',
        choices=[('1', '1'), ('2', '2'),
        ('3', '3'), ('4', '4'), ('i diplomuar', 'i diplomuar'),
        ('1 - Master', '1 - Master'), ('2 - Master', '2 - Master'),
        ('i diplomuar - Master', 'i diplomuar - Master')
        ])

    shkathesite_tjera = TextAreaField("Shkathesite tjera(te ndahen me presje):")

    #programming languages checkbox group
    python_lang = MultiCheckboxField("Python", choices=[('Python', 'Python')])
    java_lang = MultiCheckboxField("Java", choices=[('Java', 'Java')])
    vb_lang = MultiCheckboxField("VB", choices=[('VB', 'VB')])
    csharp_lang = MultiCheckboxField("C#", choices=[('C#', 'C#')])
    cpp_lang = MultiCheckboxField("C++", choices=[('C++', 'C++')])

    java_script_lang = MultiCheckboxField(
        "JavaScript",
        choices=[('JavaScript', 'JavaScript')]
    )

    ruby_lang = MultiCheckboxField("Ruby", choices=[('Ruby', 'Ruby')])
    html_lang = MultiCheckboxField("HTML", choices=[('HTML', 'HTML')])
    css_lang = MultiCheckboxField("CSS", choices=[('CSS', 'CSS')])

    objective_c_lang = MultiCheckboxField(
        "Objective-C",
        choices=[('Objective-C', 'Objective-C')]
    )

    php_lang = MultiCheckboxField("PHP", choices=[('PHP', 'PHP')])
    perl_lang = MultiCheckboxField("Perl", choices=[('Perl', 'Perl')])

    tjera_lang = MultiCheckboxField("Tjera", choices=[('Tjera', 'Tjera')])
    gjuhet_tjera_programuese = TextAreaField(
        'Gjuhet tjera programuese(te ndahen me presje)'
    )

    # programming skills level per each language
    niveli_ptyhon = SelectField(
        'Nivelet',
        choices=[('Ekspert', 'Ekspert'),
        ('Mesatar', 'Mesatar'),
        ('Fillestar', 'Fillestar')
        ]
    )

    niveli_java_lang = SelectField(
        'Nivelet',
        choices=[('Ekspert', 'Ekspert'),
        ('Mesatar', 'Mesatar'),
        ('Fillestar', 'Fillestar')
        ]
    )

    niveli_vb_lang = SelectField(
        'Nivelet',
        choices=[('Ekspert', 'Ekspert'),
        ('Mesatar', 'Mesatar'),
        ('Fillestar', 'Fillestar')
        ]
    )

    niveli_csharp_lang = SelectField(
        'Nivelet',
        choices=[('Ekspert', 'Ekspert'),
        ('Mesatar', 'Mesatar'),
        ('Fillestar', 'Fillestar')
        ]
    )

    niveli_cpp_lang = SelectField(
        'Nivelet',
        choices=[('Ekspert', 'Ekspert'),
        ('Mesatar', 'Mesatar'),
        ('Fillestar', 'Fillestar')
        ]
    )

    niveli_java_script_lang = SelectField(
        'Nivelet',
        choices=[('Ekspert', 'Ekspert'),
        ('Mesatar', 'Mesatar'),
        ('Fillestar', 'Fillestar')
        ]
    )

    niveli_ruby_lang = SelectField(
        'Nivelet',
        choices=[('Ekspert', 'Ekspert'),
        ('Mesatar', 'Mesatar'),
        ('Fillestar', 'Fillestar')
        ]
    )

    niveli_html_lang = SelectField(
        'Nivelet',
        choices=[('Ekspert', 'Ekspert'),
        ('Mesatar', 'Mesatar'),
        ('Fillestar', 'Fillestar')
        ]
    )

    niveli_css_lang = SelectField(
        'Nivelet',
        choices=[('Ekspert', 'Ekspert'),
        ('Mesatar', 'Mesatar'),
        ('Fillestar', 'Fillestar')
        ]
    )

    niveli_objective_c_lang = SelectField(
        'Nivelet',
        choices=[('Ekspert', 'Ekspert'),
        ('Mesatar', 'Mesatar'),
        ('Fillestar', 'Fillestar')
        ]
    )

    niveli_php_lang = SelectField(
        'Nivelet',
        choices=[('Ekspert', 'Ekspert'),
        ('Mesatar', 'Mesatar'),
        ('Fillestar', 'Fillestar')
        ]
    )

    niveli_perl_lang = SelectField(
        'Nivelet',
        choices=[('Ekspert', 'Ekspert'),
        ('Mesatar', 'Mesatar'),
        ('Fillestar', 'Fillestar')
        ]
    )
