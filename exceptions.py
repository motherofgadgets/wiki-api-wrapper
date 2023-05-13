class NotFoundException(RuntimeError):
    """Not found."""


class BadRequestException(RuntimeError):
    """Bad request."""


class MyDataNotFound(NotFoundException):
    def __init__(self, input_param):
        super().__init__(f"'{input_param}' not found.")


class BadRequest(BadRequestException):
    def __init__(self, input_param):
        super().__init__(f"'{input_param}' is invalid.")
