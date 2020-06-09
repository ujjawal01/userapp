class UserException(Exception):

    def __init__(self, source, code, message):
        super().__init__(message)
        self._source = source
        self._code = code

    @property
    def source(self):
        return self._source

    @property
    def code(self):
        return self._code


class InvalidEntityException(UserException):
    pass


class ConflictException(UserException):
    pass

class NoLoggedException(UserException):

    def __init__(self):
        super().__init__(source='authentication', code='required', message='Authentication required')

class EntityDoesNotExistException(UserException):

    def __init__(self):
        super().__init__(source='entity', code='not_found', message='Entity not found')
