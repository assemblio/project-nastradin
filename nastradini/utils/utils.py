from bson import ObjectId


class Utils(object):

    def __init__(self):
        pass

    def get_doc_id(self):
        ''' Get the doc_id.
            First, try to retrieve it from the session.
            If it's not in the session, create one.
        '''
        doc_id = str(ObjectId())
        return doc_id

    def get_structured_skills_form(self, form):

        '''This functions returns a structured json_obj document
            for skills form
        '''

        form_obj = {}
        form_obj = form.data

        json_obj = {}
        json_obj = {
            'personalInfo': {
                'emri': form_obj["emri"],
                'mbiemri': form_obj["mbiemri"],
                'gjinia': form_obj["gjinia"],
                'qyteti': form_obj["qyteti"],
                'e_mail': form_obj["e_mail"],
                'universiteti': form_obj["universiteti"],
                'departamenti': form_obj["departamenti"],
                'viti_studimit': form_obj["viti_studimit"],
                'shkathesite_tjera': form_obj["shkathesite_tjera"],
            },
            'languages': [
                {
                    'language': form_obj['python_lang'],
                    'level': form_obj['niveli_ptyhon']
                },
                {
                    'language': form_obj['java_lang'],
                    'level': form_obj['niveli_java_lang']
                },
                {
                    'language': form_obj['vb_lang'],
                    'level': form_obj['niveli_vb_lang']
                },
                {
                    'language': form_obj['csharp_lang'],
                    'level': form_obj['niveli_csharp_lang']
                },
                {
                    'language': form_obj['cpp_lang'],
                    'level': form_obj['niveli_cpp_lang']
                },
                {
                    'language': form_obj['java_script_lang'],
                    'level': form_obj['niveli_java_script_lang']
                },
                {
                    'language': form_obj['ruby_lang'],
                    'level': form_obj['niveli_ruby_lang']
                },
                {
                    'language': form_obj['html_lang'],
                    'level': form_obj['niveli_html_lang']
                },
                {
                    'language': form_obj['css_lang'],
                    'level': form_obj['niveli_css_lang']
                },
                {
                    'language': form_obj['objective_c_lang'],
                    'level': form_obj['niveli_objective_c_lang']
                },
                {
                    'language': form_obj['php_lang'],
                    'level': form_obj['niveli_php_lang']
                },
                {
                    'language': form_obj['perl_lang'],
                    'level': form_obj['niveli_perl_lang']
                },
                {
                    'language': form_obj['tjera_lang'],
                    'level': form_obj['gjuhet_tjera_programuese']
                }
            ]
        }

        return json_obj

    def bulid_json_obj_for_visualisation(self):

        langs_obj = {
            'fillestar': {
                'python': 0,
                'java': 0,
                'vb': 0,
                'csharp': 0,
                'cpp': 0,
                'javascript': 0,
                'ruby': 0,
                'html': 0,
                'css': 0,
                'objective-c': 0,
                'php': 0,
                'perl': 0,
                'tjera': 0,
            },
            'mesatar': {
                'python': 0,
                'java': 0,
                'vb': 0,
                'csharp': 0,
                'cpp': 0,
                'javascript': 0,
                'ruby': 0,
                'html': 0,
                'css': 0,
                'objective-c': 0,
                'php': 0,
                'perl': 0,
                'tjera': 0,
            },
            'ekspert': {
                'python': 0,
                'java': 0,
                'vb': 0,
                'csharp': 0,
                'cpp': 0,
                'javascript': 0,
                'ruby': 0,
                'html': 0,
                'css': 0,
                'objective-c': 0,
                'php': 0,
                'perl': 0,
                'tjera': 0,
            }
        }

        return langs_obj
