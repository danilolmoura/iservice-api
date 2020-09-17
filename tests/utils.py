from application.models import Product, Store, User

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

def create_user(session, autogenerate=False, **kwargs):
    if autogenerate:
        pass

    obj = User(**kwargs)

    return insert_object(session, obj)

def create_store(session, autogenerate=False, **kwargs):
    if autogenerate:
        pass

    obj = Store(**kwargs)

    return insert_object(session, obj)

def create_product(session, autogenerate=False, **kwargs):
    if autogenerate:
        pass

    obj = Product(**kwargs)

    return insert_object(session, obj)
