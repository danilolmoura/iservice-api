def get_headers(token=None):
    headers = {
        'Content-Type': 'application/json'
    }

    return headers

def insert_object(session, obj):
    try:
        session.add(obj)
        session.commit()
        return obj
    except Exception as e:
        session.rollback()
        raise e

def create_resource(session, model, **kwargs):
    obj = model(**kwargs)

    return insert_object(session, obj)