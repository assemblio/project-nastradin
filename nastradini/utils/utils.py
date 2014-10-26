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
