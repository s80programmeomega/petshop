import uuid

DEFAULT_SIZE = 8

def get_uuid(size=DEFAULT_SIZE):
    return uuid.uuid4().hex[:size]