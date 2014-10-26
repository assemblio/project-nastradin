from flask import session
from bson import ObjectId


class Utils(object):

    def __init__(self):
        pass

    def get_doc_id(self):
        ''' Get the doc_id.
            First, try to retrieve it from the session.
            If it's not in the session, create one.
        '''
        if 'doc_id' in session:
            return session['doc_id']
        else:
            doc_id = str(ObjectId())
            session['doc_id'] = doc_id
            return doc_id

    def convert_form_to_json_object(self, form, keys_to_ignore=None):
        ''' Take a request.form object and convert it into a key-value json object that
            will be stored in Mongo.

            If we try to store form_request object directly then the values will be arrays
            with one string variable in them instead of just being a string variable.

        :param form_request: the form request object.
        :param keys_to_ignore: keys that we want to ignore because their checkbox/radio
                                element wasn't selected in the form.
        '''
        json_obj = {}
        for key in form:
            if keys_to_ignore is not None:
                if key not in keys_to_ignore:
                    json_key = self.to_camel_case(key)
                    json_obj[json_key] = form[key]
            else:
                json_key = self.to_camel_case(key)
                json_obj[json_key] = form[key]

        return json_obj

    def to_camel_case(self, key):
        ''' Convert python property name to camel case equivalent.
            e.g. hello_my_friend ---> helloMyFriend
            :param key: the key to convert.
        '''
        camel_key = []
        capitalize_next_char = False
        for c in key:
            if c == '_':
                capitalize_next_char = True
            else:
                if capitalize_next_char:
                    camel_key.append(c.capitalize())
                    capitalize_next_char = False
                else:
                    camel_key.append(c)

        return "".join(camel_key)